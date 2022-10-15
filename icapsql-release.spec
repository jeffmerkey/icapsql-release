%define _build_id_links none
%define debug_package %{nil}

Name:           icapsql-release
Version:        1.0 
Release:        1
Summary:        ICAPSQL Enterprise Linux repository configuration and gpg keys
License:        LGPL

URL:            http://www.icapsql.com
Source0:        RPM-GPG-KEY-icapsql
Source1:        icapsql.repo
BuildArch:      noarch

%description
This package contains the ICAPSQL Enterprise Linux repository
GPG key as well as ICAPSQL Repository configuration for dnf/yum.


%prep
%setup -q -c -T

%install
#GPG Key
install -Dpm 644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-icapsql

# dnf
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/icapsql.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog

