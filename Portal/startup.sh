#!/bin/sh
cd /opt/portal/Portal
ps -ef|grep "manage.py"|grep "bin"|grep 8080|grep -v grep|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
nohup python manage.py runserver 0.0.0.0:8080 >mynohup.out 2>&1 &
nohup sh /opt/portal/Portal/keeper.sh >/dev/null 2>&1 &
