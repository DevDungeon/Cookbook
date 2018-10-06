Running TomCat
==============

In Windows:

* Download and extract TomCat from https://tomcat.apache.org
* Move to the TomCat bin directory
* In PowerShell set the Java home environment variable

    $Env:JAVA_HOME="C:\opt\jdk-11-openjdk"

* Run TomCat using startup script

    .\startup.bat

* Default management portal is at http://localhost:8080/
* Create a new directory in tomcat\webapps. E.g. "mystuff"
* Put an index.html inside tomcat\webapps\mystuff
* Visit URL http://localhost:8080/mystuff


