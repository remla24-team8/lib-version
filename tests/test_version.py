"""Unit tests for the VersionUtil class in the remla24-team8-lib-version package."""

import unittest

import lib_version.versioning as versioning

class TestVersionUtil(unittest.TestCase):
    """Tests for verifying the functionality of the VersionUtil class."""

    def test_get_version(self):
        """Print to the console: get_version method returns the correct version."""
        util = versioning.VersionUtil()
        received_version = util.get_version()    
        
        print(received_version)


if __name__ == '__main__':
    unittest.main()