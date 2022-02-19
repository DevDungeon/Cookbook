import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;

// Run with:
// javac PortScan.java
// java PortScan www.example.com
class PortScan {

    private static void printUsage() {
        System.out.println("Usage:");
        System.out.println("  java PortScan <host>");
        System.out.println("Examples:");
        System.out.println("  java PortScan 127.0.0.1");
        System.out.println("  java PortScan www.devdungeon.com");
    }

    private static void checkPort(String host, int portNumber) {
        Thread thread = new Thread(() -> {
            Socket clientSocket = new Socket();
            try {
                clientSocket.connect(new InetSocketAddress(host, portNumber), 3000);
                System.out.printf("[+] %d connected\n", portNumber);
                clientSocket.close();
            } catch (IOException e) {
                //System.out.printf("[-] Could not connect %d", portNumber);
                //e.printStackTrace();
            }
        });
        thread.start();
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("No arguments received.");
            printUsage();
            System.exit(1);
        }

        String host = args[0];
        System.out.println(args);
        System.out.println(host);
        System.out.printf("Scanning %s now...\n", host);

        for (Integer portNumber = 1; portNumber <= 65535; portNumber++) {
            checkPort(host, portNumber);
        }

    }
}