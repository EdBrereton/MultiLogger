from functools import wraps
from StdOut_Logger import StdOut_Logger

class Instrumentation(object):
        
    __LogSource = "DEBUG"
    __Logger = None
    __LoggerActive = True

    @classmethod
    def SetLogSource(cls, logSource):
        cls.__LogSource = logSource

    @classmethod
    def SetLogger(cls, logger):
        cls.__Logger = logger

    @classmethod
    def SetLoggerActive(cls, toggle):
        cls.__LoggerActive = toggle

    @classmethod
    def debug_log(cls, function_to_log):
        if(cls.__LoggerActive != True):
            return function_to_log
        else:
            @wraps(function_to_log)
            def wrapper():
                    if(cls.__Logger == None):
                        cls.SetLogger(StdOut_Logger(cls.__LogSource))

                    entering = "Entering {0}".format(function_to_log)
                    exiting = "Exiting {0}".format(function_to_log)
                    cls.__Logger.LogInfo(entering)
                    function_to_log()
                    cls.__Logger.LogInfo(exiting)
                
            return wrapper
