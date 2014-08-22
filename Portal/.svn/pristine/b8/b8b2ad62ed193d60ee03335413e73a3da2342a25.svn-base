# -*- encoding: utf-8 -*-
__author__ = 'Wang Shuhao'

from .Error import TargetSourceEOF, TargetSourceSyntaxError
from .FSMState import SourceParseFSMState


class TargetMakeupStateNormalState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()
                if char == "<":
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupTagLPState(self.context, self.inputCtx, None))
                    return "ident", self.inputCtx.getInputBuf()
                elif char == "\n" or char == "\r":
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupEOLStateState(self.context, self.inputCtx, None, self))
                    return None, None
                elif char == ' ' or char == "\t":
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupBlankState(self.context, self.inputCtx, None, self))
                    return None, None
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupBlankState(SourceParseFSMState):
    def input(self):
        prevState = self.args[0]
        while True:
            try:
                char = self.inputCtx.input()
                if char != ' ' and char != '\t':
                    self.inputCtx.uninput()
                    self.setState(prevState)
                    return "separator", self.inputCtx.getInputBuf()

            except TargetSourceEOF as e:
                e.params = ("separator", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupDefineState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()
                if char == "?":
                    char = self.inputCtx.input()
                    if char == ">":
                        self.setState(TargetMakeupStateNormalState(self.context, self.inputCtx, None))
                        return "xmltag", self.inputCtx.getInputBuf()
                    else:
                        e = TargetSourceSyntaxError()
                        e.params = ("ident", self.inputCtx.getInputBuf())
                        raise e

            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupEOLStateState(SourceParseFSMState):
    def input(self):
        """
            self.args[0]  -->  prevState
        """
        char = self.inputCtx.input()
        if char == "\n":
            self.setState(self.args[0])
            return "crlf", self.inputCtx.getInputBuf()
        char = self.inputCtx.input()
        if char == "\r":
            char = self.inputCtx.input()
            if char != "\n":
                self.inputCtx.uninput()
            self.setState(self.args[0])
            return "crlf", self.inputCtx.getInputBuf()
    pass


class TargetMakeupTagLPState(SourceParseFSMState):
    def input(self):
        # read "<"
        self.inputCtx.input()

        char = self.inputCtx.input()
        if char == '?':
            self.setState(TargetMakeupDefineState(self.context, self.inputCtx, None))
            return None, None
        elif char == '!':
            # comment or CDATA?
            # comment start with <!--
            if self.inputCtx.input() + self.inputCtx.input() == "--":
                self.setState(TargetMakeupCommentState(self.context, self.inputCtx, None))
                return None, None
            else:
                self.inputCtx.uninput()
                self.inputCtx.uninput()

            # CDATA start with <![CDATA[
            # shit!!!
            cdata_prefix = []
            for i in range(7):
                cdata_prefix.append(self.inputCtx.input())
            if "".join(cdata_prefix) == "[CDATA[":
                self.setState(TargetMakeupCDataStateStart(self.context, self.inputCtx, None))
                return None, None
            else:
                for i in range(7):
                    self.inputCtx.uninput()

            # shit!!! end!!!
            e = TargetSourceSyntaxError()
            e.params = (None, self.inputCtx.getInputBuf())
            raise e
        else:
            self.inputCtx.uninput()
            self.setState(TargetMakeupTagStartState(self.context, self.inputCtx, None))
            return None, None

    pass


class TargetMakeupTagStartState(SourceParseFSMState):
    def input(self):
        try:
            # shit begin!!!
            char = self.inputCtx.input()
            if char == "<" or char == " " or char == '\t':
                e = TargetSourceSyntaxError()
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e
            elif char == "/":
                self.setState(TargetMakeupTagCloseState(self.context, self.inputCtx, None))
                return None, None
            else:
                while True:
                    char = self.inputCtx.input()
                    if char == " " or char == "\t":
                        nextState = TargetMakeupTagAttrState(self.context, self.inputCtx, None)
                        self.setState(TargetMakeupBlankState(self.context, self.inputCtx, None, nextState))
                        return "xmltag", self.inputCtx.getInputBuf()
                    elif char == "<":
                        e = TargetSourceSyntaxError()
                        e.params = ("ident", self.inputCtx.getInputBuf())
                        raise e
                    elif char == ">":
                        self.inputCtx.uninput()
                        self.setState(TargetMakeupTagCloseState(self.context, self.inputCtx, None))
                        return "xmltag", self.inputCtx.getInputBuf()
            # shit end!!!
        except TargetSourceEOF as e:
            e.params = ("ident", self.inputCtx.getInputBuf())
            raise e
        except:
            raise


class TargetMakeupTagCloseState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()
                if char == " " or char == "\t" or char == "/":
                    e = TargetSourceSyntaxError()
                    e.params = ("ident", self.inputCtx.getInputBuf())
                    raise e
                elif char == ">":
                    self.setState(TargetMakeupStateNormalState(self.context, self.inputCtx, None))
                    return "xmltag", self.inputCtx.getInputBuf()
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e
            except:
                raise


class TargetMakeupTagAttrState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()

                if char == "/":
                    self.setState(TargetMakeupTagCloseState(self.context, self.inputCtx, None))
                    return None, None
                elif char == ">":
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupTagCloseState(self.context, self.inputCtx, None))
                    return None, None
                else:
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupTagAttrNameState(self.context, self.inputCtx, None))
                    return None, None

            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e



class TargetMakeupTagAttrNameState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()
                if char == " " or char == "\t" or char == '=':
                    self.inputCtx.uninput()
                    nextState = TargetMakeupTagAttrAssignState(self.context, self.inputCtx, None)
                    self.setState(TargetMakeupBlankState(self.context, self.inputCtx, None, nextState))
                    return "xmlattr", self.inputCtx.getInputBuf()
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e
        pass

class TargetMakeupTagAttrAssignState(SourceParseFSMState):
    def input(self):

        while True:
            try:
                char = self.inputCtx.input()
                if char != " " and char != "\t" and char != '=':
                    e = TargetSourceSyntaxError()
                    e.params = ("ident", self.inputCtx.getInputBuf())
                    raise e
                elif char == "=":
                    self.setState(TargetMakeupTagAttrValueStartState(self.context, self.inputCtx, None))
                    return "operator", self.inputCtx.getInputBuf()
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupTagAttrValueStartState(SourceParseFSMState):
    def input(self):
        while True:
            try:
                char = self.inputCtx.input()
                if char == " " or char == "\t":
                    self.inputCtx.uninput()
                    self.setState(TargetMakeupBlankState(self.context, self.inputCtx, None, self))
                    return "ident", self.inputCtx.getInputBuf()
                elif char == "'" or char == '"':
                    self.setState(TargetMakeupValueState(self.context, self.inputCtx, None, char))
                    return None, None
                else:
                    e = TargetSourceSyntaxError()
                    e.params = ("ident", self.inputCtx.getInputBuf())
                    raise e
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupValueState(SourceParseFSMState):
    def input(self):
        """
            self.args[0]  --> ' / "

        """
        end = self.args[0]
        while True:
            try:
                char = self.inputCtx.input()
                if char == end:
                    nextState = TargetMakeupTagAttrState(self.context, self.inputCtx, None)
                    self.setState(TargetMakeupBlankState(self.context, self.inputCtx, None, nextState))
                    return "string", self.inputCtx.getInputBuf()
            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e


class TargetMakeupCommentState(SourceParseFSMState):
    def input(self):
        record = []
        while True:
            try:
                char = self.inputCtx.input()
                if char == "-" and len(record) < 2:
                    record.append(char)
                elif char == ">" and len(record) == 2:
                    self.setState(TargetMakeupStateNormalState(self.context, self.inputCtx, None))
                    return "comment", self.inputCtx.getInputBuf()
                else:
                    record = []

            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e

class TargetMakeupCDataStateStart(SourceParseFSMState):
    def input(self):
        record = []
        while True:
            try:
                char = self.inputCtx.input()
                if char == "]" and len(record) < 2:
                    record.append(char)
                elif char == ">" and len(record) == 2:
                    self.setState(TargetMakeupStateNormalState(self.context, self.inputCtx, None))
                    return "xmlcdata", self.inputCtx.getInputBuf()
                else:
                    record = []

            except TargetSourceEOF as e:
                e.params = ("ident", self.inputCtx.getInputBuf())
                raise e

