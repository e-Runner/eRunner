# -*- encoding: utf-8 -*-
__author__ = 'Wang Shuhao'

from .Error import TargetSourceEOF


class TargetSourceReader(object):
    def __init__(self):
        self.input_buf = []
        self.input_pos = 0
        self.source = ""
        self.source_len = 0

    def setSource(self, sourceString):
        self.source = sourceString
        self.source_len = len(sourceString)

    def input(self):
        if self.input_pos == self.source_len:
            raise TargetSourceEOF()

        char = self.source[self.input_pos]

        self.input_buf.append(char)
        self.input_pos = self.input_pos + 1

        return char

    def uninput(self):
        if len(self.input_buf):
            self.input_pos -= 1
            self.input_buf.pop()

    def getInputBuf(self):
        ret = "".join(self.input_buf)
        self.input_buf = []
        return ret

    def getNoParsedSource(self):
        return self.source[self.input_pos:]
