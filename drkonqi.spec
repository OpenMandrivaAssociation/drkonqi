%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	DrKonqi: The KDE Crash Handler
Name:		drkonqi
Version:	5.27.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5XmlRpcClient)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	systemd-coredump
BuildRequires:	systemd-rpm-macros
BuildRequires:	pkgconfig(systemd)
Requires:	systemd-coredump
Conflicts:	plasma-workspace < 5.12.0
# duplicated files with KDE 4
Conflicts:	kdebase4-workspace < 2:4.11.23

%description
DrKonqi: The KDE Crash Handler.

%files -f %{name}.lang
%{_bindir}/drkonqi-coredump-gui
%{_datadir}/qlogging-categories5/%{name}.categories
%{_libdir}/libexec/drkonqi
%{_kde5_datadir}/applications/org.kde.drkonqi.desktop
%{_kde5_datadir}/applications/org.kde.drkonqi.coredump.gui.desktop
%{_kde5_datadir}/drkonqi
%{_presetdir}/86-%{name}.preset
%{_unitdir}/drkonqi-coredump-processor@.service
%{_userunitdir}/drkonqi-coredump-cleanup.service
%{_userunitdir}/drkonqi-coredump-cleanup.timer
%{_userunitdir}/drkonqi-coredump-launcher.socket
%{_userunitdir}/drkonqi-coredump-launcher@.service
%{_libdir}/libexec/drkonqi-*
%{_libdir}/qt5/plugins/drkonqi/KDECoredumpNotifierTruck.so

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DKDE_INSTALL_SYSTEMDUNITDIR=%{_systemd_util_dir} -DSYSTEMD_USER_UNIT_INSTALL_DIR=%{_userunitdir}

%build
%ninja -C build

%install
%ninja_install -C build

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-%{name}.preset << EOF
enable drkonqi-coredump-processor@.service
EOF

%find_lang %{name} --all-name

%post
%systemd_post drkonqi-coredump-processor@.service
%systemd_user_post drkonqi-coredump-cleanup.timer
%systemd_user_post drkonqi-coredump-launcher.socket

%preun
%systemd_preun drkonqi-coredump-processor@.service
%systemd_user_preun drkonqi-coredump-cleanup.timer
%systemd_user_preun drkonqi-coredump-launcher.socket

%postun
%systemd_postun drkonqi-coredump-processor@.service
%systemd_user_postun drkonqi-coredump-cleanup.timer
%systemd_user_postun drkonqi-coredump-launcher.socket
