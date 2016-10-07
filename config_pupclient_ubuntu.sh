#!/bin/sh
echo "deb http://repo.corp.inmobi.com:9999/precise ./" >> /etc/apt/sources.list.d/inmobi.list
/usr/bin/wget -N --directory-prefix=/etc/apt http://fai.uh1.inmobi.com:9999/files/inmobi_global.gpg
/usr/bin/apt-key add /etc/apt/inmobi_global.gpg
apt-get update
apt-get install puppetlabs-release
apt-get update
apt-get install puppet=3.7.5-1puppetlabs1 puppet-common=3.7.5-1puppetlabs1
puppet agent --test --server puppet.inmobi.com

