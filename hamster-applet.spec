Name:           hamster-applet
Version:        2.32.1
Release:        %mkrel 1
Summary:        Time tracking applet

Group:          Graphical desktop/GNOME
License:        GPLv3+
URL:            http://code.google.com/p/projecthamster/
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
SYSCONFDIR=%_sysconfdir ./waf --prefix=%_prefix configure build

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


