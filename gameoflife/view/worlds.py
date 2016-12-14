import view.grid as grid
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QWidget,
                             qApp, QAction)

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

        self.build_states()
        self.build_menu()
        self.resize(600, 400)
        self.center()
        self.setWindowTitle("Planet Earth")

        self.grid = grid.get_grid(self.height(), self.width())
        self.setCentralWidget(self.grid)

        self.set_state('osc', 'pulsar')
        self.timer.start(self.speed)
        self.show()

    def center(self):
        """ Center the planet in the universe of your screen. """
            
        rect = self.geometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center_point)
        self.move(rect.topLeft())

    def ask_god(self):
#        for coor in self.states['osc']['beacon']:
#            print(self.grid.get_cell(coor[0],coor[1]).poll_neighbors())
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

    def build_menu(self):
        
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
        beacon_action = QAction('&Beacon', self)
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

    def build_states(self):
        
        self.states = {
            'still': {
                'block': [(30,30),(30,31),(31,30),(31,31)],
                'loaf': [(30,30),(30,31),(31,29),(31,32),(32,30),(32,32),(33,31)],
                'boat': [(30,30),(30,31),(31,30),(31,32),(32,31)],
                'tub': [(30,30),(31,29),(31,31),(32,30)]
            },
            'osc': {
                'blinker': [(20,30),(20,31),(20,32)],
                'toad': [(20,30),(20,31),(20,32),(21,29),(21,30),(21,31)],
                'beacon': [(20,29),(20,30),(21,29),(22,32),(23,31),(23,32)],
                'pulsar': [(15,25),(15,26),(15,27),(17,23),(18,23),(19,23),(20,25),(20,26),(20,27),(17,28),(18,28),(19,28),(15,31),(15,32),(15,33),(17,35),(18,35),(19,35),(20,33),(20,32),(20,31),(19,30),(18,30),(17,30),(22,31),(22,32),(22,33),(23,35),(24,35),(25,35),(27,33),(27,32),(27,31),(25,30),(24,30),(23,30),(22,25),(22,26),(22,27),(23,28),(24,28),(25,28),(27,27),(27,26),(27,25),(25,23),(24,23),(23,23)],
                'penta': []
            },
            'ship': {
                'glider': [(18,30),(19,31),(20,31),(20,30),(20,29)],
                'lwss': []
            }
        }
