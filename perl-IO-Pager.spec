%define upstream_name    IO-Pager
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl Module for Syndication feed auto-discovery
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# only when building from CVS (version 1.51-3mdk)
#CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
#make docs -i
# only when building from CVS (version 1.51-3mdk)
SKIP_SAX_INSTALL=1 CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test < /dev/null

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/IO/t.pl

%files
%doc CHANGES README
%{perl_vendorlib}/IO/Pager*
%{_mandir}/*/*


%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 504936
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.06-4mdv2010.0
+ Revision: 430472
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.06-3mdv2009.0
+ Revision: 241559
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 26 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.06-1mdv2008.0
+ Revision: 31531
- Import perl-IO-Pager



* Sun May 20 2007 Shlomi Fish  0.06-1mdv2007.1
- Initial release. Adapted the Feed-Find spec for this one.
