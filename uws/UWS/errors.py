# -*- coding: utf-8 -*-


class UWSError(Exception):
    def __init__(self, msg, raw=False):
        self.msg = msg
        self.raw = raw
