/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.simplejson;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

/**
 *
 * @author dtron
 */
public class DecodeJson {
    public static void main(String[] args) {

		try {
			String jsonData = getJsonFromUrl("http://www.reddit.com/r/houston.json");

			JSONParser jsonParser = new JSONParser();
			JSONObject jsonObject = (JSONObject) jsonParser.parse(jsonData); // The whole JSON value

            //System.out.println(jsonObject);
            JSONObject data = (JSONObject)jsonObject.get("data"); // The data object
            //System.out.println(data); 

            JSONArray children = (JSONArray)data.get("children"); // All children
            
            // for each child in children
            // get child("data")
            for (int i = 0; i < children.size(); i++) {
                JSONObject child = (JSONObject)children.get(i);
                //System.out.println(child); // The whole post object
                
                JSONObject childData = (JSONObject)child.get("data");
                System.out.print(childData.get("title") + ": ");
                System.out.println(childData.get("url"));
            }
            
		} catch (ParseException ex) {
			ex.printStackTrace();
		} catch (NullPointerException ex) {
			ex.printStackTrace();
		}

	}
    
    public static String getJsonFromUrl(String url) {
        HttpClient httpclient = new DefaultHttpClient();
        HttpGet httpget = new HttpGet(url); 
        httpget.setHeader("User-Agent", "Java Reddit Test Client 0.0.1");
        ResponseHandler<String> responseHandler = new BasicResponseHandler();
        String responseBody = null;
        try {
            responseBody = httpclient.execute(httpget, responseHandler);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        httpclient.getConnectionManager().shutdown();
        return responseBody;
    }
}
