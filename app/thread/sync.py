from PyQt5.QtCore import pyqtSignal, QThread

from ..model.seven_cow import SevenCow


class TSync(QThread):
    sig_progress = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.model = SevenCow()
        self.bucket = ''
        self.sync_dir = ''

    def set_params(self, bucket, sync_dir):
        self.bucket = bucket
        self.sync_dir = sync_dir

    def run(self):
        self.model.use(self.bucket)
        self.model.sync_dir(self.sync_dir, False, self.sig_progress.emit)
