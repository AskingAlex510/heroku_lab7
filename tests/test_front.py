import unittest

import app

def test_test():
    assert app.test() == "Frontend Testing Works!"

    assert app.text() != "Frontend Testing Does Not Work"
