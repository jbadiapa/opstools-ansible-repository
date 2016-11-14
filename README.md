# opstools-ansible-repository

The epel repository is needed to build the rpm as it uses:

> - pandoc
> - python-tox
> - ansible-lint
> - yamllint

This spec file is an upgrade of the one created by Sandro Bonazzola [releng-tools]

```bash
cat <<EOF > ~/.opstools.hosts
[logging_hosts]
192.168.1.100
[am_hosts]
192.168.1.100
[pm_hosts]
192.168.1.100

[targets]
192.168.1.100 ansible_connection=ssh user=root
EOF

ansible-playbook -i /usr/share/opstools-ansible/inventory -i ~/.opstools.hosts /usr/share/opstools-ansible/playbook.yml
```

[releng-tools]:https://gerrit.ovirt.org/gitweb?p=releng-tools.git
