"""Test for the versioning module of the remla24_team8_lib_version package."""
from remla24_team8_lib_version import versioning

def test_get_version():
    """
    Test the get_version method of VersionUtil class.

    This test verifies that the `get_version` method of the VersionUtil class
    returns a non-empty string version that is not equal to "0.0.0".
    """
    util = versioning.VersionUtil()
    received_version = util.version
    print(f"Received version: {received_version}")

    assert isinstance(received_version, str)
    assert received_version != "0.0.0" and received_version != "9.9.9"
