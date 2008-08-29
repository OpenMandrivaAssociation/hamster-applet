Name:           hamster-applet
Version:        2.23.90
Release:        %mkrel 2
Summary:        Time tracking applet

Group:          Graphical desktop/GNOME
License:        GPLv3+
URL:            http://code.google.com/p/projecthamster/
Source0:        http://download.gnome.org/sources/hamster-applet/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  pygtk2.0-devel
BuildRequires:  python-sqlite2
BuildRequires:  gnome-python-devel
BuildRequires:  gnome-python-applet
BuildRequires:  libxscrnsaver-devel
BuildRequires:  libgnome-window-settings-devel
BuildRequires:  intltool

Requires:       pygtk2.0
Requires:  	python-sqlite2
Requires:       gnome-python-applet
Requires:       gnome-python-canvas
Requires:       gnome-python-gnomevfs
Requires:       gnome-python-gconf
Requires:       gnome-python-evolution
Requires:       pygtk2.0-libglade

Requires(post):  GConf2
Requires(preun): GConf2


%description
Time tracking for masses in GNOME.

%prep
%setup -q


%build
%configure2_5x
%make


%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
%find_lang %{name}

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
%{py_platsitedir}/hamster
%{_libdir}/bonobo/servers/Hamster_Applet.server
%{_libdir}/hamster-applet
%{_datadir}/hamster-applet
%{_datadir}/icons/hicolor/*/apps/hamster-applet.*
%{_sysconfdir}/gconf/schemas/hamster-applet.schemas
%_datadir/gnome-control-center/keybindings/99-hamster-applet.xml


