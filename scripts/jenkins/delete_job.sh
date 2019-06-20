#!/bin/bash
# -*- coding: utf-8 -*-

# this script would be executed by 4 parameters:
# 1..  the jenkins host's uri which include the port num and the request path(jenkins index web page path)
# 2..  the jenkins host's username
# 3..  the jenkins host's password
# 4..  the job name which you want to delete
# 5..  the remote sync host user, this user need sudo auth without entering password
# 6..  the remote sync host ip address


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
if [ ${#} -ne 6 ]; then
    eror "parameters number error, please check the calling command"
    warn "script exit with status 1"
    exit 1
fi

# remove the sync directory to store the build result
ssh -A ${5}@${6} "rm -rf /data/code_deploy/${4}"
if [ ${?} -ne 0 ]; then
    eror "can not remove the remote sync directory in ${6} by user ${5}"
    warn "script exit with status 2"
    exit 2
else
    info "remove the remote sync directory successfully in ${6} by user ${5}"
fi

URI="${1}/job/${4}/doDelete"
curl -X POST ${URI} --user ${2}:${3}