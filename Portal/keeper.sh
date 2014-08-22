#!/bin/sh
workdir="/opt/portal/Portal"
cd ${workdir}
while true;do
  svn up ${workdir}
  youngest=`svn st -v ${workdir}|grep -v "Portal/"|awk '{print $1}'`
  if [ -f ${workdir}/lastbkrev ];then
    lastrev=`cat ${workdir}/lastbkrev`
    if [ ${lastrev} -ne ${youngest} ];then
      ps -ef|grep "manage.py"|grep "bin"|grep 8080|grep -v grep|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
      nohup python manage.py runserver 0.0.0.0:8080 >> mynohup.out 2>&1 &
    fi
  fi
  echo ${youngest} > ${workdir}/lastbkrev
  sleep 10s
done
