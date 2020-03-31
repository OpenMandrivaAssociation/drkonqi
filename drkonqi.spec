%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	DrKonqi: The KDE Crash Handler
Name:		drkonqi
Version:	5.18.4.1
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
Conflicts:	plasma-workspace < 5.12.0
# duplicated files with KDE 4
Conflicts:	kdebase4-workspace < 2:4.11.23

%description
DrKonqi: The KDE Crash Handler

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/drkonqi.categories
%{_libdir}/libexec/drkonqi
%{_kde5_datadir}/applications/org.kde.drkonqi.desktop
%{_kde5_datadir}/drkonqi

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name
