# -*- encoding: utf-8 -*-
__author__ = "Wang Shuhao"

import re


__HTML_TPL__ = """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{?title?}</title>
    <style type="text/css">
        html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
          margin: 0;
          padding: 0;
          border: 0;
        }

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

        .keyword {
            color: #00f
        }

        .var {
            color: #990;
        }

        .number {
            color: #909;
        }

        .string {
            color: #999;
        }

        .operator {
            color: #009;
        }

        .comment {
            color: #090;
        }

        .xmltag {
            color: #00f;
        }

        .xmlattr {
            color: #f00;
        }

        .xmlattr_value {
            color: #f0f;
        }

        .xmlcdata {
            color:#f90;
        }

    </style>
</head>
<body>
</body>
{?htmlCode?}
</html>
"""


class HTMLTemplate(object):

    def __init__(self):
        self.codes = {}
        pass

    def _format_type(self, typeName, value, syntax):
        value = value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;")
        value = value.replace("\"", "&quot;")

        if typeName == "ident":
            tmpValue = value
            if syntax is None:
                return value

            if syntax and not syntax["matchcase"]:
                tmpValue = value.lower()

            if tmpValue in syntax["keyword"]:
                return '<span class="keyword">%s</span>' % value
            elif re.match(syntax["number"], value):
                return '<span class="number">%s</span>' % value
            elif len(syntax["var"]) and re.match(syntax["var"], value):
                return '<span class="var">%s</span>' % value
            else:
                return value
        elif typeName == "separator" or typeName == "operator":
            return '<span class="operator">%s</span>' % value

        elif typeName == "comment":
            return '<span class="comment">%s</span>' % value

        elif typeName == "crlf":
            return value

        elif typeName == "string":
            return '<span class="string">%s</span>' % value

        elif typeName == "xmltag":
            return '<span class="xmltag">%s</span>' % value

        elif typeName == "xmlattr":
            return '<span class="xmlattr">%s</span>' % value

        elif typeName == "xmlattr_value":
            return '<span class="xmlattr_value">%s</span>' % value

        elif typeName == "xmlcdata":
            return '<span class="xmlcdata">%s</span>' % value

    def _fmtCode(self, title, contents, syntax):
        titleHtml = "<h2>%s</h2>" % title

        htmlLines = []

        for typeName, value in contents:
            if typeName is None or value is None or value == '':
                continue
            htmlCode = self._format_type(typeName, value, syntax)

            htmlLines.append(htmlCode)

        contentHtml = "".join(htmlLines)

        return "%s\n<pre><code>%s</code></pre>" % (titleHtml, contentHtml)

    def render(self, pageTitle):
        fmtCodes = []

        for title, content in self.codes.items():
            fmtCodes.append(self._fmtCode(title, content[0], content[1]))

        return __HTML_TPL__.replace("{?htmlCode?}", "".join(fmtCodes)).replace("{?title?}", pageTitle)

    def addParsedCode(self, codeTitle, parsedCodeContents, syntax):
        self.codes[codeTitle] = (parsedCodeContents, syntax)
