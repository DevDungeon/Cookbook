/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.httpexamples;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;

/**
 *
 * @author dtron
 */
public class DownloadFile {

    public static void main(String[] args) {
        download("http://www.devdungeon.com", "devdungeon.html");
    }

    private static void download(String url, String filepath) {
        HttpClient client = new DefaultHttpClient();

        HttpParams params = client.getParams();
        HttpConnectionParams.setConnectionTimeout(params, 1000 * 5);
        HttpConnectionParams.setSoTimeout(params, 1000 * 5);

        HttpGet request = new HttpGet(url);

        HttpResponse response = null;
        try {
            response = client.execute(request);
        } catch (IOException ex) {
            Logger.getLogger(HttpGetExample.class.getName()).log(Level.SEVERE, null, ex);
        }
        BufferedReader rd;
        String line = null;
        try {
            rd = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));
            FileWriter fileWriter = new FileWriter(filepath);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            while ((line = rd.readLine()) != null) {
                bufferedWriter.write(line);
                bufferedWriter.newLine();
            }
            bufferedWriter.close();

        } catch (IOException ex) {
            Logger.getLogger(HttpGetExample.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnsupportedOperationException ex) {
            Logger.getLogger(HttpGetExample.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
