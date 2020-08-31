#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eternalegypt
Version  : 0.0.12
Release  : 16
URL      : https://files.pythonhosted.org/packages/3b/e3/07ab59d0a12555b58ad8e4bea0466eff3c564172d7d1f0fd64117b61afaf/eternalegypt-0.0.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/e3/07ab59d0a12555b58ad8e4bea0466eff3c564172d7d1f0fd64117b61afaf/eternalegypt-0.0.12.tar.gz
Summary  : Netgear LTE modem API
Group    : Development/Tools
License  : MIT
Requires: eternalegypt-license = %{version}-%{release}
Requires: eternalegypt-python = %{version}-%{release}
Requires: eternalegypt-python3 = %{version}-%{release}
Requires: aiohttp
Requires: attrs
Requires: flatten_json
BuildRequires : aiohttp
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : flatten_json

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
Provides: pypi(eternalegypt)
Requires: pypi(aiohttp)
Requires: pypi(attrs)

%description python3
python3 components for the eternalegypt package.


%prep
%setup -q -n eternalegypt-0.0.12
cd %{_builddir}/eternalegypt-0.0.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598908885
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eternalegypt
cp %{_builddir}/eternalegypt-0.0.12/LICENSE.txt %{buildroot}/usr/share/package-licenses/eternalegypt/1e516e92e435cf640c534f48416dca1ddd6cefb7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eternalegypt/1e516e92e435cf640c534f48416dca1ddd6cefb7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
