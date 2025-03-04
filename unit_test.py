import pytest
from ui_handler import get_amount, get_category, get_date, get_type
import datetime


def test_get_amount_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "100")
    assert get_amount() == 100.0

def test_get_amount_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Cancel")
    assert get_amount() is None

def test_get_category_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Rent")
    assert get_category() == "Rent"

def test_get_category_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Cancel")
    assert get_category() is None

def test_get_date_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2025-01-01")
    assert get_date() == datetime.date(2025, 1, 1)

def test_get_date_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Cancel")
    assert get_date() is None

def test_get_type_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "income")
    assert get_type() == "income"

def test_get_type_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Cancel")
    assert get_type() is None




    