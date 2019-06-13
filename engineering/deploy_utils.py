# -*- coding: utf-8 -*-

"""
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

    _TEST_JENKINS_URI          = file.get("jenkins configure", "TEST_JENKINS_URI")
    _TEST_JENKINS_USERNAME     = file.get("jenkins configure", "TEST_JENKINS_USERNAME")
    _TEST_JENKINS_PASSWORD     = file.get("jenkins configure", "TEST_JENKINS_PASSWORD")
    _PRELEASE_JENKINS_URI      = file.get("jenkins configure", "PRELEASE_JENKINS_URI")
    _PRELEASE_JENKINS_USERNAME = file.get("jenkins configure", "PRELEASE_JENKINS_USERNAME")
    _PRELEASE_JENKINS_PASSWORD = file.get("jenkins configure", "PRELEASE_JENKINS_PASSWORD")
    _GRAY_JENKINS_URI          = file.get("jenkins configure", "GRAY_JENKINS_URI")
    _GRAY_JENKINS_USERNAME     = file.get("jenkins configure", "GRAY_JENKINS_USERNAME")
    _GRAY_JENKINS_PASSWORD     = file.get("jenkins configure", "GRAY_JENKINS_PASSWORD")
    _PROD_JENKINS_URI          = file.get("jenkins configure", "PROD_JENKINS_URI")
    _PROD_JENKINS_USERNAME     = file.get("jenkins configure", "PROD_JENKINS_USERNAME")
    _PROD_JENKINS_PASSWORD     = file.get("jenkins configure", "PROD_JENKINS_PASSWORD")

    _TEST_SYNC_ADDR            = file.get("sync configure", "TEST_SYNC_ADDR")
    _TEST_SYNC_USERNAME        = file.get("sync configure", "TEST_SYNC_USERNAME")
    _PRELEASE_SYNC_ADDR        = file.get("sync configure", "PRELEASE_SYNC_ADDR")
    _PRELEASE_SYNC_USERNAME    = file.get("sync configure", "PRELEASE_SYNC_USERNAME")
    _GRAY_SYNC_ADDR            = file.get("sync configure", "GRAY_SYNC_ADDR")
    _GRAY_SYNC_USERNAME        = file.get("sync configure", "GRAY_SYNC_USERNAME")
    _PROD_SYNC_ADDR            = file.get("sync configure", "PROD_SYNC_ADDR")
    _PROD_SYNC_USERNAME        = file.get("sync configure", "PROD_SYNC_USERNAME")

    def __init__(self, project):
        self.name = project.full_tag
        self.description = project.description
        self.git_source = project.git_source
        self.arch = project.arch

    def get_info(self, env):
        if env == "test":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._TEST_JENKINS_URI, self._TEST_JENKINS_USERNAME, self._TEST_JENKINS_PASSWORD, self.name
            )
        elif env == "prelease":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._PRELEASE_JENKINS_URI, self._PRELEASE_JENKINS_USERNAME, self._PRELEASE_JENKINS_PASSWORD, self.name
            )
        elif env == "gray":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._GRAY_JENKINS_URI, self._GRAY_JENKINS_USERNAME, self._GRAY_JENKINS_PASSWORD, self.name
            )
        elif env == "prod":
            command = "bash scripts/get_job_info.sh %s %s %s %s" % (
                self._PROD_JENKINS_URI, self._PROD_JENKINS_USERNAME, self._PROD_JENKINS_PASSWORD, self.name
            )
        else:
            eror("parameter passing error, location to engineering.deploy_utils.Job.get_info")
            return None
        try:
            data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
            data = json.loads(data)
        except:
            warn("send the request into " + env + " jenkins host failure")
            data = None
        return data

    def create_job(self, env):
        if env == "test":
            if self.arch == "dubbo":
                # =====================================================================================================
                # create the dubbo job in the test environment
                # =====================================================================================================
                with open("scripts/template_dubbo.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", "./" + self.name)
                    config = config.replace("POINT_4", "target/*.war")
                    config = config.replace("POINT_5", "target")
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            elif self.arch == "nodejs":
                # =====================================================================================================
                # create the nodejs job in the test environment
                # =====================================================================================================
                with open("scripts/template_nodejs.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", self.name)
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            else:
                warn("project architecture error, location to engineering.deploy_utils.Job.create_job")
                return None
            command = "bash scripts/create_job.sh %s %s %s %s %s %s" % (
                self._TEST_JENKINS_URI,
                self._TEST_JENKINS_USERNAME,
                self._TEST_JENKINS_PASSWORD,
                self.name,
                self._TEST_SYNC_USERNAME,
                self._TEST_SYNC_ADDR
            )
        elif env == "prelease":
            if self.arch == "dubbo":
                # =====================================================================================================
                # create the dubbo job in the pre-release environment
                # =====================================================================================================
                with open("scripts/template_dubbo.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", "./" + self.name)
                    config = config.replace("POINT_4", "target/*.war")
                    config = config.replace("POINT_5", "target")
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            elif self.arch == "nodejs":
                # =====================================================================================================
                # create the nodejs job in the pre-release environment
                # =====================================================================================================
                with open("scripts/template_nodejs.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", self.name)
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            else:
                warn("project architecture error, location to engineering.deploy_utils.Job.create_job")
                return None
            command = "bash scripts/create_job.sh %s %s %s %s %s %s" % (
                self._PRELEASE_JENKINS_URI,
                self._PROD_JENKINS_USERNAME,
                self._PROD_JENKINS_PASSWORD,
                self.name,
                self._PRELEASE_SYNC_USERNAME,
                self._PRELEASE_SYNC_ADDR
            )
        elif env == "gray":
            if self.arch == "dubbo":
                # =====================================================================================================
                # create the dubbo job in the gray environment
                # =====================================================================================================
                with open("scripts/template_dubbo.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", "./" + self.name)
                    config = config.replace("POINT_4", "target/*.war")
                    config = config.replace("POINT_5", "target")
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            elif self.arch == "nodejs":
                # =====================================================================================================
                # create the nodejs job in the gray environment
                # =====================================================================================================
                with open("scripts/template_nodejs.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", self.name)
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            else:
                warn("project architecture error, location to engineering.deploy_utils.Job.create_job")
                return None
            command = "bash scripts/create_job.sh %s %s %s %s %s %s" % (
                self._GRAY_JENKINS_URI,
                self._GRAY_JENKINS_USERNAME,
                self._GRAY_JENKINS_PASSWORD,
                self.name,
                self._GRAY_SYNC_USERNAME,
                self._GRAY_SYNC_ADDR
            )
        elif env == "prod":
            if self.arch == "dubbo":
                # =====================================================================================================
                # create the dubbo job in the prod environment
                # =====================================================================================================
                with open("scripts/template_dubbo.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", "./" + self.name)
                    config = config.replace("POINT_4", "target/*.war")
                    config = config.replace("POINT_5", "target")
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            elif self.arch == "nodejs":
                # =====================================================================================================
                # create the nodejs job in the prod environment
                # =====================================================================================================
                with open("scripts/template_nodejs.xml", 'r') as config:
                    config = config.read()
                    config = config.replace("POINT_1", self.description)
                    config = config.replace("POINT_2", self.git_source)
                    config = config.replace("POINT_3", self.name)
                with open("scripts/config.xml", 'w') as output:
                    output.write(config)
                    info("write the config.xml successfully for " + self.name)
            else:
                warn("project architecture error, location to engineering.deploy_utils.Job.create_job")
                return None
            command = "bash scripts/create_job.sh %s %s %s %s %s %s" % (
                self._PROD_JENKINS_URI,
                self._PROD_JENKINS_USERNAME,
                self._PROD_JENKINS_PASSWORD,
                self.name,
                self._PROD_SYNC_USERNAME,
                self._PROD_SYNC_ADDR
            )
        else:
            eror("parameter passing error, location to engineering.deploy_utils.Job.create_job")
            return None
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()

    def build_job(self, env):
        if env == "test":
            command = "bash scripts/build_job.sh %s %s %s %s" % (
                self._TEST_JENKINS_URI, self._TEST_JENKINS_USERNAME, self._TEST_JENKINS_PASSWORD, self.name
            )
        elif env == "prelease":
            command = "bash scripts/build_job.sh %s %s %s %s" % (
                self._PRELEASE_JENKINS_URI, self._PRELEASE_JENKINS_USERNAME, self._PRELEASE_JENKINS_PASSWORD, self.name
            )
        elif env == "gray":
            command = "bash scripts/build_job.sh %s %s %s %s" % (
                self._GRAY_JENKINS_URI, self._GRAY_JENKINS_USERNAME, self._GRAY_JENKINS_PASSWORD, self.name
            )
        elif env == "prod":
            command = "bash scripts/build_job.sh %s %s %s %s" % (
                self._PROD_JENKINS_URI, self._PROD_JENKINS_USERNAME, self._PROD_JENKINS_PASSWORD, self.name
            )
        else:
            warn("project architecture error, location to engineering.deploy_utils.Job.build_job")
            return None
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()