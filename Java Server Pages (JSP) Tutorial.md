Java Server Pages (JSP) Tutoirial
=================================

<!-- Tags: Java, TomCat, Linux, sysadmin, JSP, Servlet -->
intro
you need tomcat (link to tomcat tutorial) (or equivalent, tomcatee glasshfish, etc)
what are jsp (drop in standalone jsp files just like html files (think of it like a PHP script like HTML with java code inerjected for pre-processing) tomcat knows to process them)
comparison to JSF

jsp are an abstraction on top of servlets,and are converted to servlets under the hood. They are much easier to work with for beginners and get started with though as they don't require any special directory structure or XML configuration. You can just create a index.jsp or test.jsp in any directory inside the TomCat webapps/ directory.

- using them as a front end to servlets


other templating options available (velocity?jsf?jstl?)
simplest file (just plain html)
boiler plate file (with proper headers/internationalization)
hello world 
printing date
processing a form input
diff between servlet and jsp (link to servlet tutorial)
jsp are built on top of servlet technology
Set up tomcat (link to tutorial) (alternatives like glassfish can work)
what can u do with them? imports, math, other? forms?
diff content types
what are their limitations?
when to start using a servlet or a framework?
how to integrate with a servlet?
internationalization
form inputs? 
get vs post?
action tags, JSTL, custom tags, 
packaging JSPs as a war (no web.xml strictly necessary)


§ Just drop them in to webapps/some_custom_webapp/ and in subdirs
			
			§ Examples
				□ Straight HTML
				□ Hello world - calling a function
				□ Standard Boilerplate (setting doctype/mimetype/encoding/output date
                World clock - printing local times of major cities
                using sessions
                setting cookies
                making an ajax call back to self for updates
                
				□ Analytics - log->write to file bunch
				□ Network tools -> echo ip, user agent, etc, as .json if requested
				□ Dice roller -> d20 dice roller
				- contact form -> send email///log to file
				- guestbook read/post
				□ Fortune cookie/random quote page
Page visit counter (session cookie, how many times you’ve been to the site)
