%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: drkonqi
Version: 6.4.1
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/drkonqi/-/archive/%{gitbranch}/drkonqi-%{gitbranchd}.tar.bz2#/drkonqi-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{version}/drkonqi-%{version}.tar.xz
%endif
Summary: Crash handler for KDE software
URL: https://invent.kde.org/plasma/drkonqi
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KUserFeedbackQt6)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: python%{pyver}dist(chai)
BuildRequires: python%{pyver}dist(psutil)
BuildRequires: python%{pyver}dist(pygdbmi)
BuildRequires: python%{pyver}dist(sentry-sdk)
BuildRequires: systemd-coredump
BuildRequires: systemd
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DWITH_PYTHON_VENDORING:BOOL=OFF
Requires: python%{pyver}dist(psutil)
Requires: python%{pyver}dist(pygdbmi)
Requires: python%{pyver}dist(sentry-sdk)
Requires: systemd-coredump
# Renamed after 6.0 2025-04-27
%rename plasma6-drkonqi

%description
Crash handler for KDE software

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/drkonqi.*
%{_bindir}/drkonqi-coredump-gui
%{_prefix}/lib/systemd/system/drkonqi-coredump-processor@.service
%{_prefix}/lib/systemd/user/drkonqi-coredump-cleanup.service
%{_prefix}/lib/systemd/user/drkonqi-coredump-cleanup.timer
%{_prefix}/lib/systemd/user/drkonqi-coredump-launcher.socket
%{_prefix}/lib/systemd/user/drkonqi-coredump-launcher@.service
%{_libdir}/libexec/drkonqi
%{_libdir}/libexec/drkonqi-coredump-cleanup
%{_libdir}/libexec/drkonqi-coredump-launcher
%{_libdir}/libexec/drkonqi-coredump-processor
%{_qtdir}/plugins/drkonqi
%{_datadir}/applications/org.kde.drkonqi.coredump.gui.desktop
%{_datadir}/applications/org.kde.drkonqi.desktop
%{_datadir}/drkonqi
%{_bindir}/drkonqi-sentry-data
%{_prefix}/lib/systemd/user/default.target.wants/drkonqi-sentry-postman.path
%{_prefix}/lib/systemd/user/drkonqi-sentry-postman.path
%{_prefix}/lib/systemd/user/drkonqi-sentry-postman.service
%{_prefix}/lib/systemd/user/drkonqi-sentry-postman.timer
%{_prefix}/lib/systemd/user/timers.target.wants/drkonqi-sentry-postman.timer
%{_prefix}/lib/systemd/system/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
%{_prefix}/lib/systemd/user/default.target.wants/drkonqi-coredump-cleanup.service
%{_prefix}/lib/systemd/user/sockets.target.wants/drkonqi-coredump-launcher.socket
%{_prefix}/lib/systemd/user/timers.target.wants/drkonqi-coredump-cleanup.timer
%{_libdir}/libexec/drkonqi-sentry-postman
%{_prefix}/lib/systemd/user/drkonqi-coredump-pickup.service
%{_prefix}/lib/systemd/user/plasma-core.target.wants/drkonqi-coredump-pickup.service
%{_prefix}/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.path
%{_prefix}/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.timer
%{_libdir}/libexec/kf6/drkonqi-polkit-helper
%{_datadir}/dbus-1/system-services/org.kde.drkonqi.service
%{_datadir}/dbus-1/system.d/org.kde.drkonqi.conf
%{_datadir}/polkit-1/actions/org.kde.drkonqi.policy
