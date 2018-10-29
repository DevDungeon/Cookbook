package com.devdungeon.nanodano.text2speech;

import android.app.Activity;
import android.speech.tts.TextToSpeech;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;

import java.util.Locale;

/**
 * http://www.androidhive.info/2012/01/android-text-to-speech-tutorial/
 */
public class MainActivity extends Activity implements TextToSpeech.OnInitListener {

    private TextToSpeech tts;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tts = new TextToSpeech(this, this);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onInit(int status) {

        if (status == TextToSpeech.SUCCESS) {

            int result = tts.setLanguage(Locale.US);

            // Change language
            //tts.setLanguage(Locale.CHINESE); // Chinese language

            // Change pitch - 1.0 is default
            //tts.setPitch(0.7);

            // Change speed rate
            //tts.setSpeechRate(2);


            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            } else {
                speakOut();
            }

        } else {
            Log.e("TTS", "Initilization Failed!");
        }

    }


    private void speakOut() {
        String text = "Hello world";
        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null);
    }

}
