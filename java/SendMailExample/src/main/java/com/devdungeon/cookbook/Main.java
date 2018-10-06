package com.devdungeon.cookbook;

import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.commons.mail.DefaultAuthenticator;
import org.apache.commons.mail.Email;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;
import org.apache.commons.mail.SimpleEmail;

public class Main {
    // http://commons.apache.org/proper/commons-email/userguide.html

    static String password = "";

    public static void main(String[] args) {
        try {
            sendSimpleTextMail();
        } catch (EmailException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public static void sendSimpleTextMail() throws EmailException {
        Email email = new SimpleEmail();
        email.setHostName("mail.devdungeon.com");
        email.setSmtpPort(465); // SSL port 465
        email.setAuthenticator(new DefaultAuthenticator("nanodano@devdungeon.com", password));
        email.setSSLOnConnect(true);
        email.setFrom("nanodano@devdungeon.com");
        email.setSubject("Test mail, please ignore");
        email.setMsg("Hello, world!");
        email.addTo("nanodano@devdungeon.com");
        
        // When using a secured transport (STARTTLS or SSL) you can force validating the server's certificate by calling
        //Email.setSSLCheckServerIdentity(true);
        // Enforce using STARTTLS by calling 
        //Email.setStartTLSRequired(true);
        
        // Change where bounce emails go
        //email.setBounceAddress(emailAddressString);
        
        email.setDebug(true); // Print extra details to System.out
        
        email.send();
    }

//    public static void sendMailWithAttachment() throws EmailException {
//        EmailAttachment attachment = new EmailAttachment();
//        attachment.setPath("mypictures/john.jpg");
//        // Can also attach a remote url and it will be downloaded on send
//        //attachment.setURL(new URL("http://www.apache.org/images/asf_logo_wide.gif"));
//        attachment.setDisposition(EmailAttachment.ATTACHMENT);
//        attachment.setDescription("Picture of John");
//        attachment.setName("John");
//
//        MultiPartEmail email = new MultiPartEmail();
//        email.setHostName("mail.myserver.com");
//        email.addTo("jdoe@somewhere.org", "John Doe");
//        email.setFrom("me@apache.org", "Me");
//        email.setSubject("The picture");
//        email.setMsg("Here is the picture you wanted");
//
//        email.attach(attachment); // Attach as many as needed
//            
//        email.setDebug(true); // Print extra details to System.out
//        
//        email.send();
//    }
//
//    public static void sendHtmlEmail() {
//        // Create the email message
//        HtmlEmail email = new HtmlEmail();
//        email.setHostName("mail.myserver.com");
//        email.addTo("jdoe@somewhere.org", "John Doe");
//        email.setFrom("me@apache.org", "Me");
//        email.setSubject("Test email with inline image");
//
//        // embed the image and get the content id
//        URL url = new URL("http://www.apache.org/images/asf_logo_wide.gif");
//        String cid = email.embed(url, "Apache logo");
//
//        // set the html message
//        email.setHtmlMsg("<html>The apache logo - <img src=\"cid:" + cid + "\"></html>");
//
//        // set the alternative message
//        email.setTextMsg("Your email client does not support HTML messages");
//
//        // send the email
//        
//        email.send();
//    }
//
//    public static void sendHtmlEmailWithEmbeddedImage() {
//        // load your HTML email template
//        String htmlEmailTemplate = ".... <img src=\"http://www.apache.org/images/feather.gif\"> ....";
//
//        // define you base URL to resolve relative resource locations
//        URL url = new URL("http://www.apache.org");
//
//        // create the email message
//        ImageHtmlEmail email = new ImageHtmlEmail();
//        email.setDataSourceResolver(new DataSourceUrlResolver(url));
//        email.setHostName("mail.myserver.com");
//        email.addTo("jdoe@somewhere.org", "John Doe");
//        email.setFrom("me@apache.org", "Me");
//        email.setSubject("Test email with inline image");
//
//        // set the html message
//        email.setHtmlMsg(htmlEmailTemplate);
//
//        // set the alternative message
//        email.setTextMsg("Your email client does not support HTML messages");
//
//        // send the email
//        email.send();
//    }

}
