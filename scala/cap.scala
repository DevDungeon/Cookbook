import scala.io.Source

object cap {
       def main(args: Array[String]) {
       	   // Files is args(0)
	   for (line <- Source.fromFile(args(0)).getLines()) {
	       val words = line.split(" ")
	       words.foreach {
	         _ = "x"
		 print
	       
	       }
	       println()
	       

	   }
       }
}