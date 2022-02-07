# Autorun app on startup in Debian desktop

Place desktop entries that you want to run automatically on login to `~/.config/autostart/`.

For example, a `conky.desktop` file:

```ini
[Desktop Entry]
Type=Application
Exec=/usr/bin/conky
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=conky
Comment=
```
