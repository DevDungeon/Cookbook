Java JAR Tutorial
=================

Intro
-----
Can make a jar that just holds a bunch of classes and is used as a library or create an executable jar.


Creating a .jar
-----------------
jar tool is just like the tar tool. you archvie and unarchive files in to a .jar

First compile a java source file in to a class file like normal

	javac MyProgram.java

Then create the jar. This will create a default manifest file in the jar.
It is just a collection of classes until a main class is defined and
then it becomes an executable jar as well.

	jar cf MyJar.jar MyProgram.class

	# how to add multiple files
	jar cf MyJar.jar ClassA.class ClassB.class ClassC.class
	
	# how to add everything in a dir
	?test- jar cf MyJar.jar /path/to/*.class
	?test- jar cf MyJar.jar /path/to/projectdir

Listing contents of a .jar

	jar tf MyJar.jar

Adding a file to an existing jar
-------------------

Extract a .jar
--------------

	jar xfv MyJar.jar

Edit the manifest file in the archive to include the main class.

	Main-Class: Main

Adding jar as class path
-----------------------

	# Add a single jar to classpath
	java -cp Libs.jar ClassName

	# Multiple entries. Can add whole directory of jars at once with *
	java -cp /class/dir/*:Other.jar ClassName

	# Or set CLASSPATH environment variable
	CLASSPATH=/path/to/jars/*:/path/to/Single.jar:/path/to/classes

With classpath set, you can call any class by its full packaged name. For example:

	# Assume the PortScanner.jar is in /home/nanodano/jars
	export CLASSPATH=/home/nanodano/jars/*

	java com.devdungeon.apps.portscanner.Main

Running an executable .jar
--------------------------

	java -jar MyProgram.jar arg1 arg2



Creating a .jar with Maven
---------------------------
Add the jar plugin to the Maven pom.xml 

	<project>
		<build>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-jar-plugin</artifactId>
					<version>2.4</version>
					<configuration>
						<archive>
							<manifest>
								<mainClass>com.mycompany.packagename.MainClass</mainClass>
							</manifest>
						</archive>
					</configuration>
				</plugin>
			</plugins>
		</build>
	</project>

Creating a .jar with dependencies inside using Maven
----------------------------------------------------

Add the shade plugin inside the Maven pom.xml

	<project>
		<build>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-shade-plugin</artifactId>
					<executions>
						<execution>
							<phase>package</phase>
							<goals>
								<goal>shade</goal>
							</goals>
						</execution>
					</executions>
					<configuration>
						<finalName>uber-${artifactId}-${version}</finalName>
					</configuration>
				</plugin>
			</plugins>
		</build>
	</project>

???? packaging in resource files?