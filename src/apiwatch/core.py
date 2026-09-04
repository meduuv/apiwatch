import hashlib


def snapshot(status: int, headers: dict[str, str], body: bytes) -> dict:
    return {"status": status, "headers": {k.lower(): v for k, v in headers.items()}, "size": len(body), "sha256": hashlib.sha256(body).hexdigest()}


def compare(old: dict, new: dict) -> dict:
    old_h, new_h = old.get("headers", {}), new.get("headers", {})
    added = sorted(set(new_h) - set(old_h))
    removed = sorted(set(old_h) - set(new_h))
    changed = sorted(k for k in set(old_h) & set(new_h) if old_h[k] != new_h[k])
    return {"status_changed": old.get("status") != new.get("status"), "added_headers": added, "removed_headers": removed, "changed_headers": changed, "size_changed": old.get("size") != new.get("size"), "body_changed": old.get("sha256") != new.get("sha256")}
