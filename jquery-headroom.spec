%define		plugin	headroom
Summary:	Give your pages some headroom. Hide your header until you need it
Name:		jquery-%{plugin}
Version:	0.7.0
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/WickyNilliams/headroom.js/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e7959001926fb7f708f69c17e5a19174
URL:		http://wicky.nillia.ms/headroom.js/
BuildRequires:	unzip
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Headroom.js is a lightweight, high-performance JS widget (with no
dependencies!) that allows you to react to the user's scroll. The
header on this site is a living example, it slides out of view when
scrolling down and slides back in when scrolling up.

%prep
%setup -qc
mv headroom.js-%{version}/* .

%build
cat dist/headroom.js dist/jQuery.headroom.js > jquery.%{plugin}.js
cat dist/headroom.min.js dist/jQuery.headroom.min.js > jquery.%{plugin}.min.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
