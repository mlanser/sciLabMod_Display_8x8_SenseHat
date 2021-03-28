import os
import time
import copy

from rich.console import Console
from rich.table import Table
from rich.progress import Progress

from .display_base import _DisplayBase


# =========================================================
#                      G L O B A L S
# =========================================================
# Misc. defaults
_DEFAULT_HOLD_TIME_: int = 0         # 0 sec
_DEFAULT_STYLE_:     str = ''        # Blank string

# Screen resolution for Console display
_SCRN_COLORS_:       int = 2         # We use 'Rich' library, but assume user has only monochrome console.
_SCRN_TYPE_:         str = 'console'


# =========================================================
#        M A I N   C L A S S   D E F I N I T I O N
# =========================================================
class Display(_DisplayBase):
    def __init__(self):
        cols, lines = os.get_terminal_size()
        super().__init__(cols, lines, _SCRN_COLORS_, _SCRN_TYPE_)
        self._console = Console()
        self._progress = Progress()

    def clear(self, attribs=None):
        goHome = (self._parse_attribs(attribs, 'goHome', True) is True)
        holdTime = self._parse_attribs(attribs, 'holdTime', _DEFAULT_HOLD_TIME_)
        time.sleep(holdTime)
        self._console.clear(goHome)

    def display_log(self, data):
        self._console.log(data)

    def display_msg(self, msg='', attribs=None):
        style = self._parse_attribs(attribs, 'style', _DEFAULT_STYLE_)
        self._console.print(msg, style=style)

    def display_table(self, data=None, columns=None, attribs=None):
        style = self._parse_attribs(attribs, 'style', _DEFAULT_STYLE_)
        hasHeader = (columns is not None)

        table = Table(show_header=hasHeader, style=style)
        for col in columns:
            table.add_column(col['title'], style=col['style'], width=col['width'], justify=col['justify'])

        for row in data:
            table.add_row(*row)

        self._console.print(table)

    def display_status(self, tasks=None, msg=None, attribs=None):
        statusMsg = msg if msg is not None else "[green]Processing ..."
        work = copy.deepcopy(tasks)

        with self._console.status(statusMsg):
            while work:
                task = work.pop(0)
                task['action'](task['params'])
                self._console.print("{} complete.".format(task['title']))

    def display_progress(self, tasks=None, msg=None):
        statusMsg = msg if msg is not None else "[green]Processing ..."
        work = copy.deepcopy(tasks)

        with self._progress as progress:
            todo = progress.add_task(statusMsg, total=len(work))

            while work:
                task = work.pop(0)
                task['action'](task['params'])
                if not progress.finished:
                    progress.update(todo, advance=1)
