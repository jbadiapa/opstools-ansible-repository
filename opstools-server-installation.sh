#!/bin/bash

#Help info
if [ "-h" == $1 ]; then
  echo 
  echo
  echo "The first time the command is run, it will generate the ~/.opstools.hosts file"
  echo "Once the ~/.opstools.hosts file is created, when the command is executed againi"
  echo "the ansible-playbook will be deployed"
  echo
  echo "By default everything will be installed on localhost"
  echo "It can also be run like $0 REMOTE_IP to install there"
  echo "You can edit manually the ~/.opstools.hosts file to install the tools on different servers"
  echo 
  echo "* Just to generate the ~/.opstools.hosts file:"
  echo "   $0"
  echo 
  echo "* To install everything on localhost:"
  echo "   $0 && $0"
  echo 
  echo "* To install everything on 192.168.122.125:"
  echo "   $0 192.168.122.125 && $0"
  echo 
  exit 0
fi

#Creates the ~/.opstools.hosts if it does not exits
if [ ! -f  ~/.opstools.hosts ]; then
  if [ "x$1" != "x" ]; then
    HOST=$1
  else
    HOST="localhost"
  fi

  if [ "x$PM_HOST" == "x" ]; then
   PM_HOST=$HOST
  fi

  if [ "x$AM_HOST" == "x" ]; then
   AM_HOST=$HOST
  fi
  if [ "x$LOG_HOST" == "x" ]; then
   LOG_HOST=$HOST
  fi

 CONNECTION=""
 for host in $(echo "$PM_HOST $AM_HOST $LOG_HOST"| xargs -n1 | sort -u ) ; do
  if [ "localhost" == $host ]; then
   CONNECTION=$CONNECTION"localhost ansible_connection=local
"
  else
   CONNECTION=$CONNECTION"$host ansible_connection=ssh user=root
"
  fi
 done

cat <<EOF > ~/.opstools.hosts
[logging_hosts]
$LOG_HOST
[am_hosts]
$AM_HOST
[pm_hosts]
$PM_HOST

[targets]
$CONNECTION
EOF

echo "The file ~/.opstools.hosts was created"

else
  #Executes the playbook to install the opstools
  ansible-playbook -i /usr/share/opstools-ansible/inventory -i ~/.opstools.hosts /usr/share/opstools-ansible/playbook.yml
fi

