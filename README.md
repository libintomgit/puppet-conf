pupclient-conf
============
Puppet client for Ubuntu>>

Aut: Libin
Curt : Naman


- Switch the to root - $sudo bash
- Download the file Ubuntu -$wget http://blrfpsvw01/infra/puppet/config_pupclient_ubuntu.sh
- Download the file Centos -$
- Delete the cert. from puppet cert server - $curl http://puppet.inmobi.com:5000/cleanCert/<hostname> or /$(hostname) - for using the self hostname
- Delete the cert. from ubuntu client - $rm -r /var/lib/puppet/ssl
- Run the downloaded file - $sh config_pupclient_ubuntu.sh 
- Follow the further instructions on screen.
