Summary:	IPv6 Tunneling daemon
Summary(pl.UTF-8):   Demon do tunelowania IPv6
Name:		miredo
Version:	0.8.0
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.remlab.net/files/miredo/archive/%{name}-%{version}.tar.bz2
# Source0-md5:	326664cb9af10a38806149b7bd565340
URL:		http://www.simphalempin.com/dev/miredo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miredo is an open-source Teredo IPv6 tunneling software, for Linux and
the BSD operating systems. It includes functional implementations of
all components of the Teredo specification (client, relay and server).
It is meant to provide IPv6 connectivity even from behind NAT devices.

%description -l pl.UTF-8
Miredo to oprogramowanie do tunelowania IPv6 Toredo z otwartymi
źródłami dla systemów operacyjnych Linux i BSD. Zawiera funkcjonalne
implementacje wszystkich składników specyfikacji Toredo (klienta,
przekaźnika i serwera). Ma dostarczyć łączność z IPv6 nawet za
urządzeniami NAT.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-server.conf{-dist,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo-server.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo.conf
%attr(755,root,root) %{_sbindir}/miredo
%attr(755,root,root) %{_sbindir}/miredo-server
%{_mandir}/man5/miredo-server.conf.5*
%{_mandir}/man5/miredo.conf.5*
%{_mandir}/man8/miredo-server.8*
%{_mandir}/man8/miredo.8*
