%define	module		PadWalker
%define	modprefix	PadWalker

%define	name		perl-%{module}

%define	version	1.5

%define	release	%mkrel 1

Summary:	Play with other peoples' lexical variables
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root

%description
PadWalker is a module which allows you to inspect (and even change!) lexical
variables in any subroutine which called you. It will only show those variables
which are in scope at the point of the call.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/PadWalker.pm
%{perl_vendorarch}/auto/PadWalker
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


