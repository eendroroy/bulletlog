# coding=utf-8
import sys
import unittest
from contextlib import contextmanager
from StringIO import StringIO

import logtrail


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class LogtrailTest(unittest.TestCase):
    def test_should_have_a_version(self):
        self.assertNotEqual(
            logtrail.VERSION, None
        )

    def test_should_print_info(self):
        with captured_output() as (out, err):
            logtrail.Logger.i("logtrail.Logger.i")
        self.assertEqual(
            err.getvalue().strip(), ""
        )
        self.assertEqual(
            out.getvalue().strip(), u'\x1b[44m\x1b[30m INFO  \x1b[0m\x1b[34m\ue0b0\x1b[0m logtrail.Logger.i'
        )

    def test_should_print_debug(self):
        with captured_output() as (out, err):
            logtrail.Logger.d("logtrail.Logger.d")
        self.assertEqual(
            err.getvalue().strip(), ""
        )
        self.assertEqual(
            out.getvalue().strip(), u'\x1b[42m\x1b[30m DEBUG \x1b[0m\x1b[32m\ue0b0\x1b[0m logtrail.Logger.d'
        )

    def test_should_print_warn(self):
        with captured_output() as (out, err):
            logtrail.Logger.w("logtrail.Logger.w")
        self.assertEqual(
            err.getvalue().strip(), ""
        )
        self.assertEqual(
            out.getvalue().strip(), u'\x1b[43m\x1b[30m WARN  \x1b[0m\x1b[33m\ue0b0\x1b[0m logtrail.Logger.w'
        )

    def test_should_print_error(self):
        with captured_output() as (out, err):
            logtrail.Logger.e("logtrail.Logger.e")
        self.assertEqual(
            err.getvalue().strip(), ""
        )
        self.assertEqual(
            out.getvalue().strip(), u'\x1b[41m\x1b[30m ERROR \x1b[0m\x1b[31m\ue0b0\x1b[0m logtrail.Logger.e'
        )
