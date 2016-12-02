package com.devdungeon.sshexample;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.ChannelShell;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import com.jcraft.jsch.UIKeyboardInteractive;
import com.jcraft.jsch.UserInfo;
import java.io.IOException;
import java.io.InputStream;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.*;

public class ExecuteProgram {

    public static void main(String[] arg) {

        try {
            JSch jsch = new JSch();
            jsch.setKnownHosts("C:\\Users\\dtron\\.ssh\\known_hosts");
            jsch.addIdentity("A:\\Dropbox\\private\\ssh\\id_rsa");
            Session session = jsch.getSession("dtron", "www.devdungeon.com", 22);

            // It must not be recommended, but if you want to skip host-key check, invoke following,
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect(30 * 1000); // making a connection with the optional timeout

            Channel channel = session.openChannel("exec");
            ((ChannelExec) channel).setCommand("ls");

            channel.setInputStream(null);
            ((ChannelExec) channel).setErrStream(System.err);
            //channel.setOutputStream(System.out);  // default?

            // Set environment variables
            //((ChannelShell)channel).setEnv("ENV_VAR", "someValue");
            channel.connect(3 * 1000);

            
            
            
            
            InputStream in = null;
            try {
                in = channel.getInputStream();
            } catch (IOException ex) {
                Logger.getLogger(ExecuteProgram.class.getName()).log(Level.SEVERE, null, ex);
            }
            byte[] tmp = new byte[1024];
            while (true) {
                try {
                    while (in.available() > 0) {
                        int i = 0;
                        try {
                            i = in.read(tmp, 0, 1024);
                        } catch (IOException ex) {
                            Logger.getLogger(ExecuteProgram.class.getName()).log(Level.SEVERE, null, ex);
                        }
                        if (i < 0) {
                            break;
                        }
                        System.out.print(new String(tmp, 0, i));
                    }
                } catch (IOException ex) {
                    Logger.getLogger(ExecuteProgram.class.getName()).log(Level.SEVERE, null, ex);
                }
                if (channel.isClosed()) {
                    try {
                        if (in.available() > 0) {
                            continue;
                        }
                    } catch (IOException ex) {
                        Logger.getLogger(ExecuteProgram.class.getName()).log(Level.SEVERE, null, ex);
                    }
                    System.out.println("exit-status: " + channel.getExitStatus());
                    break;
                }
                try {
                    Thread.sleep(1000);
                } catch (Exception ee) {
                }
            }
            
            

            channel.disconnect();
            session.disconnect();
        } catch (JSchException ex) {
            Logger.getLogger(ExecuteProgram.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
