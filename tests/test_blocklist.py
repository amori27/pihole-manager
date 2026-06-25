from src.core.blocklist import BlocklistManager


def test_add_and_list_domains(tmp_path):
    path = tmp_path / "blocklist.txt"
    mgr = BlocklistManager(str(path))
    mgr.add_domain("tracker.example.com")
    mgr.add_domain("ads.example.org")
    domains = mgr.list_domains()
    assert "tracker.example.com" in domains
    assert "ads.example.org" in domains
    assert mgr.count() == 2


def test_remove_domain(tmp_path):
    path = tmp_path / "blocklist.txt"
    mgr = BlocklistManager(str(path))
    mgr.add_domain("spam.com")
    mgr.remove_domain("spam.com")
    assert mgr.count() == 0


def test_no_duplicates(tmp_path):
    path = tmp_path / "blocklist.txt"
    mgr = BlocklistManager(str(path))
    assert mgr.add_domain("test.com") is True
    assert mgr.add_domain("test.com") is False
    assert mgr.count() == 1


def test_remove_nonexistent(tmp_path):
    path = tmp_path / "blocklist.txt"
    mgr = BlocklistManager(str(path))
    assert mgr.remove_domain("nonexistent.com") is False


def test_empty_blocklist(tmp_path):
    path = tmp_path / "blocklist.txt"
    mgr = BlocklistManager(str(path))
    assert mgr.list_domains() == []
    assert mgr.count() == 0
