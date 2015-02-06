%define upstream_name MasonX-Request-WithApacheSession
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	MasonX::Request::WithApacheSession - Add a session to the Mason Request object
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MasonX/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildRequires:	perl(Apache::Session::Wrapper)
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module integrates "Apache::Session" into Mason by adding
methods to the Mason Request object available in all Mason
components. Any subrequests created by a request share the same
session.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%{__make}

#%%check
#%__make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

./Build install destdir=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README SIGNATURE
%{perl_vendorlib}/MasonX/Request/WithApacheSession.pm
%{perl_vendorlib}/MasonX/Request/WithMultiSession.pm
%{_mandir}/man3/*


%changelog
* Wed Jul 29 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.0
+ Revision: 403849
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.31-2mdv2009.0
+ Revision: 268590
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.0
+ Revision: 202325
- update to new version 0.31

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu May 04 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.30-3mdk
- Add BuildRequires

* Wed May 03 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.30-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.30-1mdk
- initial Mandriva package

