import os
from .display_base import _DisplayBase


class Display(_DisplayBase):
    def __init__(self):
        self._cols, self._lines = os.get_terminal_size()
        super().__init__(self._cols, self._lines, 2)

    def display_msg(self, msg=''):
        print(msg)
