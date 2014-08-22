# -*- encoding: utf-8 -*-
__author__ = "Wang Shuhao"


class SourceParseFSMState(object):
    def __init__(self, fsmCtx, inputCtx, syntax, *args):
        self.context = fsmCtx
        self.inputCtx = inputCtx
        self.syntax = syntax
        self.args = args

    def setState(self, newState):
        self.context.setState(newState)

    def input(self):
        pass
