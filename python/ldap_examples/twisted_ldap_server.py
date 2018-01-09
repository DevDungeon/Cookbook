from twisted.internet import reactor, defer
from ldaptor.protocols.ldap import ldapclient, ldapsyntax, ldapconnector


@defer.inlineCallbacks
def example():
    serverip = '192.168.128.21'
    basedn = 'dc=example,dc=com'
    binddn = 'bjensen@example.com'
    bindpw = 'secret'
    query = '(cn=Babs*)'
    c = ldapconnector.LDAPClientCreator(reactor, ldapclient.LDAPClient)
    overrides = {basedn: (serverip, 389)}
    client = yield c.connect(basedn, overrides=overrides)
    yield client.bind(binddn, bindpw)
    o = ldapsyntax.LDAPEntry(client, basedn)
    results = yield o.search(filterText=query)
    for entry in results:
        print(entry)


if __name__ == '__main__':
    df = example()
    df.addErrback(lambda err: err.printTraceback())
    df.addCallback(lambda _: reactor.stop())
    reactor.run()
