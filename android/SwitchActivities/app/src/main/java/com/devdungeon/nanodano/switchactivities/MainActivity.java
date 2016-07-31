package com.devdungeon.nanodano.switchactivities;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.View;


public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void switchOnce(View v) {
        // This only changes the screen, it does not change to another activity
        setContentView(R.layout.activity_second);

    }
    public void switchBack(View view) {
        setContentView(R.layout.activity_main);
    }
}
