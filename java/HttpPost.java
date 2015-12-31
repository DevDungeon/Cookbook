import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class TestHttpPost {
  public static void main(String[] args)  throws Exception {
    URL remoteUrl = null;
    HttpURLConnection conn = null;
    BufferedReader in = null;
    String inputLine;

      remoteUrl = new URL("http://www.devdungeon.com/archive");

      conn = (HttpURLConnection)remoteUrl.openConnection();

      conn.setRequestMethod("POST");
      conn.setDoOutput(true);
      conn.setRequestProperty("User-Agent", "Not Java!?");    

      in = new BufferedReader(new InputStreamReader(conn.getInputStream()));

      while ((inputLine = in.readLine()) != null) {
        System.out.println(inputLine);
      }
        in.close();
  }
}