# -*- encoding: utf-8 -*-
__author__ = 'Wang Shuhao'


def GetSyntax():
    syntax = {}

    keyword = ['require', 'our', 'my', 'use', 'BEGIN', 'END',
               '__DATA__', '__END__', 'DATA', 'if', 'else', 'elsif',
               '__FILE__', '__LINE__', '__PACKAGE__', 'and', 'cmp',
               'continue', 'CORE', 'do', 'eq', 'exp', 'for', 'foreach',
               'ge', 'gt', 'le', 'lock', 'lt', 'm', 'ne', 'no', 'or',
               'package', 'q', 'qq', 'qr', 'qw', 'qx', 's', 'sub',
               'tr', 'unless', 'until', 'while', 'xor', 'y',
               'print', 'exit', 'die', 'time', 'open', 'close', 'localtime',
               'return', 'local']

    string_decl = ['\"', '\'']
    var = r"[\$|@].*"
    number = r"[+|-]{0,1}\d+\.{0,1}\d+[f|u|F|U|l|L]{0,1}"
    operator = ['+', '-', '*', '/', '=', '(', ')', ':']
    seperator = [',', ' ', '\t', '{', '}', ';']
    comment = ["#"]
    conflict = {}

    syntax["keyword"] = set(keyword)
    syntax["var"] = var
    syntax["string"] = set(string_decl)
    syntax["number"] = number
    syntax["operator"] = set(operator)
    syntax["separator"] = set(seperator)
    syntax["comment"] = set(comment)
    syntax["matchcase"] = True
    syntax["conflict"] = conflict


    return syntax