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



---
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
---