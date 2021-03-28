import time
import pytest

from rich.table import Table

from libs.displayMod.src.display_console import Display


# =========================================================
#     G L O B A L S   &   P Y T E S T   F I X T U R E S
# =========================================================
@pytest.fixture()
def valid_attribs():
    return {
        'goHome': False,
        'holdTime': 1,
        'style': "bold red"
    }


# =========================================================
#                T E S T   F U N C T I O N S
# =========================================================
def test_clear_no_attribs(mocker):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))
    mocker.patch.object(time, 'sleep')

    display = Display()
    mocker.patch.object(display._console, 'clear')

    display.clear()
    time.sleep.assert_called_once_with(0)
    display._console.clear.assert_called_once_with(True)


def test_clear_with_attribs(mocker, valid_attribs):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))
    mocker.patch.object(time, 'sleep')

    display = Display()
    mocker.patch.object(display._console, 'clear')

    attribs = valid_attribs
    display.clear(attribs)
    time.sleep.assert_called_once_with(attribs['holdTime'])
    display._console.clear.assert_called_once_with(attribs['goHome'])


def test_display_log(mocker):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))

    display = Display()
    mocker.patch.object(display._console, 'log')

    data = ['apple', 'banana', 'orange']
    display.display_log(data)
    display._console.log.assert_called_once_with(data)


def test_display_msg(mocker, valid_attribs, valid_string):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))

    display = Display()
    mocker.patch.object(display._console, 'print')

    attribs = valid_attribs
    text = valid_string
    display.display_msg(text, attribs)
    display._console.print.assert_called_once_with(text, style="bold red")


def test_display_table(mocker, valid_attribs, valid_data):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))
    mocker.patch.object(Table, 'add_column')
    mocker.patch.object(Table, 'add_row')

    display = Display()
    mocker.patch.object(display._console, 'print')

    attribs = valid_attribs
    data = valid_data
    display.display_table(data['data'], data['headers'], attribs)
    assert Table.add_column.call_count == len(data['headers'])
    assert Table.add_row.call_count == len(data['data'])
    display._console.print.assert_called_once()


def test_display_status(mocker, valid_tasks):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))

    display = Display()
    mocker.patch.object(display._console, 'print')
    mocker.patch.object(display._console, 'status')

    tasks = valid_tasks
    display.display_status(tasks, "TEST MSG")
    display._console.status.assert_called()
    assert display._console.print.call_count == len(tasks)


def test_display_progress(mocker, valid_tasks):
    mocker.patch('os.get_terminal_size', return_value=(80, 80))

    display = Display()
    mocker.patch.object(display._progress, 'update')

    tasks = valid_tasks
    display.display_progress(tasks, "TEST MSG")
    display._progress.update.assert_called()
    assert display._progress.update.call_count == len(tasks)
