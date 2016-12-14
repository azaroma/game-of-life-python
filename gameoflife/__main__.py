import sys
from PyQt5.QtWidgets import QApplication
import view.worlds as worlds
import model.heaven as heaven

def main(args=None):
    """ Application entry point. Here is where everything begins. """

    if args is None:
        args = sys.argv[1:]

    print("Life starts thriving...")
    life = QApplication(sys.argv)
    god = heaven.God()
    world = worlds.Earth(god)
    sys.exit(life.exec_())

if __name__ == '__main__':
    main()
