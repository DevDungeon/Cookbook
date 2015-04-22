#!/usr/bin/env python

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

### Protocol Implementation

# This is just about the simplest possible protocol
class NanoBot(Protocol):
    def dataReceived(self, data):
        """
        As soon as any data is received, write it back.
        """
        self.transport.write(data)
        # process incoming data

def main():
    f = Factory()
    f.protocol = NanoBot
    reactor.listenTCP(8000, f)
    reactor.run()

if __name__ == '__main__':
    main()
