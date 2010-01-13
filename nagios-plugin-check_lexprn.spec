%define		plugin check_lexprn
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Plugin for checking the status of Lexmark printers
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania stanu drukarek Lexmark
Name:		nagios-plugin-check_lexprn
Version:	0.1
Release:	3
License:	GPL
Group:		Networking
Source0:	http://www.universalnet.at/projects/check_lexprn/%{plugin}-%{version}.tar.gz
# Source0-md5:	b2234770a61360957a2520f6c7e39bd3
Source1:	%{plugin}.conf
URL:		http://www.universalnet.at/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
Requires:	nagios-plugins-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_prefix}/lib/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins
%define		_noautoreq	'perl(utils)'

%description
check_lexprn is a Nagios plugin that can be used to monitor the status
of Lexmark printers.

%description -l pl.UTF-8
check_lexprn to wtyczka Nagiosa do monitorowania stanu drukarek
Lexmark.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{_plugindir}
sed -e 's,@plugindir@,%{_plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL.TXT
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{_plugindir}/%{plugin}
