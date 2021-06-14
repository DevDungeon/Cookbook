/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.cookbook;

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 *
 * @author johnd
 */
public class GetUserHomeDir {
    public static void main(String[] args) {
        String homeDir = System.getProperty("user.home");
        System.out.println("Your home directory is: " + homeDir);
        
        // Getting a Path object from the string
        Path homeDirPath = Paths.get(homeDir);
        System.out.println(homeDir);
        System.out.println(homeDirPath);
        
        Path usersConfigDir = Paths.get(homeDir, ".config");
        System.out.println("Config dir is: " + usersConfigDir);
    }
}
