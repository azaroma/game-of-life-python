from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

def get_grid(height, width):
    return Grid(height, width)

class Grid(QWidget):
    """ Container of cells. """

    def __init__(self, height, width):
        super().__init__()
        cell_size = 10
        self.rows = int(height / cell_size)
        self.cols = int(width / cell_size)
        self.rows_index = range(self.rows)
        self.cols_index = range(self.cols)
        
        self.cells = [[Cell() for c in self.cols_index]
                      for r in self.rows_index]
        for r in self.rows_index:
            for c in self.cols_index:
                self.get_cell(r,c).set_neighbors(self.make_neighbors(r,c))
        self.setup_layout()

    def get_cells(self):
        return self.cells

    def clear(self):
        for r in self.rows_index:
            for c in self.cols_index:
                self.get_cell(r,c).die()

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
        if r - 1 >= 0 and c + 1 < self.cols:
            neighbors[2] = self.cells[r - 1][c + 1]
        if c + 1 < self.cols:
            neighbors[3] = self.cells[r][c + 1]
        if r + 1 < self.rows and c + 1 < self.cols:
            neighbors[4] = self.cells[r + 1][c + 1]
        if r + 1 < self.rows:
            neighbors[5] = self.cells[r + 1][c]
        if r + 1 < self.rows and c - 1 >= 0:
            neighbors[6] = self.cells[r + 1][c - 1]
        if c - 1 >= 0:
            neighbors[7] = self.cells[r][c - 1]
                
        return neighbors

class Cell(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setStyleSheet("QLabel {background-color: black}")
        self.label.setFixedWidth(16)
        self.alive = False
        self.neighbors = []
        self.will_die = False
        self.will_resurrect = False

    def set_neighbors(self, neighbors):
        """ You don't pick your neighbors """
        
        self.neighbors = neighbors

    def is_alive(self):
        """ Are you alive? """
        
        return self.alive

    def mark_will_die(self):
        self.will_die = True

    def mark_will_resurrect(self):
        self.will_resurrect = True

    def obey(self):
        if self.will_die:
            self.die()
        elif self.will_resurrect:
            self.resurrect()

    def die(self):
        if self.is_alive():
            self.alive = False
            self.will_die = False
            self.will_resurrect = False
            self.label.setStyleSheet("QLabel {background-color: black}")

    def resurrect(self):
        if not self.is_alive():
            self.alive = True
            self.will_die = False
            self.will_resurrect = False
            self.label.setStyleSheet("QLabel {background-color: white}")

    def stay(self):
        pass

    def poll_neighbors(self):
        """ Ask your neighbors if they are alive """
        
        alive = 0
        for neigh in self.neighbors:
            if neigh is not None and neigh.is_alive():
                alive += 1

        return alive
