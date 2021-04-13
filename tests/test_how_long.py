from how_long import __version__
from how_long import how_long


def test_version():
    assert __version__ == "0.1.1"


def test_wrap():
    @how_long.timer
    def wrapped_function():
        return

    assert wrapped_function.__name__ == "wrapped_function"
