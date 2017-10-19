from PyQt5.QtWidgets import QMainWindow, QFileDialog

from ..thread.sync import TSync
from ..view.main import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.f_dialog = QFileDialog()
        self.t_sync = TSync()

        self._event_connect()

    def _event_connect(self):
        self.tb_browser.clicked.connect(self._event_tb_browser_clicked)
        self.pb_sync.clicked.connect(self._event_pb_sync_clicked)

        self.t_sync.sig_progress.connect(self._callback_progress)

    def _event_tb_browser_clicked(self, p):
        path = self.f_dialog.getExistingDirectory(self, 'Select sync directory.')
        self.le_sync_dir.setText(path)

    def _event_pb_sync_clicked(self, p):
        bucket = self.le_bucket.text()
        path = self.le_sync_dir.text()
        self.t_sync.set_params(bucket, path)
        self.t_sync.start()

    def _callback_progress(self, now, max):
        self.pb_progress.setMaximum(max)
        self.pb_progress.setValue(now)
