# -*- encoding: utf-8 -*-
__author__ = "Wang Shuhao"

from .Error import TargetSourceEOF
from .FSM import SourceParseFSM
from .ProgFSMState import SourceParseFSMNormalState
from .MakeupFSMState import TargetMakeupStateNormalState
from .Reader import TargetSourceReader
from .HTMLTemplate import HTMLTemplate
from . import SyntaxPerl
from . import SyntaxSQL


__LANG_MAP__ = {
    "perl": SyntaxPerl,
    "sql": SyntaxSQL
}


class Formater(object):
    def __init__(self, title):
        self.title = title
        self.html_render = HTMLTemplate()
        self.codes = {}

    def addCode(self, langName, codeName, codeSource, langType="general"):

        self.codes[codeName] = (langType, langName, codeSource)

    def _lex(self, codeName, codeSource, syntax = None, langType="general"):
        reader = TargetSourceReader()
        reader.setSource(codeSource)

        if syntax is None and langType == "general":
            return [("ident", codeSource)]

        fsm = SourceParseFSM()
        if langType == "makeup":
            fsm.setState(TargetMakeupStateNormalState(fsm, reader, None))
        else:
            fsm.setState(SourceParseFSMNormalState(fsm, reader, syntax))

        run = True
        lexResults = []

        while run:
            try:
                state = fsm.getState()
                tokenType, tokenValue = state.input()
            except TargetSourceEOF as e:
                tokenType, tokenValue = e.params
                run = False
            except Exception:
                tokenType, tokenValue = "ident", reader.getNoParsedSource()
                run = False

            if tokenType is None or tokenValue is None or tokenValue == '':
                continue

            lexResults.append((tokenType, tokenValue))
        return lexResults

    def render(self):

        for codeName, codeContent in self.codes.items():
            langType = codeContent[0]
            langName = codeContent[1]
            codeSource = codeContent[2]

            if langName.lower() not in __LANG_MAP__:
                syntax = None
            else:
                syntax = __LANG_MAP__[langName.lower()].GetSyntax()

            lexResult = self._lex(codeName, codeSource, syntax, langType)
            self.html_render.addParsedCode(codeName, lexResult, syntax)

        return self.html_render.render(self.title)

