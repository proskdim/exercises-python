import importlib

index = importlib.import_module("index")


def test_greet():
    expected = "Hello, World!"
    assert index.greet() == expected


def test_add():
    assert index.add(2, 3) == 5
