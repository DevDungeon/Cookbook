/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.cookbook;
// https://docs.oracle.com/javase/7/docs/api/java/nio/file/Path.html

import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;


/**
 *
 * @author johnd
 */
public class JoinPaths {
    
    public static void main(String[] args) {
        // Relative path
        Path relativePath = FileSystems.getDefault().getPath("var", "log", "access.log");
        System.out.println(relativePath); // var\log\access.log
        // Absolute path relative to CWD
        Path absolutePath = relativePath.toAbsolutePath();  
        System.out.println(absolutePath); // C:\Users\johnd\workspace\Cookbook\java\FileExamples\var\log\access.log
        
        // It will get converted to Windows format properly
        Path rootPath = Paths.get("/var/log/access.log"); // \var\log\access.log
        System.out.println(rootPath); // var\log\access.log
        absolutePath = rootPath.toAbsolutePath();  //  C:\var\log\access.log
        System.out.println(absolutePath);
     
        // Full absolute path to users home dir
        String homeDir = System.getProperty("user.home"); // C:\Users\johnd
        Path homeDirPath = Paths.get(homeDir);
        System.out.println(homeDir);
        System.out.println(homeDirPath);
        
    }
    
}
