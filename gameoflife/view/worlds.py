from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class Earth(QMainWindow):
    """ This is where life as we know it lives. It is in charge of
    displaying the evolution of the cells matrix and suffer the passing
    of time.
    """

    def __init__(self):
        """ Set the initial state of this planet. """
        
        super().__init__()
        self.resize(400, 400)
        self.center()
        self.setWindowTitle("Planet Earth")
        self.show()

    def center(self):
        """ Center the planet in the universe of your screen. """
            
        rect = self.geometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center_point)
        self.move(rect.topLeft())
