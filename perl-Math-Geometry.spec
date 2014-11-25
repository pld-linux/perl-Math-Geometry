#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Geometry
%include	/usr/lib/rpm/macros.perl
Summary:	Math::Geometry - geometry related functions
Summary(pl.UTF-8):	Math::Geometry - funkcje związane z geometrią
Name:		perl-Math-Geometry
Version:	0.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc05acfb1b8ddcc3bb869f0df13ea15b
URL:		http://search.cpan.org/dist/Math-Geometry/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Matrix
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements classic geometry methods.

%description -l pl.UTF-8
Ten pakiet zawiera implementacje klasycznych metod geometrycznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e '$.==1&&s|/usr/local/|/usr/|' Geometry.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Geometry.pm
%{_mandir}/man3/*
