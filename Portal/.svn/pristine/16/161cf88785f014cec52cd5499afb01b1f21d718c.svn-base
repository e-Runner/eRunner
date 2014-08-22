#!/bin/sh
ps -ef|grep "keeper.sh"|grep -v grep|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps -ef|grep "manage.py"|grep "bin"|grep 8080|grep -v grep|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1