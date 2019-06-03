#!/bin/bash
# -*- coding: utf-8 -*-


# this script would be executed by 4 parameters:
# 1..  the jenkins host's uri which include the port num and the request path(jenkins index web page path)
# 2..  the jenkins host's username
# 3..  the jenkins host's password
# 4..  the job name which you want to search


URI="${1}/job/${4}/api/json?pretty=true"
curl -X GET ${URI} --user ${2}:${3}