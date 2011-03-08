import mox
from unittest import TestCase, main

def setup():
    """setup"""
    self.mox = mox.Mox()

def teardown():
    self.mox.UnsetStubs()
