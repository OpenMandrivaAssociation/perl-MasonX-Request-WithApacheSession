%define upstream_name MasonX-Request-WithApacheSession
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
