%define	upstream_name	 PadWalker
%define upstream_version 1.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

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


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 1.920.0-3mdv2012.0
+ Revision: 767858
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.920.0-2mdv2011.0
+ Revision: 555295
- rebuild

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.920.0-1mdv2011.0
+ Revision: 553969
- update to 1.92

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.9-2mdv2011.0
+ Revision: 551996
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2010.0
+ Revision: 389800
- update to new version 1.9

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.7-2mdv2009.0
+ Revision: 268706
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdv2009.0
+ Revision: 195165
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.5-2mdv2008.1
+ Revision: 151413
- rebuild for perl-5.10.0

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.5-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 06 2007 Scott Karns <scottk@mandriva.org> 1.5-1mdv2007.0
+ Revision: 104724
- Import perl-PadWalker

* Fri Jan 05 2007 Scott Karns <scottk@mandriva.org> 1.5-1mdv2007.1
- 1.5

* Thu Nov 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.0-1mdk
- 1.0

* Tue Oct 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.13-1mdk
- 0.13

* Thu May 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- First Mandriva release

