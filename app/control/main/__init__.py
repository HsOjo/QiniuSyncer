from PyQt5.QtWidgets import QMainWindow, QFileDialog, QAction

from app.config import Config
from app.res.const import Const
from app.res.language import LANGUAGES
from app.res.language.english import English
from app.view.main import Ui_MainWindow
from .thread.sync import TSync


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)

        self.events = kwargs.get('events')  # type: dict

        self.config = self.events['get_config']()  # type:Config

        self.f_dialog = QFileDialog()
        self.t_sync = TSync()

        self._event_connect()
        self.load_language()

        self.init_languages_menu()

    @property
    def lang(self):
        language = self.events['get_language']()  # type: English
        return language

    def load_language(self):
        self.setWindowTitle(Const.app_name)

        lang_keys = dir(self.lang)
        for k in dir(self):
            item = getattr(self, k)
            set_text = getattr(item, 'setText', None)
            if callable(set_text) and k in lang_keys:
                set_text(getattr(self.lang, k))

    def load_data(self):
        self.le_sync_dir.setText(self.config.sync_dir)
        self.le_bucket.setText(self.config.bucket)
        self.le_access_key.setText(self.config.access_key)
        self.le_secret_key.setText(self.config.secret_key)

    def _event_connect(self):
        self.tb_browser.clicked.connect(self._event_tb_browser_clicked)
        self.pb_sync.clicked.connect(self._event_pb_sync_clicked)

        self.t_sync.sig_progress.connect(self._callback_progress)

    def _event_tb_browser_clicked(self, p):
        path = self.f_dialog.getExistingDirectory(self, 'Select sync directory.')
        self.le_sync_dir.setText(path)

    def _event_pb_sync_clicked(self, p):
        self.config.bucket = self.le_bucket.text()
        self.config.sync_dir = self.le_sync_dir.text()
        self.config.access_key = self.le_access_key.text()
        self.config.secret_key = self.le_secret_key.text()
        self.config.save()

        self.t_sync.set_params(self.config.bucket, self.config.sync_dir, self.config.access_key, self.config.secret_key)
        self.t_sync.start()

    def _callback_progress(self, now, max):
        self.pb_progress.setMaximum(max)
        self.pb_progress.setValue(now)

    def set_language(self, language):
        self.events['set_language'](language)
        self.load_language()

    def init_languages_menu(self):
        for k in LANGUAGES:
            a_lang = QAction(self)
            a_lang.setText(LANGUAGES[k].l_this)
            a_lang.triggered.connect((lambda x: (lambda _: self.set_language(x)))(k))
            self.m_languages.addAction(a_lang)
