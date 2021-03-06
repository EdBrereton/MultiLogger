#!/usr/bin/env python3
from LogLevels import LogLevel
from LoggerAbc import Logger
import datetime

class Text_Logger(Logger):
    
    def __init__ (self,logLocation, logSource):
        self._logLocation_ = logLocation
        self._logSource_ = logSource


    def _writeLog_(self, logLevel, logMessage):
        logLine = "[{0}] : {1} - {2} - {3}\n".format(self._logSource_, datetime.datetime.now(), logLevel.name, logMessage)
        logFile = open(self._logLocation_, 'a')
        logFile.write(logLine)
        logFile.close()
    
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
    