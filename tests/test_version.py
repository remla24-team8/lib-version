from remla24_team8_lib_version import versioning

def test_get_version():
    util = versioning.VersionUtil()
    received_version = util.version
    assert isinstance(received_version, str)
    assert received_version != "0.0.0"