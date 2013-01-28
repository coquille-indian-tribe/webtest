# -*- coding: utf-8 -*-
from webtest.debugapp import DebugApp
from webtest.app import TestApp
from doctest import ELLIPSIS
import os

dirname = os.path.dirname(__file__)


def setup_test(test):
    app = DebugApp(form=os.path.join(dirname, 'form.html'),
                   show_form=True)
    test.globs['app'] = TestApp(app)
    for example in test.examples:
        example.options.setdefault(ELLIPSIS, 1)

setup_test.__test__ = False
