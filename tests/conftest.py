import time
import uuid
import pprint
from faker import Faker

from inspect import getframeinfo

import pytest


# =========================================================
#                      H E L P E R S
# =========================================================
class Helpers:
    @staticmethod
    def pp(capsys, data, frame=None):
        with capsys.disabled():
            _PP_ = pprint.PrettyPrinter(indent=4)
            print('\n')
            if frame is not None:
                print('LINE #: {}\n'.format(getframeinfo(frame).lineno))
            _PP_.pprint(data)


# =========================================================
#        G L O B A L   P Y T E S T   F I X T U R E S
# =========================================================
@pytest.fixture()
def helpers():
    return Helpers


@pytest.fixture()
def default_test_msg(prefix='', suffix='', sep=' '):
    """Create a random test string"""
    msg = sep.join([prefix, uuid.uuid4().hex, suffix])
    return msg


@pytest.fixture()
def valid_string():
    return 'Valid TEST string'


@pytest.fixture()
def valid_data():
    faker = Faker()

    return dict(
        headers=[
            {'title': '#', 'style': 'bold', 'width': 3, 'justify': 'center'},
            {'title': 'Name', 'style': 'bold', 'width': 20, 'justify': 'left'},
            {'title': 'Street', 'style': 'blue', 'width': 35, 'justify': 'center'},
            {'title': 'City', 'style': 'italic green', 'width': 15, 'justify': 'right'},
            {'title': 'Zip', 'style': 'yellow', 'width': 5, 'justify': 'left'},
        ],
        data=[
            ['1', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
            ['2', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
            ['3', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
            ['4', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
            ['5', faker.name(), faker.street_address(), faker.city(), faker.postcode()],
        ]
    )


@pytest.fixture()
def valid_tasks():
    return [
        {'title': 'Simple task',  'action': time.sleep, 'params': 0},
        {'title': 'Medium task',  'action': time.sleep, 'params': 0},
        {'title': 'Complex task', 'action': time.sleep, 'params': 0},
    ]



