
from pm_toolkit.greetings import greet

def test_greet():
    assert greet("World") == "Hello, World!"
def test_farewell():
    from pm_toolkit.greetings import farewell
    result = farewell("Alice")
    assert result == "Goodbye, Alice!"
