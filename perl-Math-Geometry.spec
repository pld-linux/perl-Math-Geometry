#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Geometry
Summary:	Math::Geometry - geometry related functions
Summary(pl.UTF-8):	Math::Geometry - funkcje związane z geometrią
Name:		perl-Math-Geometry
Version:	0.03
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/GMCCAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b875ad521c0bab56d78ed525466caff9
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
