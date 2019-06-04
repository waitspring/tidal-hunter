#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
deploy_utils.py

we use the python-jenkins package as our utils file, this file would support some functions for our deploy.views file

please attention that: the python-jenkins package can be used in the python language but not python3, we need to change
our choices in the CICD way

this is the jenkins office document say:"In Python 2.6 or later you can safely parse this output using
ast.literal_eval(urllib.urlopen("...").read())"
"""

import configparser
import subprocess
import json
from tidal.utils import *


# =====================================================================================================================
# classes for our job
# =====================================================================================================================
class Job:
    """
    a class with some methods from python-jenkins packages
    """
    file = configparser.ConfigParser()
    file.read("config")
    _TEST_URI          = file.get("jenkins configure", "TEST_JENKINS_URI")
    _TEST_USERNAME     = file.get("jenkins configure", "TEST_JENKINS_USERNAME")
    _TEST_PASSWORD     = file.get("jenkins configure", "TEST_JENKINS_PASSWORD")
    _PRELEASE_URI      = file.get("jenkins configure", "PRELEASE_JENKINS_URI")
    _PRELEASE_USERNAME = file.get("jenkins configure", "PRELEASE_JENKINS_USERNAME")
    _PRELEASE_PASSWORD = file.get("jenkins configure", "PRELEASE_JENKINS_PASSWORD")
    _GRAY_URI          = file.get("jenkins configure", "GRAY_JENKINS_URI")
    _GRAY_USERNAME     = file.get("jenkins configure", "GRAY_JENKINS_USERNAME")
    _GRAY_PASSWORD     = file.get("jenkins configure", "GRAY_JENKINS_PASSWORD")
    _PROD_URI          = file.get("jenkins configure", "PROD_JENKINS_URI")
    _PROD_USERNAME     = file.get("jenkins configure", "PROD_JENKINS_USERNAME")
    _PROD_PASSWORD     = file.get("jenkins configure", "PROD_JENKINS_PASSWORD")

    def __init__(self, project):
        self.name = project.full_tag

    def get_info(self, env):
        if env == "test":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._TEST_URI, self._TEST_USERNAME, self._TEST_PASSWORD, self.name
            )
        elif env == "prelease":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._PRELEASE_URI, self._PRELEASE_USERNAME, self._PRELEASE_PASSWORD, self.name
            )
        elif env == "gray":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._GRAY_URI, self._GRAY_USERNAME, self._GRAY_PASSWORD, self.name
            )
        elif env == "prod":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._PROD_URI, self._PROD_USERNAME, self._PROD_PASSWORD, self.name
            )
        else:
            eror("parameter passing error, location to engineering.deploy_utils.Job.get_job_info")
            return None
        try:
            info = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
            info = json.loads(info)
        except:
            warn("send the request into " + self.env + " jenkins host failure")
            info = None
        return info