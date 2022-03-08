/*
[GLib](https://docs.gtk.org/glib/)

gcc main.c `pkg-config --cflags --libs gobject-2.0`

# To build GLib from source
# https://docs.gtk.org/glib/
# https://download.gnome.org/sources/
# https://download.gnome.org/sources/glib/2.71/glib-2.71.2.tar.xz

# Extract and run:

```bash
# pip install meson; apt install ninja
meson setup builddir
meson compile -c builddir
meson install -c builddir
```
*/
#include <glib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
	printf("==\nExample using GLib to encode/decode UTF-8 strings.\n==\n");

	// Store a UTF-8 string literal
	guchar* input = "⮂⮂⮂⮂⮂⮂";
	printf("Input string: %s\n", input);

	// To get the "actual" number of characters (6)
	// use g_utf8_strlen()
	glong len = g_utf8_strlen (input, -1);
	printf("Number of characters: %d\n", len);
	
	// Get the number of raw bytes the UTF-8 string contains.
	int raw_len = strlen(input);
	printf("Number of raw bytes: %d\n", raw_len);

	// Encode string to Base64
	gchar* encoded_text = g_base64_encode(input, raw_len);
	printf("encoded_text: %s\n", encoded_text);

	// Decode base64 to string
	gsize decoded_text_length;
	guchar* text = g_base64_decode(encoded_text, &decoded_text_length);
	printf("Decoded text: %s\n", text);
	printf("Decoded text length returned: %d\n", decoded_text_length);

	return 0;
}
