%define module  IO-Pager
%define name    perl-%{module}
%define release %mkrel 1
%define version 0.06

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Syndication feed auto-discovery
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRoot:          %{_tmppath}/%{name}-%{version}
BuildArch:          noarch

%description
Perl Module for Syndication feed auto-discovery.

Feed::Find implements feed auto-discovery for finding syndication feeds, 
given a URI. It (currently) passes all of the auto-discovery tests at 
http://diveintomark.org/tests/client/autodiscovery/ .

Feed::Find will discover the following feed formats:

RSS 0.91
RSS 1.0
RSS 2.0
Atom

%prep
%setup -q -n %{module}-%{version}

%build
# only when building from CVS (version 1.51-3mdk)
#CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
#make docs -i
# only when building from CVS (version 1.51-3mdk)
SKIP_SAX_INSTALL=1 CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test < /dev/null

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/IO/t.pl

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/IO/Pager*
%{_mandir}/*/*
