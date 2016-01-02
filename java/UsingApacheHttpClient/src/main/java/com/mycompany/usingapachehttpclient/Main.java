package com.mycompany.usingapachehttpclient;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;

// Perform HTTP requests
public class Main {
    
    public static void main(String[] args) throws Exception {        
        HttpClient client = new DefaultHttpClient();
        
        HttpParams params = client.getParams();
        HttpConnectionParams.setConnectionTimeout(params, 1000 * 5);
        HttpConnectionParams.setSoTimeout(params, 1000 * 5);

        HttpGet request = new HttpGet("http://localhost:9998");

        HttpResponse response = client.execute(request);
        BufferedReader rd = new BufferedReader (new InputStreamReader(response.getEntity().getContent()));
        String line = "";
        while ((line = rd.readLine()) != null) {
            System.out.println(line);
        }
    }
   
}
