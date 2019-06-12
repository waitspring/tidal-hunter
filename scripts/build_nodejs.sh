#!/bin/bash
# -*- coding: utf-8 -*-

# this script is a standard file for jenkins execute action, if your jenkins host has installed the jenkins like:
#     * /opt/jenkins
# you could mv this file into /opt/jenkins/cicd/ and rewrite the template_nodejs.xml file
# this script would be executed by 1 parameter:
# 1..  the nodejs project name, and this parameter need to pass by the job's xml configure file


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
# build nodejs part
# =====================================================================================================================
# make sure the sync directory has been made
ssh <USERNAME>@<SYNC_ADDR> "rm -rf <SYNC_DIR>/${1}/*"

cd <JENKINS_DIR>/workspace/${1}
sudo npm install -g @zbj/utopia-cli
sudo npm install -verbose
sudo npm run build-prod

info "************************************************************************"
info "nodejs has been built successfully"
info "************************************************************************"

sudo tar -czf ${1}.tgz *
scp ${1}.tgz <USERNAME>@<SYNC_ADDR>:<SYNC_DIR>/${1}
sudo rm -f ${1}.tgz

info "************************************************************************"
info "nodejs .tgz package has been send into remote sync host successfully"
info "************************************************************************"