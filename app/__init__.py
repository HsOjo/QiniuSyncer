from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog

from app import common
from app.config import Config
from app.util import pyinstaller
from app.util.log import Log
from .control import init_app
from .res.const import Const
from .res.language import load_language, LANGUAGES
from .res.language.english import English
from .util import github


class Application:
    def __init__(self, args):
        Log.append('app_init', 'Info', 'version: %s' % Const.version)

        self.qt = QApplication(args)
        self.qt.setApplicationName(Const.app_name)
        self.qt.setWindowIcon(QIcon('%s/app/res/icon.png' % pyinstaller.get_runtime_dir()))

        self.config = Config()
        self.config.load()

        self.lang = None  # type: English
        self.load_language(Config.language)

        self.events = {
            'process_events': self.qt.processEvents,
            'export_log': self.export_log,
            'check_update': self.check_update,
            'load_language': self.load_language,
            'get_language': lambda: self.lang,
            'set_language': self.set_language,
            'get_config': lambda: self.config,
        }

    def load_language(self, language):
        self.lang = load_language(language)

    def set_language(self, language):
        self.lang = load_language(language)
        self.config.language = language
        self.config.save()

    def run(self):
        init_app(events=self.events)
        return self.qt.exec_()

    def callback_exception(self):
        exc = common.get_exception()
        Log.append(self.callback_exception, 'Error', exc)

        if QMessageBox.warning(None, self.lang.title_crash, self.lang.description_crash):
            self.export_log()

    def export_log(self):
        folder = QFileDialog.getExistingDirectory(None, caption=self.lang.menu_export_log)
        if folder is not None:
            log = Log.extract_log()
            err = Log.extract_err()

            for f in Config._protect_fields:
                v = getattr(Config, f, '')
                if v != '':
                    log = log.replace(v, Const.protector)
                    err = err.replace(v, Const.protector)

            if log != '':
                with open('%s/%s' % (folder, '%s.log' % Const.app_name), 'w') as io:
                    io.write(log)

            if err != '':
                with open('%s/%s' % (folder, '%s.err' % Const.app_name), 'w') as io:
                    io.write(err)

    def check_update(self, test=False):
        try:
            release = github.get_latest_release(Const.author, Const.app_name, timeout=5)
            Log.append(self.check_update, 'Info', release)

            if test or common.compare_version(Const.version, release['tag_name']):
                if len(release['assets']) > 0:
                    QMessageBox.information(self.lang.title_check_update, '%s\n%s\n\n%s' % (
                        self.lang.description_new_version, release['body'],
                        release['assets'][0]['browser_download_url']))
                else:
                    QMessageBox.information(self.lang.title_check_update, '%s\n%s\n\n%s' % (
                        self.lang.description_new_version,
                        release['body'], release['assets'][0]['browser_download_url']))
        except:
            Log.append(self.check_update, 'Warning', common.get_exception())
