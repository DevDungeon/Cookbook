package com.devdungeon.contactlist;
import android.content.ContentResolver;
import android.database.Cursor;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });


        ArrayList<String> names = getContactNames();//{"Johnny", "Bill", "Ted"};
        // it needs THIS(a the activity, which is a view), the layout to use for each list item, and the text field that should be populated, and the array string
        ArrayAdapter<String> contactAdapter = new ArrayAdapter<String>(this, R.layout.single_list_item, R.id.textView, names);
        ListView listView = (ListView) findViewById(R.id.contactList);
        listView.setAdapter(contactAdapter);


    }

    public ArrayList<String> getContactNames() {
        ContentResolver cr = getContentResolver();
        Cursor cur = cr.query(ContactsContract.Contacts.CONTENT_URI,
                null, null, null, null);
        ArrayList<String> contactStrings = new ArrayList<String>();
        if (cur.getCount() > 0) {
            while (cur.moveToNext()) {
                // Process each contact found

                String id = cur.getString(
                        cur.getColumnIndex(ContactsContract.Contacts._ID));
                String name = cur.getString(cur.getColumnIndex(
                        ContactsContract.Contacts.DISPLAY_NAME));
                String contactString = id + " - " + name;

                if (cur.getInt(cur.getColumnIndex(ContactsContract.Contacts.HAS_PHONE_NUMBER)) > 0) {
                    Cursor pCur = cr.query( // Phone number cursor
                            ContactsContract.CommonDataKinds.Phone.CONTENT_URI,
                            null,
                            ContactsContract.CommonDataKinds.Phone.CONTACT_ID +" = ?",
                            new String[]{id}, null);
                    while (pCur.moveToNext()) {
                        String phoneNo = pCur.getString(pCur.getColumnIndex(
                                ContactsContract.CommonDataKinds.Phone.NUMBER));
                        contactString += " | " + phoneNo;
                    }
                    pCur.close();
                }

                contactStrings.add(contactString);
            }
        }
        return contactStrings;
    }

}
