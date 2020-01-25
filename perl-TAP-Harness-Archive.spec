#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	TAP
%define		pnam	Harness-Archive
Summary:	TAP::Harness::Archive - Create an archive of TAP test results
Summary(pl.UTF-8):	TAP::Harness::Archive - tworzenie archiwów wyników testów TAP
Name:		perl-TAP-Harness-Archive
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/TAP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f7417c336ebb9c28937f494f05e342bb
URL:		http://search.cpan.org/dist/TAP-Harness-Archive/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Archive-Tar
BuildRequires:	perl-Test-Harness >= 3.05
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-YAML-Tiny
%endif
Requires:	perl-Test-Harness >= 3.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a direct subclass of TAP::Harness and behaves in
exactly the same way except for one detail. In addition to outputting
a running progress of the tests and an ending summary it can also
capture all of the raw TAP from the individual test files or streams
into an archive file (.tar or .tar.gz).

%description -l pl.UTF-8
Ten moduł jest bezpośrednią podklasą TAP::Harness i zachowuje się
dokładnie w ten sam sposób, z wyjątkiem jednego szczegółu. Poza
wypisywaniem postępów testów oraz końcowego podsumowania potrafi także
przechwycić całe surowe wyniki TAP z poszczególnych plików lub
strumieni testów do pliku archiwum (.tar lub .tar.gz).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/TAP/Harness/Archive.pm
%{_mandir}/man3/TAP::Harness::Archive.3pm*
