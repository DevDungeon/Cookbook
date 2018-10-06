import java.io.OutputStream;
import java.io.InputStream;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Properties;

class PropertiesExample {
    public static void main(String[] args) {
        generatePropertiesFile();
        loadPropertiesFile();
    }

    private static void generatePropertiesFile() {
        Properties properties = new Properties();  
        properties.setProperty("key", "value");
        
        OutputStream output = null;
        try {
            output = new FileOutputStream("sample.properties");
        } catch (FileNotFoundException ex) {
            System.err.println(ex.getMessage());
            System.exit(1);
        }

        try {
            // store() Takes OutputStream or Writer
            properties.store(output, "Comments.\nMultiple lines allowed.");
            // or storeToXML
        } catch (IOException ex) {
            System.err.println(ex.getMessage());
        }
    }

    private static void loadPropertiesFile() {
        // Alternatively, to load a file from the jar src/main/resources directory
        // InputStream in = getClass().getResourceAsStream("/file.txt"); // Non-static
        InputStream in = null;
        try {
            in = new FileInputStream("sample.properties");
        } catch (FileNotFoundException ex) {
            System.err.println(ex.getMessage());
            System.exit(1);
        }

        Properties properties = new Properties();
        try {
            properties.load(in);
            // or loadFromXML
        } catch (IOException ex) {
            System.err.println(ex.getMessage());
            System.exit(1);
        }
        
        System.out.println(properties.get("key"));
        System.out.println(properties.getOrDefault("absentKey", "defaultValue"));
    }

}