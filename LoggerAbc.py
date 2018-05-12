import abc

class Logger(abc.ABC):
    def LogInfo(self, logMessage):
        pass

    def LogWarn(self, logMessage):
        pass

    def LogError(self, logMessage):
        pass

    def LogSecurity(self, logMessage):
        pass

    def LogCritical(self, logMessage):
        pass