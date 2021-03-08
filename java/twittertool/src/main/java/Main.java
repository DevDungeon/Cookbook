import twitter4j.*;
import twitter4j.auth.AccessToken;
import twitter4j.auth.RequestToken;

import java.awt.*;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws TwitterException, MalformedURLException, AWTException, InterruptedException {


        TrayIconManager trayIconManager = new TrayIconManager();
        trayIconManager.notify("New Tweets", "test\nTest\ntest");

        Twitter twitter = new TwitterFactory().getInstance();

/*
        // Login code to get accessToken and accessTokenSecret
        RequestToken requestToken = twitter.getOAuthRequestToken();
        System.out.println("Please visit this URL: " +
        requestToken.getAuthenticationURL());
        Scanner scanner = new Scanner(System.in);
        String pin = scanner.nextLine();
        AccessToken accessToken = twitter.getOAuthAccessToken(requestToken, pin);
        System.out.println(accessToken.getScreenName());
        System.out.println(accessToken.getToken());
        System.out.println(accessToken.getTokenSecret());
*/

        // Print Twitter screen name
//        System.out.println(twitter.getScreenName());

        // Post a tweet
//        twitter.updateStatus("Test tweet!");

        // # TODO Create a list of queries to monitor
        Query query = new Query();
        query.setQuery("#news");
        List<Long> knownTweetIds = new ArrayList<>();

        while (true) {
            // Get latest tweets
            List<Status> latestTweets = twitter.search(query).getTweets();
            // Determine which tweets are new
            List<Status> newTweets = latestTweets.stream()
                    .filter(tweet -> !knownTweetIds.contains(tweet.getId()))
                    .collect(Collectors.toList());

            // If there are new tweets, save them, and notify
            if (newTweets.size() > 0) {
                // Store new tweets
                for (Status tweet : newTweets) {
                    knownTweetIds.add(tweet.getId());
                    printTweet(tweet);
                }
                // TODO update w/ accurate info
                trayIconManager.notify("New tweets!", "#golang: 5\n #java: 3");
            }

//            Thread.sleep(15 * 60 * 1000); // 15 minutes
            Thread.sleep(5000); // 15 minutes
        }


    }

    private static void printTweet(Status tweet) {
        System.out.println(tweet.getUser().getScreenName() + ": " + tweet.getText());
    }

}
