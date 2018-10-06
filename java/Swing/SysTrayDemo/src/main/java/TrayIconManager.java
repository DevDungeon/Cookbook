import javax.swing.*;
import java.awt.*;
import java.net.URL;


class TrayIconManager {


    private final TrayIcon trayIcon = new TrayIcon(createImage("/devdungeon64x64.png", "tray icon"));
    private final SystemTray tray = SystemTray.getSystemTray();
    private final PopupMenu rightClickPopupMenu = new PopupMenu();


    TrayIconManager() {
        if (!SystemTray.isSupported()) {
            System.out.println("SystemTray is not supported. Exiting.");
            System.exit(1);
        }
        setupActions();
        SwingUtilities.invokeLater(this::display);
    }


    private void setupActions() {
        // Double click action on system tray icon
        trayIcon.addActionListener(e -> JOptionPane.showMessageDialog(
                null,
                "This dialog box is run from System Tray")
        );

        // Right click menu on system tray icon
        MenuItem aboutItem = new MenuItem("About");
        MenuItem exitItem = new MenuItem("Exit");
        rightClickPopupMenu.add(aboutItem);
        rightClickPopupMenu.add(exitItem);
        aboutItem.addActionListener(e -> JOptionPane.showMessageDialog(
                null,
                "This dialog box is run from the About menu item")
        );
        exitItem.addActionListener(e -> {
            tray.remove(trayIcon);
            System.exit(0);
        });
        trayIcon.setPopupMenu(rightClickPopupMenu);
    }


    private void display() {
        trayIcon.setImageAutoSize(true);
        try {
            tray.add(trayIcon);
        } catch (AWTException e) {
            System.out.println("TrayIcon could not be added.");
            System.exit(1);
        }
    }


    private static Image createImage(String path, String description) {
        URL imageURL = TrayIconManager.class.getResource(path);

        if (imageURL == null) {
            System.err.println("Resource not found: " + path);
            return null;
        } else {
            return (new ImageIcon(imageURL, description)).getImage();
        }
    }


    public void notify(String title, String message) {
        trayIcon.displayMessage(title, message, TrayIcon.MessageType.NONE);
    }


}
