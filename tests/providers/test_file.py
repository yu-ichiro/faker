from __future__ import unicode_literals

import unittest
import re

from faker import Faker


class TestFile(unittest.TestCase):
    """ Tests file """

    def setUp(self):
        self.factory = Faker()

    def test_file_path(self):
        for _ in range(100):
            file_path = self.factory.file_path()
            assert re.search(r'\/\w+\/\w+\.\w+', file_path)
            file_path = self.factory.file_path(depth=3)
            assert re.search(r'\/\w+\/\w+\/\w+\.\w+', file_path)
            file_path = self.factory.file_path(extension='pdf')
            assert re.search(r'\/\w+\/\w+\.pdf', file_path)
            file_path = self.factory.file_path(category='image')
            assert re.search(r'\/\w+\/\w+\.(bmp|gif|jpeg|jpg|png|tiff)', file_path)

    def test_unix_device(self):
        reg_device = re.compile('^/dev/(vd|sd|xvd)[a-z]$')
        # Test default
        for _ in range(100):
            path = self.factory.unix_device()
            assert reg_device.match(path)
        # Test with prefix
        for _ in range(100):
            path = self.factory.unix_device('sd')
            assert reg_device.match(path)
            assert path.startswith('/dev/sd')

    def test_unix_partition(self):
        reg_part = re.compile('^/dev/(vd|sd|xvd)[a-z]\d$')
        # Test default
        for _ in range(100):
            path = self.factory.unix_partition()
            assert reg_part.match(path)
        # Test with prefix
        for _ in range(100):
            path = self.factory.unix_partition('sd')
            assert reg_part.match(path)
            assert path.startswith('/dev/sd')
