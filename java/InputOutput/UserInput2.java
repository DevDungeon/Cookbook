import java.util.Scanner;

class UserInput2
{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter your name: ");
		System.out.println("Hello, " + scanner.nextLine());

        //Scanner scanner2 = new Scanner(System.in);
		System.out.print("Enter an integer: ");
		System.out.println("Your number plus 1 is: " + (scanner.nextInt() + 1));		
	}	
}