Summary:	IPv6 Tunneling daemon
Summary(pl.UTF-8):	Demon do tunelowania IPv6
Name:		miredo
Version:	1.2.2
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.remlab.net/files/miredo/archive/%{name}-%{version}.tar.bz2
# Source0-md5:	a04a40c4b42869968e00495636ff6d82
Source1:	%{name}-server.init
Source2:	%{name}-teredo.init
URL:		http://www.simphalempin.com/dev/miredo/
BuildRequires:	judy-devel
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miredo is an open-source Teredo IPv6 tunneling software, for Linux and
the BSD operating systems. It includes functional implementations of
all components of the Teredo specification (client, relay and server).
It is meant to provide IPv6 connectivity even from behind NAT devices.

This package contains Teredo server.

%description -l pl.UTF-8
Miredo to oprogramowanie do tunelowania IPv6 Toredo z otwartymi
źródłami dla systemów operacyjnych Linux i BSD. Zawiera funkcjonalne
implementacje wszystkich składników specyfikacji Toredo (klienta,
przekaźnika i serwera). Ma dostarczyć łączność z IPv6 nawet za
urządzeniami NAT.

Ten pakiet zawiera serwer Teredo.

%package common
Summary:	Common Miredo files
Summary(pl.UTF-8):	Wspólne pliki Miredo
Group:		Daemons

%description common
Common Miredo files.

%description common -l pl.UTF-8
Wspólne pliki Miredo.

%package client-teredo
Summary:	Miredo Teredo client
Summary(pl.UTF-8):	Klient Miredo Teredo
Group:		Daemons
Requires:	%{name}-common = %{version}-%{release}

%description client-teredo
Miredo Teredo client.

%description client-teredo -l pl.UTF-8
Klient Miredo Teredo.

%package libs
Summary:	Miredo libraries
Summary(pl.UTF-8):	Biblioteki Miredo
Group:		Libraries

%description libs
Miredo libraries.

%description libs -l pl.UTF-8
Biblioteki Miredo.

%package devel
Summary:	Development files for miredo
Summary(pl.UTF-8):	Pliki programistyczne dla miredo
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	judy-devel

%description devel
Development files for miredo.

%description devel -l pl.UTF-8
Pliki programistyczne dla miredo.

%package static
Summary:	Static miredo libraries
Summary(pl.UTF-8):	Statyczne biblioteki miredo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static miredo libraries.

%description static -l pl.UTF-8
Statyczne biblioteki miredo.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}-server
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}-teredo

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add miredo-server
%service miredo-server restart

%preun
if [ "$1" = "0" ]; then
        %service miredo-server stop
        /sbin/chkconfig --del miredo-server
fi

%post client-teredo
/sbin/chkconfig --add miredo-teredo
%service miredo-teredo restart

%preun client-teredo
if [ "$1" = "0" ]; then
        %service miredo-teredo stop
        /sbin/chkconfig --del miredo-teredo
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/miredo-server
%attr(754,root,root) /etc/rc.d/init.d/miredo-server
%{_mandir}/man5/miredo-server.conf.5*
%{_mandir}/man8/miredo-server.8*

%files common -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/teredo-mire
%attr(755,root,root) %{_sbindir}/miredo-checkconf
%dir %{_libdir}/miredo
%attr(755,root,root) %{_libdir}/miredo/miredo-privproc
%dir %{_sysconfdir}/miredo
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo/miredo.conf
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo/client-hook
%{_mandir}/man1/teredo-mire.1*
%{_mandir}/man8/miredo-checkconf.8*

%files client-teredo
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/miredo
%attr(754,root,root) /etc/rc.d/init.d/miredo-teredo
%{_mandir}/man5/miredo.conf.5*
%{_mandir}/man8/miredo.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libteredo.so.*.*.*
%attr(755,root,root) %{_libdir}/libtun6.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libteredo.so
%attr(755,root,root) %{_libdir}/libtun6.so
%{_libdir}/libteredo.la
%{_libdir}/libtun6.la
%{_includedir}/libteredo
%{_includedir}/libtun6

%files static
%defattr(644,root,root,755)
%{_libdir}/libteredo.a
%{_libdir}/libtun6.a
