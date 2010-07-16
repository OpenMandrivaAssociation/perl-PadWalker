%define	upstream_name	 PadWalker
%define upstream_version 1.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Play with other peoples' lexical variables
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROBIN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PadWalker is a module which allows you to inspect (and even change!) lexical
variables in any subroutine which called you. It will only show those variables
which are in scope at the point of the call.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/PadWalker.pm
%{perl_vendorarch}/auto/PadWalker
%{_mandir}/*/*
