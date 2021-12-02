from PyQt6.QtCore import pyqtSignal, QThread

from app.util.seven_cow import SevenCow


class TSync(QThread):
    sig_progress = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.sc = SevenCow()

        self.bucket = ''
        self.sync_dir = ''

    def set_params(self, bucket, sync_dir, access_key, secret_key):
        self.sc.auth(access_key, secret_key)
        self.bucket = bucket
        self.sync_dir = sync_dir

    def run(self):
        self.sc.use(self.bucket)
        self.sc.sync_dir(self.sync_dir, False, self.sig_progress.emit)
