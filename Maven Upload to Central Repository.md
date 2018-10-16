Uploading to Maven Central Tutorial
===================================

You can push your own packages to maven central and make it available to everyone
It's a tricky process to set up the first time, but once you get it ready, it's incredibly easy to push updates. This tutorial will walk you through the basics of registering and pushing projects to Maven central.

Links
------

- https://oss.sonatype.org/#welcome
- https://issues.sonatype.org
- https://maven.apache.org/guides/mini/guide-central-repository-upload.html
- http://central.sonatype.org/pages/requirements.html
- https://dzone.com/articles/deploy-maven-central
- https://issues.sonatype.org/browse/OSSRH-37174?page=com.atlassian.jira.plugin.system.issuetabpanels%3Aall-tabpanel


Sign up
----------------------

1) Sign up for SonaType https://issues.sonatype.org/secure/Signup!default.jspa, get your namespace.
2) Create a GPG key to sign the code (save it somewhere safe)


Create a package that meets the requirements (done through pom.xml):
-------------------------------------------------------------

- Required metadata in POM (name, description, url, etc)
- Supply Javadoc and Sources (*-javadoc.jar, *-sources.jar)
- Sign files with GPG (*.asc for each file)
- License info
- Developer info
- SCM info (git url)


A note about gpg
-------------
You will have to sign your files with a private key that is 
You will need gpg installed and have a private key configured and also available on a public keyserver. 

Check out my [GPG Basics Tutorial](LINK)------ for a walkthrough of how to install gpg, generate keys, import and export, and push your private key to MIT's public key server.


Set up settings.xml in home dir or project dir or ~/.m2/settings.xml:
------------------------------------------------

    <profiles>
        <profile>
            <id>sonatype-oss-release</id>
            <properties>
            <gpg.keyname>XXXXXXXXXXXXXX</gpg.keyname>
            <!--<gpg.passphrase>xxxx</gpg.passphrase> (should get a prompt to type it in interactively if not supplied here)-->
            <!--<gpg.executable>/path/to/gpg.exe</gpg.executable>-->
            </properties>
        </profile>
    </profiles>

Building
---------------

    mvn clean
    mvn compile
    mvn package
    mvn verify  # Will sign/check GPG
    mvn install  # Install to local maven repo
    mvn deploy  # Push to Sonatype->maven central


Sample ~/.m2/settings.xml
-------------------------

    <settings>
        <servers>
            <server>
                <id>ossrh</id> <!-- Match the server id used in <distributionManagement> and <serverId> for sonatype staging plugin in pom.xml -->
                <username>nanodano</username>
                <password>*************</password>
            </server>
        </servers>
        <profiles>
            <profile>
                <id>sonatype-oss-release</id>
                <properties>
                    <gpg.keyname>NanoDano</gpg.keyname>
                    <!--<gpg.passphrase>**********</gpg.passphrase>-->
                </properties>
            </profile>
        </profiles>
    </settings>

Sample project pom.xml
-----------------

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>com.devdungeon.tools</groupId>
        <artifactId>http</artifactId>
        <version>1.0.1</version>

        <name>${project.groupId}:${project.artifactId}</name>
        <description>An HTTP utility library</description>
        <url>https://www.devdungeon.com/projects</url>

        <licenses>
            <license>
                <name>The Apache License, Version 2.0</name>
                <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
            </license>
        </licenses>

        <developers>
            <developer>
                <name>NanoDano</name>
                <email>nanodano@devdungeon.com</email>
                <organization>DevDungeon</organization>
                <organizationUrl>https://www.devdungeon.com</organizationUrl>
            </developer>
        </developers>

        <dependencies>
            <dependency>
                <groupId>org.apache.httpcomponents</groupId>
                <artifactId>httpclient</artifactId>
                <version>4.5.4</version>
            </dependency>
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <configuration>
                        <source>1.8</source>
                        <target>1.8</target>
                    </configuration>
                </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-source-plugin</artifactId>
                    <version>3.0.1</version>
                    <executions>
                        <execution>
                            <id>attach-sources</id>
                            <goals>
                                <goal>jar-no-fork</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-javadoc-plugin</artifactId>
                    <version>3.0.0</version>
                    <executions>
                        <execution>
                            <id>attach-javadocs</id>
                            <goals>
                                <goal>jar</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-gpg-plugin</artifactId>
                    <version>1.6</version>
                    <executions>
                        <execution>
                            <id>sign-artifacts</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>sign</goal>
                            </goals>
                            <configuration>
                                <!-- GPG keyname var set in the settings.xml maven file -->
                                <keyname>${gpg.keyname}</keyname>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <groupId>org.sonatype.plugins</groupId>
                    <artifactId>nexus-staging-maven-plugin</artifactId>
                    <version>1.6.8</version>
                    <extensions>true</extensions>
                    <configuration>
                        <serverId>ossrh</serverId>
                        <nexusUrl>https://oss.sonatype.org/</nexusUrl>
                        <autoReleaseAfterClose>true</autoReleaseAfterClose>
                    </configuration>
                </plugin>
            </plugins>

        </build>

        <distributionManagement>
            <snapshotRepository>
                <id>ossrh</id>
                <url>https://oss.sonatype.org/content/repositories/snapshots</url>
            </snapshotRepository>
            <repository>
                <id>ossrh</id>
                <url>https://oss.sonatype.org/service/local/staging/deploy/maven2/</url>
            </repository>
        </distributionManagement>

        <scm>
            <connection>scm:git:git://github.com/DevDungeon/tools-http.git</connection>
            <developerConnection>scm:git:ssh://github.com:DevDungeon/tools-http.git</developerConnection>
            <url>https://github.com/DevDungeon/tools-http/tree/master</url>
        </scm>

    </project>
