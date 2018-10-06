// GetPass.java
import java.io.Console;

class GetPass
{
	public static void main(String[] args)
	{
		Console console = System.console();
		char[] pass = console.readPassword("Enter the secret password: ");
		System.out.println("You could print the password, if you wanted...");
		// System.out.println(pass);
	}
}