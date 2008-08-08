%define realname MasonX-Request-WithApacheSession

Summary:	MasonX::Request::WithApacheSession - Add a session to the Mason Request object
Name:           perl-%{realname}
Version:        0.31
Release:        %mkrel 2
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MasonX/%{realname}-%{version}.tar.bz2 
BuildRequires:	perl(Apache::Session::Wrapper)
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This module integrates "Apache::Session" into Mason by adding
methods to the Mason Request object available in all Mason
components. Any subrequests created by a request share the same
session.

%prep

%setup -q -n %{realname}-%{version}

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

