#%global commit0 b734eef08163ac2263661cdaae48046b9e344972
# This commmit is the one at https://github.com/jbadiapa/opstools-ansible-1/commit/5178f7e2a72ca65973bbb92d8c12083f9142b22f
%global commit0 512286ec113b75790e31854a59c22205a03b069d 
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout 20161110git%{shortcommit0}

Name:           opstools-ansible
Version:        0.0.2
Release:        2%{?dist}
Summary:        Ansible playbooks for installing the server side of OpenStack operational tools and its documentation

License:        ASL 2.0
URL:            https://github.com/centos-opstools
Source0:        https://github.com/centos-opstools/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Group:          Applications/System
BuildArch:      noarch

BuildRequires:  pandoc
BuildRequires:  python-tox
BuildRequires:  ansible-lint
BuildRequires:  yamllint
 
Requires:       ansible > 2 

%description
Ansible playbooks for installing the server side of OpenStack operational tools

%prep
%autosetup -n %{name}-%{commit0}

%check
tools/validate-playbooks

%build 
make

%clean
rm -rf %{buildroot}

%install
install -d %{buildroot}%{_datadir}/%{name}/group_vars
install -d %{buildroot}%{_datadir}/%{name}/inventory
install -d %{buildroot}%{_datadir}/%{name}/roles
install -p -m 644 ansible.cfg %{buildroot}%{_datadir}/%{name}/ansible.cfg
install -p -m 644 playbook.yml %{buildroot}%{_datadir}/%{name}/playbook.yml
cp -pr group_vars/* %{buildroot}%{_datadir}/%{name}/group_vars
cp -pr inventory/* %{buildroot}%{_datadir}/%{name}/inventory
cp -pr roles/* %{buildroot}%{_datadir}/%{name}/roles
mkdir -p %{buildroot}%{_sbindir}
install -p -m 755 scripts/opstools-server-installation.sh %{buildroot}%{_sbindir}/opstools-server-installation.sh

%files
%defattr(-,root,root)
%license LICENSE.txt
%doc README.md
%doc README.html
%{_datadir}/%{name}/
%{_sbindir}/opstools-server-installation.sh



%changelog
* Thu Nov 10 2016 Juan Badia Payno <jbadiapa@redhat.com> - 0.0.2-0.20161110
- Documentation generated automaticaly 
- Some playbooks testing

* Tue Oct 11 2016 Sandro Bonazzola <sbonazzo@redhat.com> - 0.0.1-0.20161013gitee599e9
- Initial packaging
