# -*- coding: utf-8 -*-
"""
Non blocking timer to reload all cases. Taken from a Stack Overflow answer by
MestreLion.

https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-
execute-a-function-every-x-seconds-in-python
"""

from threading import Timer


class Delay(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class Repeater(Delay):
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
