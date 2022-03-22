#include <gst/gst.h>
#include <stdio.h>
#include <unistd.h>

/*

Shows how to play a stream. Whether it's an audio file,
video, local file, file over HTTP, CD or DVD
*/

/*
apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

*/

// gcc main.c `pkg-config --cflags --libs gstreamer-1.0`

// https://gstreamer.freedesktop.org/documentation/playback/playbin.html?gi-language=c


int main(int argc, char *argv[]) {
    GstElement *pipeline;
    GstBus *bus;
    GstMessage *msg;

    gst_init(&argc, &argv);



    char cwd[PATH_MAX];
	if (getcwd(cwd, sizeof(cwd)) != NULL) {
		printf("Current directory: %s\n", cwd);	
	} else {
		puts("Could not determine current directory. Assuming /");
		return 1;
	}
	
	// Build the gst-launch string
	char command[PATH_MAX] = "";
	strcat(command, "playbin uri=file://");
	strcat(command, cwd);
	//strcat(command, "/sound.wav");
	strcat(command, "/sintel_trailer-480p.webm");
	printf("Pipeline: %s\n", command);
	
	// This will create a WINDOW if it's a video or just play to speakers if audio only!!!
	// uri could be http:// source or file:// like file:////path/to/vid.webm
	pipeline = gst_parse_launch(command, NULL);
	// playbin uri=file:///home/dano/sound.wav
	// playbin uri=https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm
	// playbin uri=file:///home/dano/sintel_trailer-480p.webm
    // playbin uri=cdda:///4    // Track 4 on cd
    // playbin uri=dvd://       // DVD playback



    // Start playing
    puts("Telling pipeline to play");
    gst_element_set_state(pipeline, GST_STATE_PLAYING);


    // Wait until error or end of stream
    puts("Getting bus from pipeline to get event messages");
    bus = gst_element_get_bus(pipeline);
    msg = gst_bus_timed_pop_filtered(bus, GST_CLOCK_TIME_NONE,
                                     GST_MESSAGE_ERROR | GST_MESSAGE_EOS);
    if (GST_MESSAGE_TYPE(msg) == GST_MESSAGE_ERROR) {
    	// If it's a video and the window is closed early, will trigger error
        g_error("Uh oh... received error message. error occurred during streaming!");
    }

    puts("Freeing up allocations.");
    gst_message_unref(msg);
    gst_object_unref(bus);
    gst_element_set_state(pipeline, GST_STATE_NULL);
    gst_object_unref(pipeline);

    return 0;

}
