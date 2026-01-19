def test_failed_file(host):
    f = host.file("/tmp/failed")
    assert not f.exists
