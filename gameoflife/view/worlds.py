from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QLabel, QWidget,
                             QGridLayout)

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

        self.grid = Grid(self.height(), self.width())
        self.setCentralWidget(self.grid)
        
        self.show()

    def center(self):
        """ Center the planet in the universe of your screen. """
            
        rect = self.geometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center_point)
        self.move(rect.topLeft())

class Grid(QWidget):
    """ Container of cells. """

    def __init__(self, height, width):
        super().__init__()
        cell_size = 10
        rows_index = range(int(height / cell_size))
        cols_index = range(int(width / cell_size))
        
        self.cells = [[QLabel() for c in cols_index] for r in rows_index]
        self.setup_layout()

    def get_cell(self, row, col):
        return self.cells[row][col]

    def setup_layout(self):
        """ Set the widgets in place on the layout. """

        grid_layout = QGridLayout()
        for r, row in enumerate(self.cells):
            for c, col in enumerate(self.cells[r]):
                cell = self.cells[r][c]
                cell.setStyleSheet("QLabel {background-color: black}")
                grid_layout.addWidget(cell, r, c)
        grid_layout.setSpacing(1)
        self.setLayout(grid_layout)
