import logging
from constants import log


def setup_log_to_file(log_level, log_format_string, fileoutput):
  """
  Given the log level, and the log format of the log, along with the 
  output logfile location Creates a logging.Logger with the correct 
  properties.
  """
  formatter = logging.Formatter(log_format_string)

  handler = logging.FileHandler(fileoutput)
  handler.setFormatter(formatter)
  log.addHandler(handler)
  log.setLevel(log_level)


def setup_log_to_console(log_level, log_format_string):
  """
  Given the log_level, and the string format of the log,
  Adds a handler to the global log with the correct properties
  """
  formatter = logging.Formatter(log_format_string)
  
  handler = logging.StreamHandler()
  handler.setFormatter(formatter)
  log.addHandler(handler)
  log.setLevel(log_level)


def log_test():
  log.debug("Debug level!")
  log.warning("Warning level!")
  log.error("Error level!")

