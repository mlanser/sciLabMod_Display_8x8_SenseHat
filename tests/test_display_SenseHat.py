import time
import pytest

from sense_hat import SenseHat

from libs.displayMod.src.display_SenseHat import Display


# =========================================================
#     G L O B A L S   &   P Y T E S T   F I X T U R E S
# =========================================================
@pytest.fixture()
def valid_attribs():
    return {
        'doDim': False,
        'rotation': 0,
        'holdTime': 1,
        'speed': 0.2,
        'fgColor': (255, 0, 0),
        'bgColor': (0, 0, 0),
        'clearColor': (128, 128, 128),
    }


# =========================================================
#                T E S T   F U N C T I O N S
# =========================================================
def test_clear_no_attribs(mocker):
    mocker.patch.object(time, 'sleep')

    display = Display()
    mocker.patch.object(display._display, 'clear')

    display.clear()
    time.sleep.assert_called_once_with(0)
    display._display.clear.assert_called_once_with((0, 0, 0))


def test_clear_with_attribs(mocker, valid_attribs):
    mocker.patch.object(time, 'sleep')

    display = Display()
    mocker.patch.object(display._display, 'clear')

    attribs = valid_attribs
    display.clear(attribs)
    time.sleep.assert_called_once_with(attribs['holdTime'])
    display._display.clear.assert_called_once_with(attribs['clearColor'])


def test_display_msg(mocker, valid_attribs, valid_string):
    display = Display()
    mocker.patch.object(Display, '_init_display')
    mocker.patch.object(display._display, 'show_message')

    text = valid_string
    attribs = valid_attribs
    display.display_msg(text, attribs)
    display._display.show_message.assert_called_once_with(
        text,
        scroll_speed=attribs['speed'],
        text_colour=attribs['fgColor'],
        back_colour=attribs['bgColor']
    )


def test_display_msg_with_single_letter(mocker, valid_attribs):
    display = Display()
    mocker.patch.object(Display, '_init_display')
    mocker.patch.object(display._display, 'show_letter')

    letter = "M"
    attribs = valid_attribs
    display.display_msg(letter, attribs)
    display._display.show_letter.assert_called_once_with(
        letter,
        text_colour=attribs['fgColor'],
        back_colour=attribs['bgColor']
    )


def test_display_status(mocker, valid_tasks, valid_attribs):
    display = Display()
    mocker.patch.object(Display, '_init_display')
    mocker.patch.object(display._display, 'show_message')

    tasks = valid_tasks
    attribs = valid_attribs
    display.display_status(tasks, "TEST MSG", attribs)
    display._display.show_message.assert_called()
    assert display._display.show_message.call_count == len(tasks) + 1


# if False:
#     pp(capsys, data, currentframe())
#     pp(capsys, dataHdrs['sql'], currentframe())
#     pp(capsys, dataHdrs['raw'], currentframe())
#     pp(capsys, dataFName, currentframe())
#     pp(capsys, tblName, currentframe())
#     pp(capsys, dataOut, currentframe())
#     pp(capsys, dataIn, currentframe())
