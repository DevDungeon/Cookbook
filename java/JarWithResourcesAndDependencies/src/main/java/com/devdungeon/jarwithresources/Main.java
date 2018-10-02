// This example shows how to include resources like images in with the jar file
// The resources must be places in <projectRoot>/src/main/resources
// And update pom.xml to use the Maven jar plugin
// Then resources can be accessed with getClass().getResource("x.txt") relative
// to the resources directory.
package com.devdungeon.jarwithresources;

import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;

/**
 *
 * @author nanodano@devdungeon.com
 */
public class Main {
    public static void main(String[] args) {
        try {
            // Instead of Main.class you can use getClass() when non-static
            // Root resource directory is src/main/resources
            URL resourceUrl = Main.class.getResource("/devdungeon120x120.png");
            BufferedImage background = ImageIO.read(resource);
            System.out.println(background.getData());
        } catch (IOException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }  
    }
    
}
