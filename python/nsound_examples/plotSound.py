#!/usr/bin/python2

import nsound as ns

b = ns.Buffer()
b << 0 << 1 << 0.9 << 0.8 << 0.7 << 0.6 << 0.5 << 0.4 << 0.3 << 0.2 << 0.1 << 0
b.plot("Nsound")
ns.Plotter.show()
