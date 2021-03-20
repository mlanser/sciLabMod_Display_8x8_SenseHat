import uuid

import pytest


# =========================================================
#                      G L O B A L S
# =========================================================


# =========================================================
#        G L O B A L   P Y T E S T   F I X T U R E S
# =========================================================
@pytest.fixture()
def default_test_msg(prefix='', suffix='', sep=' '):
    """Create a random test string"""
    msg = sep.join([prefix, uuid.uuid4().hex, suffix])
    return msg
