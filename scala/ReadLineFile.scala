import scala.io.Source

object ReadLineFile {
       def main(args: Array[String]) {
       	   // Files is args(0)
	   for (line <- Source.fromFile(args(0)).getLines()) {
	       println(line)
	   }
       }
}