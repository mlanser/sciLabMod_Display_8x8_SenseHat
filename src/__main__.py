import time
from faker import Faker
import argparse


# =========================================================
#                       G L O B A L S
# =========================================================
faker = Faker()

_DISPLAY_ATTRIBS_ = {
    'console': {
        'doClear': True,
        'holdTime': 1,
        'style': 'bold blue',
    },
    'led8x8sh': {
        'doClear': True,
        'doDim': True,
        'clearColor': (0, 0, 0),
        'rotation': 270,
        'speed': 0.1,
        'fgColor': (128, 0, 0),
        'bgColor': (0, 0, 0),
        'holdTime': 1,
    }
}

_SAMPLE_DATA_ = {
    'headers': [
        {'title': '#', 'style': 'bold', 'width': 3, 'justify': 'center'},
        {'title': 'Name', 'style': 'bold', 'width': 20, 'justify': 'left'},
        {'title': 'Street', 'style': 'blue', 'width': 35, 'justify': 'center'},
        {'title': 'City', 'style': 'italic green', 'width': 15, 'justify': 'right'},
        {'title': 'Zip', 'style': 'yellow', 'width': 5, 'justify': 'left'},
    ],
    'data': [
        ['1', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['2', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['3', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['4', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['5', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['6', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['7', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['8', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['9', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['10', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ['000', '12345678901234567890', '12345678901234567890123456789012345', '123456789012345', '12345'],
    ]
}

_SAMPLE_TASKS_ = [
    {'title': 'Simple task', 'action': time.sleep, 'params': 2},
    {'title': 'Medium task', 'action': time.sleep, 'params': 2},
    {'title': 'Complex task', 'action': time.sleep, 'params': 2},
]


# =========================================================
#                  C L I   P A R S E R
# =========================================================
parser = argparse.ArgumentParser(
    description="Try displaying content via 'DisplayMod' module",
    epilog="NOTE: Only call a module if the corresponding hardware/driver is installed"
)
parser.add_argument(
    '--mod',
    action='store',
    type=str,
    required=True,
    help="Display module to use"
)
parser.add_argument(
    '--msg',
    action='store',
    type=str,
    help="Text to display"
)
parser.add_argument(
    '--clear',
    action='store_true',
    help="Clear console after 5 secs"
)

args = parser.parse_args()
display = None

if args.mod not in _DISPLAY_ATTRIBS_:
    print("ERROR: '{}' is not a valid display module!".format(args.mod))
    exit(1)

if args.msg is None:
    text = "Hello world!"
else:
    text = args.msg

if args.mod == 'console':
    from .display_console import Display

if args.mod == 'led8x8sh':
    from .display_SenseHat import Display

# =========================================================
#     M A I N   F U N C T I O N S   /   A C T I O N S
# =========================================================
display = Display()
display.display_log(['apple', 'banana', 'orange'])
display.display_msg(text, _DISPLAY_ATTRIBS_[args.mod])
display.display_table(_SAMPLE_DATA_['data'], _SAMPLE_DATA_['headers'], _DISPLAY_ATTRIBS_[args.mod])

display.display_status(_SAMPLE_TASKS_, "Working ...", _DISPLAY_ATTRIBS_[args.mod])
display.display_progress(_SAMPLE_TASKS_)

columns, lines = display.resolution
colors = display.colors

print("COLS: {} - LINES: {} - COLORS: {}".format(columns, lines, colors))

if args.clear:
    display.clear({'holdTime': 5})
