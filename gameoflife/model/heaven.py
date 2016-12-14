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
        self.execute(cells)

    def judge_cell(self, cell):
        """Apply the inevitable rules of life and touch cells. """
        
        alive = cell.poll_neighbors()
        if alive < 2:
            if cell.is_alive():
                cell.mark_will_die()
        elif alive > 3:
            if cell.is_alive():
                cell.mark_will_die()
        elif alive == 3:
            if not cell.is_alive():
                cell.mark_will_resurrect()
        
    def execute(self, cells):
        for row in cells:
            for cell in row:
                cell.obey()
        
