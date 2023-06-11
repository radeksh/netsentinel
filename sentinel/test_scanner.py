import os
import pytest

from sentinel.main import get_network_from_default_gateway


def test_get_network_from_default_gateway():
    """ This test will only work if you have TEST_NETWORK defined in your environment variable.
        Otherwise it is difficult to simple check what network you are using without duplicating
        tested function.
    """
    assert get_network_from_default_gateway() == os.environ.get('TEST_NETWORK', get_network_from_default_gateway())


@pytest.mark.device_joined
def test_device_joined():
    """ Run this test only in controlled test network environment,
        when you know that device will join the network in less than seconds defined in SCAN_INTERVAL.
    """
    pass


@pytest.mark.device_left
def test_device_left():
    """ Run this test only in controlled test network environment,
        when you know that device will left the network in less than seconds defined in SCAN_INTERVAL."""
    pass
