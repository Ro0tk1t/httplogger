#!/usr/bin/env python
# coding=utf-8

from httplogger import accesslog
from unittest import TestCase

from os import path

class Test(TestCase):
    def setUp(self):
        directory = path.join(path.dirname(path.abspath(__file__)), 'access.log')
        self.file = open(directory)

    def test(self):
        self.log_obj = accesslog.LOGS(self.file)
        log = self.log_obj.logs[0]
        self.assertEqual(log.code, '200')
        self.assertEqual(log.RemoteIP, '172.17.0.1')
        self.assertEqual(log.UA, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')

    def tearDown(self):
        self.file.close()
