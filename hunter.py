#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from django.core.management import execute_from_command_line


# =====================================================================================================================
# execute part
# =====================================================================================================================
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tidal.settings")
    execute_from_command_line(sys.argv)