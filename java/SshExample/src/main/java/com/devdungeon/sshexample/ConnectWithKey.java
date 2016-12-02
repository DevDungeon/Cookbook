package com.devdungeon.sshexample;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ConnectWithKey{
    
    public static void main(String[] arg){
        try {
            JSch jsch = new JSch();
            jsch.setKnownHosts("~/.ssh/known_hosts");
            jsch.addIdentity("~/.ssh/id_rsa");
            Session session = jsch.getSession("dtron", "www.devdungeon.com", 22);
            
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect(30 * 1000);
            
            Channel channel = session.openChannel("shell");
            
            channel.setInputStream(System.in);
            channel.setOutputStream(System.out);
            
            channel.connect(3 * 1000);
        } catch (JSchException ex) {
            Logger.getLogger(ConnectWithKey.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
