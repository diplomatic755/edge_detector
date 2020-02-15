from pytest import approx
from images import Picture
from EdgeDetector import Detector
import unittest


class TestDetector1:
    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.Img = Picture()
        self.Det = Detector()

    # test 1
    def test_1(self):
        assert True is True


class TestDetector2:
    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = None

    # test 1
    def test_1(self):
        assert True is True
