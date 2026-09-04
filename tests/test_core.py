from apiwatch import compare, snapshot


def test_snapshot():
    item = snapshot(200, {"Content-Type": "text/plain"}, b"hello")
    assert item["status"] == 200
    assert item["size"] == 5
    assert len(item["sha256"]) == 64


def test_compare():
    old = snapshot(200, {"X-Test": "a"}, b"one")
    new = snapshot(201, {"X-Test": "b", "X-New": "1"}, b"two")
    result = compare(old, new)
    assert result["status_changed"]
    assert result["added_headers"] == ["x-new"]
    assert result["changed_headers"] == ["x-test"]
    assert result["body_changed"]
