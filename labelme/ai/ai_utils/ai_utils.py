from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QProgressDialog

# Thread class for loading the AI model in the background.
class ModelLoaderThread(QThread):
    finished = pyqtSignal()  # Signal to indicate the thread has finished.
    errorOccurred = pyqtSignal(Exception)  # Signal to indicate an error occurred.

    def __init__(self, canvas, model_name):
        super().__init__()
        self.canvas = canvas
        self.model_name = model_name

    def run(self):
        try:
            # Attempt to load the AI model. This is a potentially time-consuming operation.
            self.canvas.initializeAiModel(name=self.model_name)
        except Exception as e:
            # If an error occurs, emit the errorOccurred signal.
            self.errorOccurred.emit(e)
        finally:
            # Once finished, whether successful or not, emit the finished signal.
            self.finished.emit()