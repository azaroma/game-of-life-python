class God(object):
    """In charge of marking every cell's destiny according to the rules 
    of Conway's game of life
    """

    def __init__(self):
        super().__init__()

    def judge(self, cells):
        """Subject every cell to your mighty judgement. """
        for row in cells:
            for cell in row:
                self.judge_cell(cell)

    def judge_cell(self, cell):
        """Apply the inevitable rules of life and touch cells. """
        
        alive = cell.poll_neighbors()
        if alive < 2:
            cell.die()
        elif alive > 3:
            cell.die()
        elif alive == 3:
            cell.resurrect()
        else:
            cell.stay()
