#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	IPv6 Tunneling daemon
Summary(pl):	-
Name:		miredo
Version:	0.8.0
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://people.via.ecp.fr/~rem/miredo/v0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	326664cb9af10a38806149b7bd565340
URL:		http://www.simphalempin.com/dev/miredo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miredo is an open-source Teredo IPv6 tunneling software, for Linux and
the BSD operating systems. It includes functionnal implementations of
all components of the Teredo specification (client, relay and server).
It is meant to provide IPv6 connectivity even from behind NAT devices.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/miredo-server.conf-dist
%{_sysconfdir}/miredo.conf
%attr(755,root,root) %{_sbindir}/miredo
%attr(755,root,root) %{_sbindir}/miredo-server
%{_mandir}/man5/miredo-server.conf.5*
%{_mandir}/man5/miredo.conf.5*
%{_mandir}/man8/miredo-server.8*
%{_mandir}/man8/miredo.8*
