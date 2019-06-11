# -*- coding: utf-8 -*-

"""
tidal.utils.py file will support some little tools for us
"""

import time


# =====================================================================================================================
# some logging functions
# =====================================================================================================================
def info(string):
    """
    output logging string with the [INFO] label
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(timestamp, "\033[32m[INFO]", string, "\033[0m")

def warn(string):
    """
    output logging string with the [WARN] label
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(timestamp, "\033[33m[WARN]", string, "\033[0m")

def eror(string):
    """
    output logging string with the [EROR] label
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(timestamp, "\033[31m[EROR]", string, "\033[0m")