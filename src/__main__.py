import os
import sys
import argparse


_VALID_MODULES_ = ['console']

parser = argparse.ArgumentParser(description="Try displaying content via 'DisplayMod' module",
                                 epilog="NOTE: Only call a module if the corresponding hardware/driver is installed")
parser.add_argument('--mod',
                    action='store',
                    type=str,
                    required=True,
                    help="Display module to use")
parser.add_argument('--msg',
                    action='store',
                    type=str,
                    help="Text to display")

args = parser.parse_args()
display = None

if args.mod not in _VALID_MODULES_:
    print("ERROR: '{}' is not a valid display module!".format(args.mod))
    exit(1)

if args.mod == 'console':
    from .display_console import Display
    display = Display()

if args.msg is None:
    text = "Hello world!"
else:
    text = args.msg

display.display_msg(text)
columns, lines = display.resolution
colors = display.colors

print("COLS: {} - LINES: {} - COLORS: {}".format(columns, lines, colors))
