#!/usr/bin/env python3

import requests
import json
from LogLevels import LogLevel
from LoggerAbc import Logger

class IFTTT_Logger(Logger):
    
    def __init__ (self, iftttMethod, iftttKey, logSource):
        self._iftttMethod_ = iftttMethod
        self._iftttKey_ = iftttKey
        self._logSource_ = logSource

    def _writeLog_(self, logLevel, logMessage):
        logUrl = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(self._iftttMethod_, self._iftttKey_)
        logText = {"value1" : self._logSource_, "value2" : logLevel.name, "value3" : logMessage}
        payload = json.dumps(logText)
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=logUrl, data=payload, headers=headers)
        print(r.content)
    
    def LogInfo(self, logMessage):
        self._writeLog_(LogLevel.INFO, logMessage)

    def LogWarn(self, logMessage):
        self._writeLog_(LogLevel.WARN, logMessage)

    def LogError(self, logMessage):
        self._writeLog_(LogLevel.ERROR, logMessage)

    def LogSecurity(self, logMessage):
        self._writeLog_(LogLevel.SECURITY, logMessage)

    def LogCritical(self, logMessage):
        self._writeLog_(LogLevel.CRITICAL, logMessage)
    