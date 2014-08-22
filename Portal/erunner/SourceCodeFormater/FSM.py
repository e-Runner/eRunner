# -*- encoding: utf-8 -*-
# Finite State Machine

__author__ = 'Wang Shuhao'


class SourceParseFSM(object):
    def __init__(self):
        self.state = None

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state
