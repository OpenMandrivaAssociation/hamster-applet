Name:           hamster-applet
Version:        2.30.2
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
%configure2_5x --disable-schemas-install
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name} --with-gnome

%post
%update_icon_cache hicolor
%post_install_gconf_schemas hamster-applet

%preun
%preun_uninstall_gconf_schemas hamster-applet

%postun
%clean_icon_cache hicolor
 
%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/hamster-applet.schemas
%_bindir/gnome-time-tracker
%_bindir/hamster-standalone
%_datadir/applications/hamster-standalone.desktop
%{py_platsitedir}/hamster
%{_libdir}/bonobo/servers/Hamster_Applet.server
%{_libdir}/hamster-applet
%{_datadir}/hamster-applet
%{_datadir}/icons/hicolor/*/apps/hamster-applet.*
%_datadir/gnome-control-center/keybindings/99-hamster-applet.xml


