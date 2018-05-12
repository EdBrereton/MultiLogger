WebLogger
===========
A python library for logging in various forms.

This library was originally developed to allow me to easily use IFTTT to log data from a raspberry pi in a location that was easily accessible. It kinda grew from there, and is now a fairly flexible framework for logging. It allows you to log locally in various formats, as well as using IFTTT. It is highly likely that other logging methods will follow...

Usage
-----
There are 2 main ways this library can be used at present. Instrumentation logging, which makes use of decorators to indicate method entry and exits, and simple logging. Usage Examples are shown below

Simple Logging
-------------
```python
import multilogger

logger = MultiLogger.IFTTT_Logger("weblog", "XXXXXXXXXXXXX", "Example Logs")
logger.LogInfo("This is an info level log")
logger.LogWarn("This is a warning level log")
logger.LogError("This is an error level log")
logger.LogCritical("This is a critical level log")
logger.LogSecurity("This is a security level log")
```

Instrumentation Logging
-----------------------
```python
import MultiLogger

MultiLogger.Instrumentation.SetLogSource("Ogga Booga")
MultiLogger.Instrumentation.SetLoggerActive(True)

@MultiLogger.Instrumentation.debug_log
def TestMethod():
    print("Test print")

TestMethod()
```

