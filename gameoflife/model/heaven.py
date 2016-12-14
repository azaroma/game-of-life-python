class God(object):
    """In charge of marking every cell's destiny according to the rules 
    of Conway's game of life
    """

    def __init__(self):
        super().__init__()

    def judge(self, cells):
        for row in cells:
            for cell in row:
                judge_cell(cell)

    def judge_cell(self, cell):
        """Apply the inevitable rules of life and touch cells. """
        
        alive = cell.poll_neighbors()[0]
        if alive < 2:
            cell.die()
        elif alive > 3:
            cell.die()
        elif alive == 3:
            cell.resurect()
        else:
            cell.stay()
