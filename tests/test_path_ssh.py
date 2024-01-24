from pathlib import Path

from app.get_ssh_path import getssh


def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh()
    assert x == Path("/abc/.ssh")
