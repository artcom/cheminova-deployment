def test_failed_file(host):
    f = host.file("/tmp/failed")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
