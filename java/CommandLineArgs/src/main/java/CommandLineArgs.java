// Compile with
// javac CommandLineArgs.java

// Run with
// java CommandLineArgs arg1 arg2

// Or if using a jar
// javac CommandLineArgs.java
// jar cf CommandLineArgs.jar CommandLineArgs.class

// Edit the manifest file in the archive to have
// Main-Class: CommandLineArgs

// Then run with
// java -jar CommandLineArgs.jar arg1 arg2
class CommandLineArgs {
	public static void main(String args[]) {
		System.out.println(args);
		for (String arg : args) {
			System.out.println(arg);
		}
	}
}