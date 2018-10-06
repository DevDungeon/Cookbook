Command Line Maven Building
===========================

Run these in the dir with the pom.xml

# Compile and create JAR (or other packages)

    mvn package

# Clean and install most things with

    mvn clean install

# Generating new Maven projects

    mvn archetype:generate -DarchetypeArtifactId=maven-archetype-quickstart
    mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp
    
    # Be sure to verify the latest versions https://github.com/DevDungeon/maven.archetypes.application
    mvn archetype:generate                                    \
        -DarchetypeGroupId=com.devdungeon.maven.archetypes    \
        -DarchetypeArtifactId=application                     \
        -DarchetypeVersion=0.1.0

    # Be sure to verify the latest versions https://github.com/DevDungeon/maven.archetypes.library
    mvn archetype:generate                                    \
        -DarchetypeGroupId=com.devdungeon.maven.archetypes    \
        -DarchetypeArtifactId=library                         \
        -DarchetypeVersion=1.0.5                              \


# Sample pom.xml

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>
        <groupId>com.devdungeon</groupId>
        <artifactId>JarWithResourcesAndDependencies</artifactId>
        <version>1.0</version>
        <packaging>jar</packaging>
        <properties>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            <maven.compiler.source>1.8</maven.compiler.source>
            <maven.compiler.target>1.8</maven.compiler.target>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-jar-plugin</artifactId>
                    <version>2.4</version>
                    <configuration>
                        <archive>
                            <manifest>
                                <mainClass>com.devdungeon.jarwithresources.Main</mainClass>
                            </manifest>
                        </archive>
                    </configuration>
                </plugin> 
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
        <name>JarWithResourcesAndDependencies</name>
    </project>