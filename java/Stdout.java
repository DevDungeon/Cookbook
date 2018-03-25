// Stdout.java

class Stdout
{
	public static void main(String[] args)
	{
		System.out.print("Hello, "); // No newline at end
		System.out.println("World!"); // With newline at end

		// Formatted string. Avoids lots of + signs. %x is lower hex
		System.out.printf("Int: %d - String: %s - UpperHex: %X", 23, "Test", 42);
	}
}