%define	modname	PadWalker

Summary:	Play with other peoples' lexical variables
Name:		perl-%{modname}
Version:	2.5
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/PadWalker
Source0:	https://cpan.metacpan.org/authors/id/R/RO/ROBIN/PadWalker-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
PadWalker is a module which allows you to inspect (and even change!) lexical
variables in any subroutine which called you. It will only show those variables
which are in scope at the point of the call.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorarch}/PadWalker.pm
%{perl_vendorarch}/auto/PadWalker
%{_mandir}/man3/*
