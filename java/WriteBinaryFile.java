// https://www.caveofprogramming.com/java/java-file-reading-and-writing-files-in-java.html
import java.io.*;

public class WriteBinaryFile {
    public static void main(String [] args) {
        String fileName = "test.txt";

        try {
            // Put some bytes in a buffer so we can
            // write them. Usually this would be
            // image data or something. Or it might
            // be unicode text.
            String bytes = "Hello theren";
            byte[] buffer = bytes.getBytes();

            FileOutputStream outputStream =
                new FileOutputStream(fileName);

            // write() writes as many bytes from the buffer
            // as the length of the buffer. You can also
            // use
            // write(buffer, offset, length)
            // if you want to write a specific number of
            // bytes, or only part of the buffer.
            outputStream.write(buffer);

            // Always close files.
            outputStream.close();       

            System.out.println("Wrote " + buffer.length + 
                " bytes");
        }
        catch(IOException ex) {
            System.out.println(
                "Error writing file '"
                + fileName + "'");
        }
    }
}