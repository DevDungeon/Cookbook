object CmdArgs {
    def main(args: Array[String]) {

        // Args does not count the program name.
        println("First argument: " + args(0))
        println("All Command Line Arguments: " + args.toList)

    }
}
