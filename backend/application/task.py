# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         task
# Description:  
# Author:       CHEN
# Date:         2022/5/13
# -------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task
from requests.exceptions import ConnectionError, ConnectTimeout


@shared_task
def get_url(url,timeout=3):
    try:
        code=requests.get(url).status_code
        return code
    except (ConnectionError,ConnectTimeout) as e:
        return 404
