Java Servlet Basics
===================

Learn how to create servlets to create REST APIs and web apps with database access and front end templating.

Overview
--------
* Intro

diff between servlet and jsp?

* First servlet - Hello world
comments

* How to package / creating a war
* Deploying a webapp/servlet
* Using maven to start a new webapp project
* How to serve static files
* logging?
sessions?
system.out vs out.print
* Handling get vs post
* XML/JSON request/responses
* setting mime type and streaming a large binary file back?
* incorporating database access
* internationalization (http://www.ntu.edu.sg/home/ehchua/programming/java/JavaServletExamples.html)
* JSP/templating/ 
How to add middleware to Servlets (e.g. analytics, auth, logging)







Intro
-----
Servlets are core part of java web applications
To run servlets you will need a servlet container, like TomCat.

Check out ---- [TomCat Basics] --- for how to install TomCat. There are other options, like Glassfish, JBoss, Wildfly, and more.



diff between servlet and jsp
----------------------
((( Link to JSP tutorial )))
a JSP file is like a PHP script and is a standalone file that can contains html with java code interjected for pre-processing
JSP are very simple since you can just drop them in any directory inside a webapp and you can access the url directly. Tomcat already knows
how to process the jsp and run the java code and how to map the URL to the JSP

Servlets are code only, plain java files. TomCat needs a little more help than it does with JSP files because it needs to know what URL should
map to the Java class. It needs what is called a deployment descriptor, the web.xml file. The deployment descriptor maps URL patterns to
servlet classes for processing.

jsp are built on top of servlet technology and are convenient for single standalone files that require no special configuration or url mapping

directory structure
-------------------

Inside a web app directory /opt/tomcat9/webapps/mywebapp/
    
    # Deployment desciptor that maps URLs to servlet classes
    WEB-INF/web.xml

    # compiled classes go in WEB-INF/classes. 
    WEB-INF/classes

    ????source files don't even have to be in the web dir at all, ? just need classes
    ??if you put src files in WEB-INF/src will it recompile automatically by tomcat?

????? Then that just sits in the webapp dir? this is the unpacked format?


hello world servlet source code
-------------------------------

    // http://www.ntu.edu.sg/home/ehchua/programming/java/JavaServletExamples.html
    // To save as "<CATALINA_HOME>\webapps\helloservlet\WEB-INF\src\mypkg\HelloWorldExample.java"
    package mypkg;
    
    import java.io.*;
    import java.util.*;
    import javax.servlet.*;
    import javax.servlet.http.*;
    
    public class HelloWorldExample extends HttpServlet {
    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
                throws IOException, ServletException {
        // Set the response message's MIME type.
        response.setContentType("text/html;charset=UTF-8");
        // Allocate a output writer to write the response message into the network socket.
        PrintWriter out = response.getWriter();
    
        // Use a ResourceBundle for localized string in "LocalStrings_xx.properties" for i18n.
        // The request.getLocale() sets the locale based on the "Accept-Language" request header.
        ResourceBundle rb = ResourceBundle.getBundle("LocalStrings", request.getLocale());
        // To test other locales.
        //ResourceBundle rb = ResourceBundle.getBundle("LocalStrings", new Locale("fr"));
    
        // Write the response message, in an HTML document.
        try {
            out.println("<!DOCTYPE html>");  // HTML 5
            out.println("<html><head>");
            out.println("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>");
            String title = rb.getString("helloworld.title");
            out.println("<title>" + title + "</title></head>");
            out.println("<body>");
            out.println("<h1>" + title + "</h1>");  // Prints "Hello, world!"
            // Set a hyperlink image to refresh this page
            out.println("<a href='" + request.getRequestURI() + "'><img src='images/return.gif'></a>");
            out.println("</body></html>");
        } finally {
            out.close();  // Always close the output writer
        }
    }
    }




How to package / creating a war
-------------------------------
* Without maven?
* With maven
* packed vs unpacked

Deploying a webapp/servlet
--------------------------
* without maven (cli)
* with maven
* using tomcat manager app
put the app in the webapps dir of tomcat
Check out ---- TomCat Basics --- for how to install TomCat and deploy apps.


------USING MAVEN to make things easier

In the previous sections we covered how to create the directory structure for a web app, how to map URLs to servlet classes web.xml deployment descriptor, where to put your source code files, and where to put the compiled classes. We can use Maven to make all of these steps throughout the project lifecycle are a little easier. Maven can generate the directory structure for a new webapp project, take care of compiling and packaging the app in to a .war file, and even handle the deployment of the app to a TomCat server (local or remote).


Using maven archetype to start a new webapp project
----------------------------------------

using archetype (benefits: easier packaging, dependecny managment, deployment)


Using maven to compile


Using maven to package a .war file


Using maven to deploy
* locally
* remotely





How to serve static files
-------------------------
you just drop them in the webapp dir somewhere?
Can you use web.xml to map a /static dir to / ?


Logging
-------

Handling get vs post
--------------------

JSON request/responses
----------------------

setting mime type and streaming a large binary file back?
---------------------------------------------------------

incorporating database access
-----------------------------

JSP/templating
--------------

JSF?
-----
















Creating a basic servlet
========================

* Using Maven archetypes:

    # Interactive
    mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp

    # Non-interactive
    mvn archetype:generate -DgroupId=com.devdungeon \
                       -DartifactId=helloservlet \
                       -Dversion=1.0-SNAPSHOT \
                       -DarchetypeArtifactId=maven-archetype-webapp \
                       -DinteractiveMode=false


* Packaging

    # Run package to get a .war file
    mvn package


* Or manually create a new directory structure

    HelloServlet\
        web\
            WEB-INF\
                web.xml
            index.jsp

* Basic web.xml example:

    <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
            version="4.0">
    </web-app>

* Example of index.jsp

    <%--
        Comments
    --%>
    <%@ page contentType="text/html;charset=UTF-8" language="java" %>
    <html>
    <head>
        <title>$Title$</title>
    </head>
    <body>
    $END$
    </body>
    </html>




<!-- Tags: Java, TomCat, Linux, sysadmin, JSP, Servlet -->