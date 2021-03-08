import java.io._

object WriteFile {
   def main(args: Array[String]) {
      val writer = new PrintWriter(new File("output.txt" ))
      writer.write("Hello, world!")
      writer.close()
   }
}
