/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.httpexamples;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class HttpPostExample {

    public static void main(String[] args) throws Exception {
        post("http://www.devdungeon.com/archive");
    }
    
    private static void post(String url) {
        try {
            URL remoteUrl = null;
            try {
                remoteUrl = new URL(url);
            } catch (MalformedURLException ex) {
                Logger.getLogger(HttpPostExample.class.getName()).log(Level.SEVERE, null, ex);
            }
            HttpURLConnection conn = null;
            BufferedReader in = null;
            String inputLine;
            
            conn = (HttpURLConnection) remoteUrl.openConnection();
            conn.setRequestMethod("POST");
            conn.setDoOutput(true);
            conn.setRequestProperty("User-Agent", "Not Java!?");
            
            in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            while ((inputLine = in.readLine()) != null) {
                System.out.println(inputLine);
            }
            in.close();
        } catch (IOException ex) {
            Logger.getLogger(HttpPostExample.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
