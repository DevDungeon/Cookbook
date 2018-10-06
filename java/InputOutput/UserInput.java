import java.util.Scanner;

class UserInput
{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter your name: ");
		System.out.println("Hello, " + scanner.nextLine());

		System.out.print("Enter an integer: ");
		System.out.println("Your number plus 1 is: " + (scanner.nextInt() + 1));		
	}	
}