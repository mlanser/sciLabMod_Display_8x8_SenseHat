from abc import ABC, abstractmethod


class _DisplayBase(ABC):
    def __init__(self, resX, resY, colors):
        self._resX = resX
        self._resY = resY
        self._colors = colors

    def __str__(self):
        return '{}x{}x{}'.format(self._resX, self._resY, self._colors)

    def __repr__(self):
        return 'RES w{}x h{} x c{}'.format(self._resX, self._resY, self._colors)

    @property
    def colors(self):
        return self._colors

    @property
    def resolution(self):
        return self._resX, self._resY

    @abstractmethod
    def display_msg(self, msg=''):
        pass
