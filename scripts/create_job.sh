#!/bin/bash
# -*- coding: utf-8 -*-


# this script would be executed by 4 parameters:
# 1..  the jenkins host's uri which include the port num and the request path(jenkins index web page path)
# 2..  the jenkins host's username
# 3..  the jenkins host's password
# 4..  the new job name
# 5..  the remote sync host ip address
# 6..  the remote sync host user, this user need sudo auth without entering password


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
# check the parameters number
if [ ${#} -ne 6 ]; then
    eror "parameters number error, please check the calling command"
    warn "script exit with status 1"
    exit 1
fi

# make the sync directory to store the build result
ssh -A ${5}@${6} "mkdir -p /data/code_deploy/${4}"
if [ ${?} -ne 0 ]; then
    eror "can not make the remote sync directory in ${6} by user ${5}"
    warn "script exit with status 2"
    exit 2
else
    info "make the remote sync directory successfully in ${6} by user ${5}"
fi

# call jenkins rest api to build the job
URI="${1}/createItem?name=${4}"
cd scripts && curl -X POST -d @config.xml -H "Content-Type:text/xml" "${URI}" --user ${2}:${3}

# delete the config.xml
rm -f config.xml