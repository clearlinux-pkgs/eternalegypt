#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eternalegypt
Version  : 0.0.5
Release  : 1
URL      : https://github.com/amelchio/eternalegypt/archive/v0.0.5.tar.gz
Source0  : https://github.com/amelchio/eternalegypt/archive/v0.0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: eternalegypt-license = %{version}-%{release}
Requires: eternalegypt-python = %{version}-%{release}
Requires: eternalegypt-python3 = %{version}-%{release}
Requires: aiohttp
Requires: attrs
BuildRequires : aiohttp
BuildRequires : attrs
BuildRequires : buildreq-distutils3

%description
# Eternal Egypt
This library piggybacks on the web interface of Netgear LTE modems to provide a simple async Python 3 API.

%package license
Summary: license components for the eternalegypt package.
Group: Default

%description license
license components for the eternalegypt package.


%package python
Summary: python components for the eternalegypt package.
Group: Default
Requires: eternalegypt-python3 = %{version}-%{release}

%description python
python components for the eternalegypt package.


%package python3
Summary: python3 components for the eternalegypt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the eternalegypt package.


%prep
%setup -q -n eternalegypt-0.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541745834
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eternalegypt
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/eternalegypt/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eternalegypt/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
