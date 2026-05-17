#!/usr/bin/env python3
import json, os, sys, tempfile
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.engine import Engine

def test_fetch_data():
    e = Engine("https://sn","admin","pass")
    with patch("src.engine.requests.get", return_value=MagicMock(status_code=200, json=lambda:{"result":[{"sys_id":"s1","name":"A"}]})):
        recs = e.fetch("incident")
    assert len(recs)==1

def test_process():
    e = Engine("https://sn","admin","pass")
    d = e.process([{"sys_id":"s1"}])
    assert d["total"]==1

def test_report_md():
    e = Engine("https://sn","admin","pass")
    with tempfile.TemporaryDirectory() as tmpdir:
        p = os.path.join(tmpdir, "r")
        e.report({"total":1,"items":[{"name":"X"}]}, p)
        assert os.path.exists(p+".md")
        assert "X" in open(p+".md").read()

def test_report_json():
    e = Engine("https://sn","admin","pass")
    with tempfile.TemporaryDirectory() as t:
        p = os.path.join(t, "r")
        e.report({"total":0,"items":[]}, p)
        assert json.load(open(p+".json"))["total"] == 0

def test_empty_handling():
    e = Engine("https://sn","admin","pass")
    assert e.process([])["total"]==0

def test_error_handling():
    e = Engine("https://sn","admin","pass")
    with patch("src.engine.requests.get", side_effect=Exception("err")):
        assert e.fetch("incident") == []

def test_cli_invocation():
    import subprocess, sys
    src = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = subprocess.run([sys.executable, os.path.join(src,"src","cli.py"),"--sn-url","https://sn","--sn-user","admin","--sn-pass","pass"], capture_output=True, text=True)
    assert result.returncode != 2

if __name__=="__main__":
    import pytest
    pytest.main([__file__, "-q"])
