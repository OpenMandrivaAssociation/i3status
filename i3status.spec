Name:		i3status
Version:	2.14
Release:	1
Summary:	Generates a status line for dzen2 or wmii
Group:		Graphical desktop/Other
License:	MIT
URL:		https://i3wm.org/%{name}
Source0:	https://i3wm.org/%{name}/%{name}-%{version}.tar.xz
#BuildRequires:	libiw-devel
BuildRequires:  meson
BuildRequires:	asciidoc
BuildRequires:	pkgconfig(libconfuse)
BuildRequires:	pkgconfig(libnl-genl-3.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(yajl)
BuildRequires:  xmlto
Requires(pre):	libcap-utils

%description
i3status is a small program for filling dzen2 or wmii’s status bar via its 9P
pseudo filesystem.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_sysconfdir}/
install -Dpm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

%post
%{_sbindir}/setcap cap_net_admin=ep %{_bindir}/%{name}

%files
%doc LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*

