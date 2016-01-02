package com.devdungeon.jsonexample;

import java.io.StringWriter;
import org.json.JSONObject;

/**
 *
 * @author nanodano@devdungeon.com
 */
public class Main {
    
    public static void main(String[] args) {
        Main.dataToJsonObject();
        Main.jsonObjectToString();
        Main.jsonStringToObject();
    }
    
    public static void dataToJsonObject() {
        System.out.println("Running JSON example.");
        
        JSONObject obj = new JSONObject();

        obj.put("name", "foo");
        obj.put("num", new Integer(100));
        obj.put("balance", new Double(1000.21));
        obj.put("is_vip", new Boolean(true));

        System.out.println(obj.toString());
    }
    
    
    public static void jsonObjectToString() {
	
        JSONObject obj = new JSONObject();

        obj.put("name","foo");
        obj.put("num",new Integer(100));
        obj.put("balance",new Double(1000.21));
        obj.put("is_vip",new Boolean(true));

        StringWriter out = new StringWriter();
        obj.write(out);

        String jsonText = out.toString();
        System.out.println(jsonText);
    }
    
    public static void jsonStringToObject() {
        // String to JSON object
        String jsonString = "{\"stat\": { \"sdr\": \"aa:bb:cc:dd:ee:ff\", \"rcv\": \"aa:bb:cc:dd:ee:ff\", \"time\": \"UTC in millis\", \"type\": 1, \"subt\": 1, \"argv\": [{\"type\": 1, \"val\":\"stackoverflow\"}]}}";
        JSONObject jsonObject = new JSONObject(jsonString);
        
        // Get a sub element of the JSON object
        JSONObject newJSON = jsonObject.getJSONObject("stat");
        System.out.println(newJSON.toString());
        
        // Clone new json object and replace original json object with the copy
        jsonObject = new JSONObject(newJSON.toString());
        // Access sub element as a string
        System.out.println(jsonObject.getString("rcv"));
        
        // Access sub element as JSON array
        System.out.println(jsonObject.getJSONArray("argv"));
    }
    

}
