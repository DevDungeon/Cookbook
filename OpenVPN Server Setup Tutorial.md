OpenVPN Server Setup Tutorial - Linode+Ubuntu
==============================

Add a Linode. Smallest tier will do. They 40GB unlimited incoming data on every plan. The outgoing badwidth starts at 125 Mbps and doubles with each tier.

https://manager.linode.com/linodes/add

Open the Linode and Deploy an Image
Ubuntu 16.04 LTS

Boot server

Download OpenVPN-AS
https://openvpn.net/index.php/access-server/download-openvpn-as-sw.html

# wget http://swupdate.openvpn.org/as/openvpn-as-2.1.2-Ubuntu16.amd_64.deb
wget http://swupdate.openvpn.org/as/openvpn-as-2.5.2-Ubuntu16.amd_64.deb
dpkg -i openvpn-as-2.5.2-Ubuntu16.amd_64.deb
passwd openvpn
useradd -d /home/dtron -m -G sudo dtron
passwd dtron

# if necessary rerun init (this was needed on DO), listen on 0.0.0.0
/usr/local/openvpn_as/bin/ovpn-init


Admin connect URL
https://<ip>:943/admin

Client connect URL
https://<ip>:943



Log in with linux user/pass to client portal
Download config file/installer