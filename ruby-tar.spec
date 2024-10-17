%define rname tar
%define name ruby-%{rname}
%define version 0.1
%define release 9

Summary: Ruby implementation of the Unix 'tar' format
Name: %{name}
Version: %{version}
Release: %{release}
URL: https://ruby.jamisbuck.org/
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




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-8mdv2010.0
+ Revision: 433561
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-7mdv2009.0
+ Revision: 260435
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-6mdv2009.0
+ Revision: 251792
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1-4mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.1-4mdv2008.0
+ Revision: 16632
- Use Development/Ruby group


* Thu Jan 11 2007 Pascal Terjan <pterjan@mandriva.org> 0.1-4mdv2007.0
+ Revision: 107563
- Usestd ruby macros
- Import ruby-tar

* Sat Nov 12 2005 Pascal Terjan <pterjan@mandriva.org> 0.1-3mdk
- fix lib64

* Sat Sep 03 2005 Pascal Terjan <pterjan@mandriva.org> 0.1-2mdk
- birthday rebuild
- mkrel

* Thu Aug 26 2004 Pascal Terjan <pterjan@mandrake.org> 0.1-1mdk 
- first mdk release

