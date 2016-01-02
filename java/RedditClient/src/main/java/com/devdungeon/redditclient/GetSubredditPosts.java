package com.devdungeon.redditclient;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.json.JSONObject;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;

/**
 *
 * @author nanodano@devdungeon.com
 */
public class GetSubredditPosts {
    
    public static void main(String[] args) throws Exception {
        String responseJson = null;
        responseJson = GetSubredditPosts.getJson("http://www.reddit.com/r/houston.json");

        JSONObject response = new JSONObject(responseJson);

        // Get a sub element of the JSON object
        String responseType = response.getString("kind");
        
        if (!responseType.equals("Listing")) {
            throw new Exception("Error: Expected a \"Listing\" response type.");
        }

        JSONObject data = response.getJSONObject("data");        
        
        // Get the children (the posts)
        JSONArray children = data.getJSONArray("children");
        
        // Print out data for each post
        for (int i = 0; i < children.length(); i++) {
            JSONObject child = children.getJSONObject(i);
            JSONObject childData = child.getJSONObject("data");
            System.out.println(childData);
            System.out.println(childData.get("title") + ": " + childData.get("url"));        
        }
    }
    
    public static String getJson(String url) {
        HttpClient httpclient = new DefaultHttpClient();
        HttpGet httpget = new HttpGet(url); 
        httpget.setHeader("User-Agent", "Java Reddit Test Client 0.0.1");
        ResponseHandler<String> responseHandler = new BasicResponseHandler();
        String responseBody = null;
        try {
            responseBody = httpclient.execute(httpget, responseHandler);
        } catch (IOException ex) {
            Logger.getLogger(GetSubredditPosts.class.getName()).log(Level.SEVERE, null, ex);
        }
        httpclient.getConnectionManager().shutdown();
        return responseBody;
    }
    
}
