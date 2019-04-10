# https://www.youtube.com/watch?v=CJ7-SroGtZ8
# Mark Smith - Writing Awesome Command-Line Programs in Python
from ConfigParser import SafeConfigParser
from os.path import dirname, join, expanduser

INSTALL_DIR = dirname(__file__)

config = SafeConfigParser()

# Load all config files, overriding any values found in subsequent loads
config.read([
    join(INSTALL_DIR, 'defaults.ini'),  # First load all defaults
    expanduser('~/.tool.ini'),          # Second load any user specific settings
    'config.ini'                        # Last, load and set/override any local configs in current running dir
])
