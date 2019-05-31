#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
jenkins_utils.py

we use the python-jenkins package as our utils file, this file would support some functions for our deploy.views file
"""

import configparser
from jenkins import Jenkins, JenkinsException
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
        """
        we define some fields like this:

            * name           the jenkins job name, one project's all jobs will be named by same
        """
        self.name = project.full_tag
        try:
            self.test_session = Jenkins(self._TEST_URI, self._TEST_USERNAME, self._TEST_PASSWORD)
            info("make the session with the test environment jenkins host: " + self._TEST_URI)
        except:
            warn("can not make the session with test environment jenkins host: " + self._TEST_URI)
            self.test_session = None
        try:
            self.prelease_session = Jenkins(self._PRELEASE_URI, self._PRELEASE_USERNAME, self._PRELEASE_PASSWORD)
            info("make the session with the pre-release environment jenkins host: " + self._PRELEASE_URI)
        except:
            warn("can not make the session with pre-release environment jenkins host: " + self._PRELEASE_URI)
            self.prelease_session = None
        try:
            self.gray_session = Jenkins(self._GRAY_URI, self._GRAY_USERNAME, self._GRAY_PASSWORD)
            info("make the session with the gray environment jenkins host: " + self._GRAY_URI)
        except:
            warn("can not make the session with gray environment jenkins host: " + self._GRAY_URI)
            self.gray_session = None
        try:
            self.prod_session = Jenkins(self._PROD_URI, self._PROD_USERNAME, self._PROD_PASSWORD)
            info("make the session with the production environment jenkins host: " + self._PROD_URI)
        except:
            warn("can not make the session with production environment jenkins host: " + self._PROD_URI)
            self.prod_session = None

    def get_info(self, env):
        """
        get the job information which has been constructed in env
        """
        if env == "test":
            try:
                info = self.test_session.get_job_info(self.name)
                return info
            except JenkinsException as error:
                eror("can not find the job " + self.name + " in the test environment jenkins host")
                return None
        elif env == "prelease":
            pass
        elif env == "gray":
            pass
        elif env == "prod":
            pass
        else:
            eror("parameter passing error, location to engineering.deploy_utils.Job.get_job_info")
            return None