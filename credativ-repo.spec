Name:		credativ-repo
Version:	2019
Release:	1
Summary:	Yum repository for Elephant Shed
Group:		System Environment/Base
License:	BSD
URL:		https://packages.credativ.com/public/postgresql/
Source0:	aptly.key
Source1:	credativ.repo
Source2:	credativ-test.repo
BuildArch:	noarch
Requires:	epel-release

%package -n credativ-test-repo
Summary: Yum test repository for Elephant Shed
Requires: epel-release

%description
This package installs the repository for Elephant Shed on Red Hat and CentOS.

%description -n credativ-test-repo
This package installs the test repository for Elephant Shed on Red Hat and CentOS.

%prep
%setup -q -c -T

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/CREDATIV-KEY
%{__install} -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/credativ.repo
%{__install} -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d/credativ-test.repo

%clean
%{__rm} -rf %{buildroot}

%post
/bin/rpm --import %{_sysconfdir}/pki/rpm-gpg/CREDATIV-KEY

%post -n credativ-test-repo
/bin/rpm --import %{_sysconfdir}/pki/rpm-gpg/CREDATIV-KEY

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/credativ.repo
%{_sysconfdir}/pki/rpm-gpg/*

%files -n credativ-test-repo
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/credativ-test.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
