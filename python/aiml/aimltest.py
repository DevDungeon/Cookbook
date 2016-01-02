import aiml
#pyaiml

k = aiml.Kernel()

k.learn("std-startup.xml")
k.respond("load aiml b")

while True: print k.respond(raw_input("> "))


"""
import aiml
import os.path

k = aiml.Kernel()
if os.path.isfile("standard.brn"):
    k.bootstrap(brainFile = "standard.brn")
else:
    k.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    k.saveBrain("standard.brn")
"""
