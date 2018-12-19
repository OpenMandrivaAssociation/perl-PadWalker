%define	modname	PadWalker
%define modver 2.3

Summary:	Play with other peoples' lexical variables
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/PadWalker
Source0:	https://cpan.metacpan.org/authors/id/R/RO/ROBIN/PadWalker-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
PadWalker is a module which allows you to inspect (and even change!) lexical
variables in any subroutine which called you. It will only show those variables
which are in scope at the point of the call.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/PadWalker.pm
%{perl_vendorarch}/auto/PadWalker
%{_mandir}/man3/*
