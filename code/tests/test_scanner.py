import os
import pytest

from netsentinel.code.scanner import get_network_from_default_gateway


def test_get_network_from_default_gateway():
    """ This test would only run if you have test network defined in your environment variable.
        Otherwise it is difficult to simple check what network you are using.
    """
    if test_network_cidr := os.environ.get('TEST_NETWORK', None):
        assert get_network_from_default_gateway() == test_network_cidr


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
