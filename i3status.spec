Name:		i3status
Version:	2.13
Release:	1
Summary:	Generates a status line for dzen2 or wmii
Group:		Graphical desktop/Other
License:	MIT
URL:		http://i3wm.org/%{name}
Source0:	http://i3wm.org/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	libiw-devel
BuildRequires:	asciidoc
BuildRequires:	pkgconfig(libconfuse)
BuildRequires:	pkgconfig(libnl-genl-3.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(yajl)
Requires(pre):	libcap-utils

%description
i3status is a small program for filling dzen2 or wmii’s status bar via its 9P
pseudo filesystem.

%prep
%setup -q

#sed \
#    -e 's|CFLAGS+=-Wall -Wshadow -Wpointer-arith -Wcast-qual -Wsign-compare|CFLAGS+=%{optflags} -Wshadow -Wpointer-arith -Wcast-qual -Wsign-compare|g' \
#    -e 's|CFLAGS+=-g|CFLAGS+=|g' \
#    -e 's|@echo " CC $<"|@echo " $(CC) $(CFLAGS) -c -o $@ $<"|g' \
#    -e 's|@echo " LD $@"|@echo " $(CC) -o $@ src/*.o *.o $(LDFLAGS)"|g' \
#    -i Makefile

%build
%setup_compile_flags
%make CC=%{__cc}

%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/
install -Dpm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

%post
%{_sbindir}/setcap cap_net_admin=ep %{_bindir}/%{name}

%files
%doc LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
