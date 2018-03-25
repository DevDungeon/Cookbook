// ReadLines.java
import java.util.Scanner;

class ReadLines
{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
	
		// Read and print out each line.
		while (scanner.hasNextLine()) {
			String lineOfInput = scanner.nextLine();
			System.out.println(lineOfInput);
		}
	}
}       a