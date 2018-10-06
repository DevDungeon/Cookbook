import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

public class GetScreenResolution {
    public static void main(String[] args) {
        GraphicsEnvironment g = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice[] devices = g.getScreenDevices();

        for (int i = 0; i < devices.length; i++) {
            System.out.println("Width:" + devices[i].getDisplayMode().getWidth());
            System.out.println("Height:" + devices[i].getDisplayMode().getHeight());
        } 
    }
    
}
