#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

LOG_INF_TPL = """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{?title?}</title>
    <style type="text/css">
        /* GitHub stylesheet for MarkdownPad (http://markdownpad.com) */
        /* Author: Nicolas Hery - http://nicolashery.com */
        /* Version: b13fe65ca28d2e568c6ed5d7f06581183df8f2ff */
        /* Source: https://github.com/nicolahery/markdownpad-github */

        /* RESET
        =============================================================================*/

        html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
          margin: 0;
          padding: 0;
          border: 0;
        }

        /* BODY
        =============================================================================*/

        body {
          font-family: Helvetica, arial, freesans, clean, sans-serif;
          font-size: 14px;
          line-height: 1.6;
          color: #333;
          background-color: #fff;
          padding: 20px;
          max-width: 960px;
          margin: 0 auto;
        }

        body>*:first-child {
          margin-top: 0 !important;
        }

        body>*:last-child {
          margin-bottom: 0 !important;
        }

        /* BLOCKS
        =============================================================================*/

        p, blockquote, ul, ol, dl, table, pre {
          margin: 15px 0;
        }

        /* HEADERS
        =============================================================================*/

        h1, h2, h3, h4, h5, h6 {
          margin: 20px 0 10px;
          padding: 0;
          font-weight: bold;
          -webkit-font-smoothing: antialiased;
        }

        h1 tt, h1 code, h2 tt, h2 code, h3 tt, h3 code, h4 tt, h4 code, h5 tt, h5 code, h6 tt, h6 code {
          font-size: inherit;
        }

        h1 {
          font-size: 28px;
          color: #000;
        }

        h2 {
          font-size: 24px;
          border-bottom: 1px solid #ccc;
          color: #000;
        }

        h3 {
          font-size: 18px;
        }

        h4 {
          font-size: 16px;
        }

        h5 {
          font-size: 14px;
        }

        h6 {
          color: #777;
          font-size: 14px;
        }

        body>h2:first-child, body>h1:first-child, body>h1:first-child+h2, body>h3:first-child, body>h4:first-child, body>h5:first-child, body>h6:first-child {
          margin-top: 0;
          padding-top: 0;
        }

        a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
          margin-top: 0;
          padding-top: 0;
        }

        h1+p, h2+p, h3+p, h4+p, h5+p, h6+p {
          margin-top: 10px;
        }

        /* LINKS
        =============================================================================*/

        a {
          color: #4183C4;
          text-decoration: none;
        }

        a:hover {
          text-decoration: underline;
        }

        /* LISTS
        =============================================================================*/

        ul, ol {
          padding-left: 30px;
        }

        ul li > :first-child,
        ol li > :first-child,
        ul li ul:first-of-type,
        ol li ol:first-of-type,
        ul li ol:first-of-type,
        ol li ul:first-of-type {
          margin-top: 0px;
        }

        ul ul, ul ol, ol ol, ol ul {
          margin-bottom: 0;
        }

        dl {
          padding: 0;
        }

        dl dt {
          font-size: 14px;
          font-weight: bold;
          font-style: italic;
          padding: 0;
          margin: 15px 0 5px;
        }

        dl dt:first-child {
          padding: 0;
        }

        dl dt>:first-child {
          margin-top: 0px;
        }

        dl dt>:last-child {
          margin-bottom: 0px;
        }

        dl dd {
          margin: 0 0 15px;
          padding: 0 15px;
        }

        dl dd>:first-child {
          margin-top: 0px;
        }

        dl dd>:last-child {
          margin-bottom: 0px;
        }

        /* CODE
        =============================================================================*/

        pre, code, tt {
          font-size: 12px;
          font-family: Consolas, "Liberation Mono", Courier, monospace;
        }

        code, tt {
          margin: 0 0px;
          padding: 0px 0px;
          white-space: nowrap;
          border: 1px solid #eaeaea;
          background-color: #f8f8f8;
          border-radius: 3px;
        }

        pre>code {
          margin: 0;
          padding: 0;
          white-space: pre;
          border: none;
          background: transparent;
        }

        pre {
          background-color: #f8f8f8;
          border: 1px solid #ccc;
          font-size: 13px;
          line-height: 19px;
          overflow: auto;
          padding: 6px 10px;
          border-radius: 3px;
        }

        pre code, pre tt {
          background-color: transparent;
          border: none;
        }

        kbd {
            -moz-border-bottom-colors: none;
            -moz-border-left-colors: none;
            -moz-border-right-colors: none;
            -moz-border-top-colors: none;
            background-color: #DDDDDD;
            background-image: linear-gradient(#F1F1F1, #DDDDDD);
            background-repeat: repeat-x;
            border-color: #DDDDDD #CCCCCC #CCCCCC #DDDDDD;
            border-image: none;
            border-radius: 2px 2px 2px 2px;
            border-style: solid;
            border-width: 1px;
            font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
            line-height: 10px;
            padding: 1px 4px;
        }

        /* QUOTES
        =============================================================================*/

        blockquote {
          border-left: 4px solid #DDD;
          padding: 0 15px;
          color: #777;
        }

        blockquote>:first-child {
          margin-top: 0px;
        }

        blockquote>:last-child {
          margin-bottom: 0px;
        }

        /* HORIZONTAL RULES
        =============================================================================*/

        hr {
          clear: both;
          margin: 15px 0;
          height: 0px;
          overflow: hidden;
          border: none;
          background: transparent;
          border-bottom: 4px solid #ddd;
          padding: 0;
        }

        /* TABLES
        =============================================================================*/

        table th {
          font-weight: bold;
        }

        table th, table td {
          border: 1px solid #ccc;
          padding: 6px 13px;
        }

        table tr {
          border-top: 1px solid #ccc;
          background-color: #fff;
        }

        table tr:nth-child(2n) {
          background-color: #f8f8f8;
        }

        /* IMAGES
        =============================================================================*/

        img {
          max-width: 100%
        }
    </style>
</head>
<body>
{?body?}
</body>
</html>
"""

class FmtStateParseAgain(Exception):
    pass


class FmtStateContext(object):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState


class FmtState(object):
    def __init__(self, ctx):
        self.context = ctx

    def setState(self, newState):
        self.context.setState(newState)

    def parse(self, line):
        pass

    def format(self, *contents):
        pass


class FmtStateInit(FmtState):
    def parse(self, line):
        try:
            match = re.match(r"(^\d+\-\d+\-\d+\s+\d+\:\d+\:\d+)(\s+)(Test\scase)(\s+)(.*)$", line.strip())
            if match is None:
                match = re.match(r"^(Entering\s+)(test\s+case\s+)(.*)$", line.strip())
                self.context.setState(FmtStateNoFormat(self.context))
            else:
                self.context.setState(FmtStateHttpURLLine(self.context))

            return self.format(*match.groups())

        except:
            pass

        return None

    def format(self, *contents):
        tpl = "<p><strong>{?title?}</strong>{?normal?}<em>{?file?}</em></p>"
        title = contents[0]
        normal = "".join(contents[1: -1:])
        src_file = contents[-1:][0]

        return tpl.replace("{?title?}", title).replace("{?normal?}", normal).replace("{?file?}", src_file)


class FmtStateHttpURLLine(FmtState):
    def parse(self, line):
        if line.startswith("http"):
            self.context.setState(FmtStateSqlQuoteLine(self.context))
            return self.format(line)
        else:
            #return None
            # FIXME
            raise ValueError(line)
        pass

    def format(self, *contents):
        tpl = "<h2>{?http?}</h2>"

        return tpl.replace("{?http?}", contents[0])


class FmtStateInputParamsTitle(FmtState):
    def parse(self, line):
        # FIXME:
        match = re.match(r"^(.*)(The\s+input\s+parameter\s+is)(.*)$", line.strip())
        if match is None:
            if line.startswith("The results from"):
                self.context.setState(FmtStateResultFromTitle(self.context))
                raise FmtStateParseAgain("")

        self.context.setState(FmtStateNewCode(self.context))

        return self.format(*match.groups())

    def format(self, *contents):
        tpl = "<p>%s</p><h2>%s%s</h2>" % (contents[0], contents[1], contents[2])

        return tpl


class FmtStateNoFormat(FmtState):
    def parse(self, line):
        match = re.match(r"^(.*)(The\s+input\s+parameter\s+is)", line.strip())
        if match:
            self.context.setState(FmtStateInputParamsTitle(self.context))
            raise FmtStateParseAgain("")

        match = re.match(r"\$VAR.*", line.strip())
        if match:
            self.setState(FmtStateNewCode(self.context))
            raise FmtStateParseAgain("")

        return self.format(line)

    def format(self, *contents):
        return "<p>%s</p>" % contents[0]


class FmtStateSqlQuoteLine(FmtState):
    def parse(self, line):
        # is valid line?
        match = re.match(r"^(.*)(The\s+input\s+parameter\s+is)", line.strip())
        if match:
            self.setState(FmtStateInputParamsTitle(self.context))
            raise FmtStateParseAgain("")
        match = re.match(r"\$VAR.*", line.strip())
        if match:
            self.setState(FmtStateNewCode(self.context))
            raise FmtStateParseAgain("")

        self.context.setState(FmtStateResultTitle(self.context))

        return self.format(line)

    def format(self, *contents):
        return "<blockquote><p>%s</p></blockquote>" % (contents[0])


class FmtStateResultTitle(FmtState):
    def parse(self, line):
        self.context.setState(FmtStateNewCode(self.context))

        return self.format(line)

    def format(self, *contents):
        return "<h2>%s</h2>" % (contents[0])


class FmtStateNewCode(FmtState):
    def parse(self, line):
        self.context.setState(FmtStateInCode(self.context))

        return self.format(line)

    def format(self, *contents):
        return "<pre><code>%s" % (contents[0])


class FmtStateInCode(FmtState):
    def parse(self, line):
        if line.startswith("FAILED:") or line.startswith("PASSED:"):
            self.context.setState(FmtStateResultLine(self.context))
            raise FmtStateParseAgain(self.format("</code></pre>"))
        elif line.startswith("The results from"):
            self.context.setState(FmtStateResultFromTitle(self.context))
            raise FmtStateParseAgain(self.format("</code></pre>"))
        else:
            return self.format(line)

    def format(self, *contents):
        return "".join(contents)


class FmtStateResultFromTitle(FmtState):
    def parse(self, line):
        self.setState(FmtStateNewCode(self.context))
        return self.format(line)

    def format(self, *contents):
        return "<h2>%s</h2>" % contents[0]
    pass


class FmtStateResultLine(FmtState):
    def parse(self, line):

        if line.startswith("PASSED"):
            result = "PASSED"
        else:
            result = "FAILED"

        self.context.setState(FmtStateExecuteTimeLine(self.context))

        return self.format("<strong>",
                           result,
                           "</strong>",
                           "<em>",
                           line[6:],
                           "</em>")

    def format(self, *contents):
        return "<p>%s</p>" % ("".join(contents))


class FmtStateExecuteTimeLine(FmtState):
    def parse(self, line):
        return self.format(line)

    def format(self, *contents):
        return "<p>%s</p>" % (contents[0])


class LoggerFormat(object):
    def __init__(self, logger_name, logger_lines):
        self.lines = logger_lines
        self.stateMachine = FmtStateContext()
        self.logger_name = logger_name

    def _parse(self, lines):
        self.stateMachine.setState(FmtStateInit(self.stateMachine))

        outputs = []

        for line in lines:
            state = self.stateMachine.getState()
            try:
                out = state.parse(line)
            except FmtStateParseAgain as e:
                outputs.append(e.message)
                # parse line again
                state = self.stateMachine.getState()
                out = state.parse(line)

            outputs.append(out)

        return "".join(outputs)

    def format(self):
        contents = self._parse(self.lines)
        return LOG_INF_TPL.replace("{?title?}", self.logger_name).replace("{?body?}", contents)


