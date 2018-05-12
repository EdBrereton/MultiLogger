#!/usr/bin/env python3

import requests
import json
from LogLevels import LogLevel

class Weblogger(object):
    
    def __init__ (self, iftttMethod, iftttKey, logSource):
        self._iftttMethod_ = iftttMethod
        self._iftttKey_ = iftttKey
        self._logSource_ = logSource

    def WriteLog(self, logLevel, logMessage):
        logUrl = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(self._iftttMethod_, self._iftttKey_)
        logText = {"value1" : self._logSource_, "value2" : logLevel, "value3" : logMessage}
        logData = json.dumps(logText)

        requests.post(url=logUrl, json=logData)
    
    