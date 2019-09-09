import logging

# Goes to stderr by default

logging.basicConfig(level=logging.WARNING, format="%(msg)s")

if options.verbose:
	logging.getLogger().setLevel(logging.DEBUG)

if stderr.isatty():  # Stderr going to terminal not a file
	# Update formatting to include color
	# or do the reverse and use colorama.strip() to remove colors
	pass


LOG = logging.getLogger(__name__)

LOG.debug('only gets output if verbose mode is on')
LOG.info('normal log message')
LOG.warning('warn')
LOG.error('full on error!')




# How to get it to go to file?
# Email?
# Slack webhook/Discord webhook
# How to format with better datetime information


# Adding colors if it's going to a console versus a file?
# Determine if in/out is a a screen or being piped to/from a file
# stdin.isatty()
# stderr.isatty()
# stdout.isatty()