#!/bin/sh
exec scala "$0" "$@"
!#

# Scripted Hello world that prints out command arguments

object HelloWorld {
  def main(args: Array[String]) {
    println("Hello, world! " + args.toList)
  }
}
HelloWorld.main(args)
