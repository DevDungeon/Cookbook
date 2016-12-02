package com.devdungeon.sshexample;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelShell;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import com.jcraft.jsch.UIKeyboardInteractive;
import com.jcraft.jsch.UserInfo;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.*;

public class EnvironmentVariables{
    
    public static void main(String[] arg){


        try {
            JSch jsch = new JSch();
            jsch.setKnownHosts("C:\\Users\\dtron\\.ssh\\known_hosts");
            jsch.addIdentity("A:\\Dropbox\\private\\ssh\\id_rsa");
            Session session = jsch.getSession("dtron", "www.devdungeon.com", 22);
            
            // It must not be recommended, but if you want to skip host-key check, invoke following,
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect(30 * 1000); // making a connection with the optional timeout
            
            Channel channel = session.openChannel("shell");
            
            channel.setInputStream(System.in);
            channel.setOutputStream(System.out);
            
            // Set environment variables
            //((ChannelShell)channel).setEnv("ENV_VAR", "someValue");
            
            channel.connect(3*1000);
            
        } catch (JSchException ex) {
            Logger.getLogger(EnvironmentVariables.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
