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
        self.resize(800, 400)
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
        self.rows = int(height / cell_size)
        self.cols = int(width / cell_size)
        rows_index = range(self.rows)
        cols_index = range(self.cols)
        
        self.cells = [[Cell() for c in cols_index]
                      for r in rows_index]
        ((self.make_neighbors(r, c) for c in cols_index) for r in rows_index)
        self.setup_layout()

    def get_cell(self, row, col):
        return self.cells[row][col]

    def setup_layout(self):
        """ Set the widgets in place on the layout. """

        grid_layout = QGridLayout()
        for r, row in enumerate(self.cells):
            for c, col in enumerate(self.cells[r]):
                cell = self.cells[r][c]
                grid_layout.addWidget(cell.label, r, c)
        grid_layout.setSpacing(1)
        self.setLayout(grid_layout)

    def make_neighbors(self, r, c):
        """Determine neighbors clockwise starting from upper left 
        """

        neighbors = [None for n in range(8)]
        if r - 1 >= 0 and c - 1 >= 0:
            neighbors[0] = self.cells[r - 1][c - 1]
        if r - 1 >= 0:
            neighbors[1] = self.cells[r - 1][c]
        if r - 1 >= 0 and c + 1 <= self.cols:
            neighbors[2] = self.cells[r - 1][c + 1]
        if c + 1 <= self.cols:
            neighbors[3] = self.cells[r][c + 1]
        if r + 1 <= self.rows and c + 1 <= self.cols:
            neighbors[4] = self.cells[r + 1][c + 1]
        if r + 1 <= self.rows:
            neighbors[5] = self.cells[r + 1][c]
        if r + 1 <= self.rows and c - 1 >= 0:
            neighbors[6] = self.cells[r + 1][c - 1]
        if c - 1 >= 0:
            neighbors[7] = self.cells[r][c - 1]
                
        return neighbors

class Cell(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setStyleSheet("QLabel {background-color: black}")
        self.alive = False
        self.neighbors = []
        self.willChange = False

    def set_neighbors(self, neighbors):
        """ You don't pick your neighbors """
        
        self.neighbors = neighbors

    def is_alive(self):
        """ Are you alive? """
        
        return self.alive

    def poll_neighbors(self):
        """ Ask your neighbors if they are alive """
        
        alive = 0
        for neigh in self.neighbors:
            if neigh.isAlive():
                alive += 1

            return (alive,)
