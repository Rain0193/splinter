import os
import unittest

from nose.tools import raises
from splinter.browser import Browser
from fake_webapp import EXAMPLE_APP
from base import WebDriverTests


class FirefoxBrowserTest(WebDriverTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('webdriver.firefox')

    def setUp(self):
        self.browser.visit(EXAMPLE_APP)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_attach_file(self):
        "should provide a way to change file field value"
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mockfile.txt')
        self.browser.attach_file('file', file_path)
        self.browser.find_by_name('upload').first.click()

        html = self.browser.html
        assert 'text/plain' in html
        assert open(file_path).read() in html

    @raises(NotImplementedError)
    def test_mouse_over(self):
        "Firefox should not support mouseover"
        self.browser.find_by_id('visible').first.mouseover()

    @raises(NotImplementedError)
    def test_mouse_out(self):
        "Firefox should not support mouseout"
        self.browser.find_by_id('visible').first.mouseout()
