Name:           hamster-applet
Version:        2.32.1
Release:        %mkrel 3
Summary:        Time tracking applet

Group:          Graphical desktop/GNOME
License:        GPLv3+
URL:            https://code.google.com/p/projecthamster/
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  pygtk2.0-devel
BuildRequires:  python-sqlite2
BuildRequires:  gnome-python-devel
BuildRequires:  gnome-python-applet
BuildRequires:  libxscrnsaver-devel
BuildRequires:  libgnome-window-settings-devel
BuildRequires:  intltool
BuildRequires:  gnome-doc-utils >= 0.17.3
Requires:       pygtk2.0
Requires:  	python-sqlite2
Requires:       gnome-python-applet
Requires:       gnome-python-canvas
Requires:       gnome-python-desktop
Requires:       gnome-python-gconf
Requires:       gnome-python-evolution
Requires:       pygtk2.0
Requires(post):  GConf2
Requires(preun): GConf2

%description
Time tracking for masses in GNOME.

%prep
%setup -q


%build
SYSCONFDIR=%_sysconfdir ./waf --prefix=%_prefix --libdir=%_libdir configure build

%install
rm -rf $RPM_BUILD_ROOT
./waf install --destdir=%buildroot
%find_lang %{name} --with-gnome
%if %_lib != lib
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/* %buildroot%_libdir
%endif

%preun
%preun_uninstall_gconf_schemas hamster-applet

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_sysconfdir}/gconf/schemas/hamster-applet.schemas
%_bindir/gnome-time-tracker
%_bindir/hamster-cli
%_bindir/hamster-service
%_bindir/hamster-time-tracker
%_datadir/applications/hamster-applet.desktop
%_datadir/applications/hamster-time-tracker.desktop
%_datadir/dockmanager/metadata/hamster_control.py.info
%_datadir/dockmanager/scripts/hamster_control.py
%_datadir/gnome-control-center/keybindings/90-hamster-applet.xml
%_datadir/docky/helpers/*
%_datadir/dbus-1/services/org.gnome.hamster.service
%{py_platsitedir}/hamster
#gw the applet is the reason this is not a noarch package:
%{_libdir}/bonobo/servers/Hamster_Applet.server
%{_libdir}/hamster-applet
%{_datadir}/hamster-applet
%{_datadir}/icons/hicolor/*/apps/hamster-applet.*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.1-3mdv2011.0
+ Revision: 665403
- mass rebuild

* Thu Mar 03 2011 Pascal Terjan <pterjan@mandriva.org> 2.32.1-2
+ Revision: 641511
- Set libdir so that the .server is correct

* Tue Nov 16 2010 Götz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597923
- update to new version 2.32.1

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 593315
- rebuild for new python 2.7

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581277
- update to new version 2.32.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 577978
- update to new version 2.31.92

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574571
- update to new version 2.31.91

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570863
- new version
- update file list

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565130
- new version
- update file list

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 563612
- fix installation
- new version
- switch to waf build system
- update file list

* Tue Jun 22 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548551
- Release 2.30.2

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539204
- update to new version 2.30.1

* Wed Mar 31 2010 Götz Waschk <waschk@mandriva.org> 2.30.0.1-1mdv2010.1
+ Revision: 530426
- update to new version 2.30.0.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528787
- update to new version 2.30.0

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-2mdv2010.1
+ Revision: 515991
- update python module deps
- update to new version 2.29.92

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509627
- update to new version 2.29.91

* Mon Feb 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502414
- new version
- update file list

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496488
- update build deps
- new version
- update file list

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 489953
- update to new version 2.29.5

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 481226
- update to new version 2.29.4

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475429
- update to new version 2.29.3

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458859
- Release 2.28.1

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447183
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437427
- update to new version 2.27.92

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414477
- update to new version 2.27.90

* Mon Jul 27 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 400787
- update to new version 2.27.5

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395760
- update to new version 2.27.4

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386269
- update to new version 2.27.3

* Tue May 26 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379783
- update to new version 2.27.2

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374181
- new version

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355977
- update to new version 2.26.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347535
- update to new version 2.25.92

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341234
- update to new version 2.25.91

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336844
- update to new version 2.25.90

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 319758
- rebuild for new python

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315816
- update to new version 2.25.3

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 306428
- update to new version 2.24.2

* Mon Oct 20 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295610
- new version
- fix source URL

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287257
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282698
- new version

* Fri Aug 29 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-2mdv2009.0
+ Revision: 277463
- new version
- rebuild

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273736
- new version

* Tue Aug 05 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-2mdv2009.0
+ Revision: 264027
- fix dep

* Tue Aug 05 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263916
- import hamster-applet


* Tue Aug  5 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
- adapt for Mandriva
- new version

* Wed Jun 11 2008 Mads Villadsen <maxx@krakoa.dk> - 0.6.1-1
- Update to latest upstream release
- Not stealing middle-click to move applet
- Correct label orientation on vertical panels
- Fixed fact pushing on overlap

* Mon Jun 9 2008 Mads Villadsen <maxx@krakoa.dk> - 0.6-1
- Update to latest upstream release
- Simple reporting via Overview dialog

* Sun May 25 2008 Mads Villadsen <maxx@krakoa.dk> - 0.5-1
- Update to latest upstream release
- Preferences are now editable via user interface
- Added option to stop tracking on shutdown
- Current activity is now showing up in totals

* Mon May 5 2008 Mads Villadsen <maxx@krakoa.dk> - 0.4-1
- Update to latest upstream release
- Fact editing functionality

* Sun May 4 2008 Mads Villadsen <maxx@krakoa.dk> - 0.3-1
- Update to latest upstream release

* Mon Apr 28 2008 Mads Villadsen <maxx@krakoa.dk> - 0.2-3
- Depend on gnome-python2-evolution instead of evolution-python

* Sat Apr 26 2008 Mads Villadsen <maxx@krakoa.dk> - 0.2-2
- Add missing libXScrnSaver-devel to BuildRequires

* Fri Apr 25 2008 Mads Villadsen <maxx@krakoa.dk> - 0.2-1
- Update to new upstream release

* Mon Apr 21 2008 Mads Villadsen <maxx@krakoa.dk> - 0.1.7.4-3
- Add hicolor-icon-theme as a Requires
- Add lots of other Requires as well - it should now run as well as build

* Sun Apr 20 2008 Mads Villadsen <maxx@krakoa.dk> - 0.1.7.4-2
- Split BuildRequires into more lines
- Don't mark the schema file as a config file

* Fri Apr 18 2008 Mads Villadsen <maxx@krakoa.dk> - 0.1.7.4-1
- New upstream version
- Updated license (as per http://mail.gnome.org/archives/desktop-devel-list/2008-April/msg00173.html)
- Added missing BuildRequires
- Correctly use python_sitelib instead of python_sitearch

* Wed Apr 16 2008 Mads Villadsen <maxx@krakoa.dk> - 0.1.7.3-1
- First release
