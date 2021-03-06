#!/bin/bash
# -*- coding: utf-8 -*-

# this script would be executed by 4 parameters:
# 1..  the jenkins host's uri which include the port num and the request path(jenkins index web page path)
# 2..  the jenkins host's username
# 3..  the jenkins host's password
# 4..  the job name


# =====================================================================================================================
# define some functions for our script
# =====================================================================================================================
function info()
{
    echo -e "$(date +"%F %T") \E[32m[INFO] ${1} \E[0m"
}

function warn()
{
    echo -e "$(date +"%F %T") \E[33m[WARN] ${1} \E[0m"
}

function eror()
{
    echo -e "$(date +"%F %T") \E[31m[EROR] ${1} \E[0m"
}


# =====================================================================================================================
# make the request to jenkins rest-api
# =====================================================================================================================
URI="${1}/job/${4}/build"
CHECK=$(curl -I -X POST ${URI} --user ${2}:${3} | egrep "HTTP/1.1" | gwak '{ print ${2} }')

if [ ${CHECK} -eq 200 ]; then
    info "build the job ${4} successfully, please wait"
    info "script will exit with status 0"
    exit 0
else
    eror "build the job ${4} failure, please check"
    warn "script will exit with status 1"
    exit 1
fi
