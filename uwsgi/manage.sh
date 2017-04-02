#!/bin/bash

cd `dirname $0`/..

action=${1:-help}

config_file=uwsgi/config.ini

function getConf()
{
    key=$1
    grep $config_file -e "^ *$key *=" | sed -e 's/^[^=]*= *//'
}

pidfile=`getConf pidfile`
PID=
if [ -e $pidfile ]; then
    content=`cat $pidfile`
    if ps --pid "$content" &>/dev/null; then
        PID=$content
    fi
fi

function log()
{
    echo "[`basename $0`][`date '+%Y-%m-%d %H:%M:%S'`]" $*
}

case $action in 
    start)
        if [ -z "$PID" ]; then
            log 'start uwsgi in background...'
            uwsgi $config_file
        else
            log "uwsgi is already running, pid = $PID"
        fi
        ;;
    reload)
        if [ "$PID" ]; then
            log try to reload uwsgi...
            uwsgi --reload $pidfile
        else
            log uwsgi is not running.
            log 'start uwsgi in background...'
            uwsgi $config_file
        fi
        ;;
    stop)
        if [ "$PID" ]; then
            log try to stop uwsgi...
            uwsgi --stop $pidfile
        else
            log uwsgi is not running.
        fi
        ;;
    status)
        if [ "$PID" ]; then
            log 'uwsgi is running, pid =' $PID
            kill -SIGUSR1 $PID
        else
            log uwsgi is not running.
        fi
        ;;
    *)
        echo "Usage: %s <start|reload|stop|status|help>"
esac
