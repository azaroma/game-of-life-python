from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QLabel, QWidget,
                             QGridLayout, qApp, QAction)

class Earth(QMainWindow):
    """ This is where life as we know it lives. It is in charge of
    displaying the evolution of the cells matrix and suffer the passing
    of time.
    """

    def __init__(self, god):
        """ Set the initial state of this planet. """
        
        super().__init__()
        self.god = god
        self.timer = QTimer()
        self.speed = 500
        self.timer.timeout.connect(self.ask_god)

        self.states = {
            'still': {
                'block': [(30,30),(30,31),(31,30),(31,31)],
                'loaf': [(30,30),(30,31),(31,29),(31,32),(32,30),(32,32),(33,31)],
                'boat': [(30,30),(30,31),(31,30),(31,32),(32,31)],
                'tub': [(30,30),(31,29),(31,31),(32,30)]
            },
            'osc': {
                'blinker': [],
                'toad': [],
                'beacon': [],
                'pulsar': [],
                'penta': []
            },
            'ship': {
                'glider': [],
                'lwss': []
            }
        }

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')        
        exit_action.triggered.connect(qApp.quit)
        block_action = QAction('&Block', self)
        block_action.triggered.connect(lambda: self.set_state('still','block'))
        loaf_action = QAction('&Loaf', self)
        loaf_action.triggered.connect(lambda: self.set_state('still','loaf'))
        boat_action = QAction('&Boat', self)
        boat_action.triggered.connect(lambda: self.set_state('still','boat'))
        tub_action = QAction('&Tub', self)
        tub_action.triggered.connect(lambda: self.set_state('still','tub'))

        blinker_action = QAction('&Blinker', self)
        blinker_action.triggered.connect(lambda: self.set_state('osc','blinker'))
        toad_action = QAction('&Toad', self)
        toad_action.triggered.connect(lambda: self.set_state('osc','toad'))
        beacon_action = QAction('&Peacon', self)
        beacon_action.triggered.connect(lambda: self.set_state('osc','beacon'))
        pulsar_action = QAction('&Pulsar', self)
        pulsar_action.triggered.connect(lambda: self.set_state('osc','pulsar'))
        penta_action = QAction('&Pentadecathlon', self)
        penta_action.triggered.connect(lambda: self.set_state('osc','penta'))

        glider_action = QAction('&Glider', self)
        glider_action.triggered.connect(lambda: self.set_state('ship', 'glider'))
        lwss_action = QAction('&Lightweight spaceship', self)
        lwss_action.triggered.connect(lambda: self.set_state('ship', 'lwss'))

        menubar = self.menuBar()
        main_menu = menubar.addMenu('&Menu')
        main_menu.addAction(exit_action)
        still_menu = menubar.addMenu('&Still life')
        still_menu.addAction(block_action)
        still_menu.addAction(loaf_action)
        still_menu.addAction(boat_action)
        still_menu.addAction(tub_action)
        oscillator_menu = menubar.addMenu('&Oscillators')
        oscillator_menu.addAction(blinker_action)
        oscillator_menu.addAction(toad_action)
        oscillator_menu.addAction(beacon_action)
        oscillator_menu.addAction(pulsar_action)
        oscillator_menu.addAction(penta_action)
        spaceship_menu = menubar.addMenu('&Spaceships')
        spaceship_menu.addAction(glider_action)
        spaceship_menu.addAction(lwss_action)

        self.resize(600, 400)
        self.center()
        self.setWindowTitle("Planet Earth")

        self.grid = Grid(self.height(), self.width())
        self.setCentralWidget(self.grid)

        self.set_state('still', 'block')
        self.timer.start(self.speed)
        self.show()

    def center(self):
        """ Center the planet in the universe of your screen. """
            
        rect = self.geometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center_point)
        self.move(rect.topLeft())

    def ask_god(self):
        for coor in self.states['still']['block']:
            print(self.grid.get_cell(coor[0],coor[1]).poll_neighbors())
        self.god.judge(self.grid.get_cells())

    def set_state(self, category, name):
        self.timer.stop()
        self.clear_grid()
        state = self.states[category][name]
        for pos in state:
            self.grid.get_cell(pos[0], pos[1]).resurrect()
        self.timer.start(self.speed)

    def clear_grid(self):
        self.grid.clear()

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
