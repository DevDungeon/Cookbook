package com.devdungeon.diskspacechecker;

import android.os.Environment;
import android.os.StatFs;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        System.out.println(Environment.DIRECTORY_ALARMS);
        System.out.println(Environment.DIRECTORY_DCIM);
        System.out.println(Environment.DIRECTORY_DOCUMENTS);
        System.out.println(Environment.DIRECTORY_DOWNLOADS);
        System.out.println(Environment.DIRECTORY_MOVIES);
        System.out.println(Environment.DIRECTORY_MUSIC);
        System.out.println(Environment.DIRECTORY_NOTIFICATIONS);
        System.out.println(Environment.DIRECTORY_PICTURES);
        System.out.println(Environment.DIRECTORY_PODCASTS);
        System.out.println(Environment.DIRECTORY_RINGTONES);

        String state = Environment.getExternalStorageState();
        boolean mExternalStorageAvailable = false;
        boolean mExternalStorageWriteable = false;
        if (Environment.MEDIA_MOUNTED.equals(state)) {
            System.out.println("External media mounted. Read + write available.");
        } else if (Environment.MEDIA_MOUNTED_READ_ONLY.equals(state)) {
            System.out.println("External media mounted but read only.");
        } else {
            System.out.println("Can neither read nor write external storage.");
        }

        System.out.println("==================================");
        System.out.println("Root directory: " + Environment.getRootDirectory().getAbsolutePath());
        System.out.println("Data directory: " + Environment.getDataDirectory().getAbsolutePath());
        System.out.println("Download cache directory: " + Environment.getDownloadCacheDirectory().getAbsolutePath());
        System.out.println("External storage directory: " + Environment.getExternalStorageDirectory().getAbsolutePath());
        System.out.println("External storage state: " + Environment.getExternalStorageState());
        //System.out.println("Is external storage emulated: " + Environment.isExternalStorageEmulated()); // Requires too high api version
        //System.out.println("Is external storage emulated: " + Environment.isExternalStorageRemovable());
        System.out.println("==================================");

        // Free internal space
        StatFs stat = new StatFs(Environment.getDataDirectory().getPath());
        long bytesAvailable = (long) stat.getFreeBlocks() * (long) stat.getBlockSize();
        long megAvailable = bytesAvailable / 1048576;
        System.out.println("Free internal space");
        System.out.println(bytesAvailable + " b");
        System.out.println(megAvailable + " Mb");

        // Total internal space
        stat = new StatFs(Environment.getDataDirectory().getPath());
        bytesAvailable = (long) stat.getBlockSize() * (long) stat.getBlockCount();
        megAvailable = bytesAvailable / 1048576;
        System.out.println("Total internal space");
        System.out.println(bytesAvailable + " b");
        System.out.println(megAvailable + " Mb");

        // External storage free space        Calculate  Available External Storage memory
        stat = new StatFs(Environment.getExternalStorageDirectory().getPath());
        bytesAvailable = (long) stat.getFreeBlocks() * (long) stat.getBlockSize();
        megAvailable = bytesAvailable / 1048576;
        System.out.println("External storage free space");
        System.out.println(bytesAvailable + " b");
        System.out.println(megAvailable + " Mb");

        // External storage total space
        stat = new StatFs(Environment.getExternalStorageDirectory().getPath());
        bytesAvailable = (long) stat.getBlockSize() * (long) stat.getBlockCount();
        megAvailable = bytesAvailable / 1048576;
        System.out.println("External storage total space");
        System.out.println(bytesAvailable + " b");
        System.out.println(megAvailable + " Mb");

        System.out.println("==================================");
    }
}
