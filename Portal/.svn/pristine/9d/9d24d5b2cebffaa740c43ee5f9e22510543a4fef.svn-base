# -*- encoding: utf-8 -*-
__author__ = 'Wang Shuhao'


def GetSyntax():
    syntax = {}
    keyword = ['add', 'all', 'alter', 'and', 'any', 'as', 'asc', 'authorization', 'avg', 'backup', 'begin', 'between',
               'break', 'browse', 'bulk', 'by', 'cascade', 'case', 'check', 'checkpoint', 'close', 'clustered',
               'coalesce', 'commit', 'committed', 'contains', 'containstable', 'continue', 'convert', 'count', 'create',
               'cross', 'current', 'current_date', 'current_time', 'current_timestamp', 'current_user', 'cursor',
               'database', 'dbcc', 'deallocate', 'declare', 'default', 'delete', 'deny', 'desc', 'disk', 'distinct',
               'distributed', 'double', 'drop', 'dump', 'else', 'end', 'escape', 'exec', 'exists', 'exit', 'fetch',
               'file', 'fillactor', 'floppy', 'for', 'foreach', 'foreign', 'freetext', 'freetexttable', 'from', 'full',
               'goto', 'grant', 'group', 'having', 'holdlock', 'identity', 'identity_insert', 'identitycol', 'if', 'in',
               'index', 'inner', 'insert', 'intersect', 'into', 'is', 'isolation', 'join', 'key', 'kill', 'left',
               'level', 'like', 'load', 'max', 'min', 'national', 'nocheck', 'nonclustered', 'not', 'null', 'nullif',
               'of', 'off', 'offsets', 'on', 'only', 'open', 'openquery', 'openrowset', 'option', 'or', 'order',
               'outer', 'percent', 'pipe', 'plan', 'prepare', 'primary', 'print', 'privileges', 'procdure', 'proc',
               'public', 'raiseerror', 'read', 'readtext', 'reconfigure', 'references', 'repeatable', 'replication',
               'restore', 'return', 'revoke', 'right', 'rollback', 'rowcount', 'rowguidcol', 'rule', 'save', 'schema',
               'select', 'serializable', 'session_user', 'set', 'setuser', 'shutdown', 'some', 'statistics', 'sum',
               'system_user', 'table', 'tape', 'temporary', 'temp', 'then', 'to', 'top', 'transaction', 'tran',
               'trigger', 'uncommitted', 'union', 'unique', 'update', 'updatetext', 'use', 'values', 'varying', 'view',
               'waitfor', 'when', 'where', 'while', 'with', 'work', 'writetext', 'call']

    comment = ["--"]
    string_decl = ['\'', '\"']
    operator = ['+', '-', '*', '/', '%', '>', '<', '=', '!', '&', '|', '~', '^', '']
    separator = [' ', '\t', '(', ')', '[', ']', '{', '}', ',', '#', ';']
    conflict = {
        "-": {
            "expect": "-",
            "expect_state": "comment",
            "unexpect_state": "operator"
        }
    }

    syntax["keyword"] = set(keyword)
    syntax["comment"] = set(comment)
    syntax["var"] = r""
    syntax["string"] = set(string_decl)
    syntax["number"] = r"[+|-]{0,1}\d+\.{0,1}\d+[f|u|F|U|l|L]{0,1}"
    syntax["operator"] = set(operator)
    syntax["separator"] = set(separator)
    syntax["matchcase"] = False
    syntax["conflict"] = conflict

    return syntax
