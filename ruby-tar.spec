%define rname tar
%define name ruby-%{rname}
%define version 0.1
%define release %mkrel 4

Summary: Ruby implementation of the Unix 'tar' format
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://ruby.jamisbuck.org/
Source0: %{rname}-%{version}.tar.bz2
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8
BuildRequires: ruby-devel
BuildArch: noarch 

%description
A pure Ruby implementation of the Unix 'tar' file format. It is a library
that allows you to easily read, write, and append to tar files, whether the
'tar' command exists on your system or not. Right now it handles archives
containing regular files very well--links, block devices, and so forth are
not handled yet.

%prep
%setup -q -n %{rname}-%{version} 

%build
ruby setup.rb config 
ruby setup.rb setup

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*.rb
%doc LICENSE ChangeLog doc samples


