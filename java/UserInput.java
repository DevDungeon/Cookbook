//UserInput.java
import java.util.Scanner;

class UserInput {
	public static void main(String[] args) {
		String userInput = null;
		Scanner inputReader = new Scanner(System.in);
		System.out.printf("Please enter something: ");

		// Will read up to first space/word barrier
		userInput = inputReader.nextLine();
		// Other options are 
		// next() for words 
		// nextInt(), nextLong(), nextByte()
		// and the relative hasNext*() for each one

		System.out.println(userInput);
	}
}

