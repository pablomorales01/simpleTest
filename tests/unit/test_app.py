
import pytest
from app_lib import greeting
from app import app

def test_greeting_basic():
    assert greeting("Pablo") == "Hello, Pablo!"

def test_greeting_trims():
    assert greeting("  Ana  ") == "Hello, Ana!"

def test_greeting_default_world():
    assert greeting("") == "Hello, World!"

def test_index_route():
    test_client = app.test_client()
    resp = test_client.get("/")
    assert resp.status_code == 200
    assert b"Simple CI App" in resp.data
