"""
Enable REST API by logging into admin portal (e.g. https://xmpp.devdungeon.com:9090) and go to `Plugins` and then `Available Plugins`. Enable the `REST API`.
Then go to `Server | Server Settings | REST API` and change it to `Enabled`.
Choose `Secret key auth` option and store that key.
"""
OPENFIRE_SECRET_KEY = 'asdfasdf234'
OPENFIRE_BASE_URL = 'https://xmpp.devdungeon.com:9091/plugins/restapi/v1'