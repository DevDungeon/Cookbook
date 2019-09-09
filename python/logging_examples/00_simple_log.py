import logging

logging.basicConfig(level=logging.DEBUG)

print("This goes to STDOUT and logging goes to STDERR")
# Try running with


# Default log level is WARNING
logging.debug('This is a debug log')
logging.info('This is an informational log')
logging.warning('This is a warn log')
logging.error('This is a error log')
logging.critical('This is a critical log')