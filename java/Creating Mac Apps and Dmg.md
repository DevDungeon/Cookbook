Creating Mac Apps and Dmg
===========================

In the Maven pom.xml add:

    <build>
        <plugins>
            <plugin>
                <groupId>sh.tak.appbundler</groupId>
                <artifactId>appbundle-maven-plugin</artifactId>
                <version>1.0.4</version>
                <configuration>
                    <mainClass>com.devdungeon.macapp.MainWindow</mainClass>
                    <dictionaryFile>YourCustomInfo.plist</dictionaryFile>
                <iconFile>CustomIncon.icns</iconFile>
                <jrePath>/Library/Java/JavaVirtualMachines/jdk1.8.0_60.jdk</jrePath>
                </configuration>
                <executions>
                  <execution>
                    <phase>package</phase>
                    <goals>
                      <goal>bundle</goal>
                    </goals>
                  </execution>
                </executions>
              </plugin>
        </plugins>
    </build>


Creating a .dmg file
--------------------

    hdiutil create -srcfolder path/to/app.app path/to/output.dmg