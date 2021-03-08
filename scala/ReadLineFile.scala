import scala.io.Source

object ReadLineFile {
    def main(args: Array[String]) {

        // Loop through each line in the file
        for (line <- Source.fromFile("test.txt").getLines()) {
            // Do something with line
            println(line)
        }

    }
}
