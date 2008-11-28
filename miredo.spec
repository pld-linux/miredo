Summary:	IPv6 Tunneling daemon
Summary(pl.UTF-8):	Demon do tunelowania IPv6
Name:		miredo
Version:	1.1.5
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.remlab.net/files/miredo/archive/%{name}-%{version}.tar.bz2
# Source0-md5:	c339a7dd24a985157e5e6c0dfd175a75
URL:		http://www.simphalempin.com/dev/miredo/
BuildRequires:	judy-devel
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

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/miredo
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo/*.conf
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/miredo/client-hook
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man?/*.?*
