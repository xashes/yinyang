import numpy as np
import pandas as pd


class Board():
    def __init__(self, size) -> None:
        self.size = size
        self.generate_board()

    def generate_board(self):
        data = np.zeros((self.size, self.size))
        columns = list('abcdefghjklmnopqrst'.upper())[:self.size]
        rows = range(19, 0, -1)[:self.size]
        self.board = pd.DataFrame(data, columns=columns, index=rows)