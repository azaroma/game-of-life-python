import sys
from PyQt5.QtWidgets import QApplication
import view.worlds as worlds

def main(args=None):
    """ Application entry point. Here is where everything begins. """

    if args is None:
        args = sys.argv[1:]

    print("Life starts thriving...")
    life = QApplication(sys.argv)
    world = worlds.Earth()
    sys.exit(life.exec_())

if __name__ == '__main__':
    main()
