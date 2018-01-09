package com.devdungeon.workingwithfiles;

import android.content.Context;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Android operating system root /system. Contains app/ with all the apks and bin/
        System.out.println("Android OS root dir: " + Environment.getRootDirectory().getAbsolutePath());
        // External storage /sdcard just means external to application, not always a removable SD card
        System.out.println("Device external storage dir: " + Environment.getExternalStorageDirectory().getAbsolutePath());
        System.out.println("Device data directory dir: " + Environment.getDataDirectory().getAbsolutePath());

        // Variables
        String FILENAME = "hello_file.txt";
        String string = "hello world! again.";

        ////////////////////////////////////////////////////////////////////////////////
        // Write a file to the internal private application storage
        ////////////////////////////////////////////////////////////////////////////////
        // By default, files saved to the internal storage are private to your application and other applications cannot
        // access them (nor can the user). When the user uninstalls your application, these files are removed.
        File file = new File(this.getFilesDir(), FILENAME);
        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            assert fos != null;
            fos.write(string.getBytes());
            fos.close();
            System.out.println("Closed file.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        ////////////////////////////////////////////////////////////////////////////////
        // List all files in the app's private storage dir
        ////////////////////////////////////////////////////////////////////////////////

        System.out.println("this.getFilesDir() dir: " + this.getFilesDir());
// List the files in /system/app (rootdir)
        // List the files in /system/bin


        ////////////////////////////////////////////////////////////////////////////////
        // Read a file from the application's private storage
        ////////////////////////////////////////////////////////////////////////////////
        try {
            FileInputStream fis = this.openFileInput(FILENAME);
            byte[] buff = new byte[65535];
            int bytesRead = fis.read(buff);
            System.out.println("Read " + bytesRead + " bytes from " + FILENAME);
            // for each byte in buffer
            System.out.println("Data ====");
            System.out.println(new String(buff, "UTF-8"));
            System.out.println("====");
            System.out.println("====");
            fis.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }


        // Cache dir
        //        Saving cache files
        //        If you'd like to cache some data, rather than store it persistently, you should use getCacheDir() to open a File that represents the internal directory where your application should save temporary cache files.
        //        When the device is low on internal storage space, Android may delete these cache files to recover space. However, you should not rely on the system to clean up these files for you. You should always maintain the cache files yourself and stay within a reasonable limit of space consumed, such as 1MB. When the user uninstalls your application, these files are removed
        //
        //                // other metods
        //        getFilesDir()
        //        Gets the absolute path to the filesystem directory where your internal files are saved.
        //        getDir()
        //        Creates (or opens an existing) directory within your internal storage space.
        //        deleteFile()
        //        Deletes a file saved on the internal storage.
        //        fileList()
        //        Returns an array of files currently saved by your application

        // List files in a dirs like Documents and Downloads


        // External storage


    }
}
