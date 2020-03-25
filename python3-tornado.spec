#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# tornado tests [use network]

%define		module	tornado
Summary:	Web framework and asynchronous networking library
Summary(pl.UTF-8):	Szkielet WWW i asynchroniczna biblioteka sieciowa
Name:		python3-tornado
Version:	6.0.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tornado/
Source0:	https://files.pythonhosted.org/packages/source/t/tornado/tornado-%{version}.tar.gz
# Source0-md5:	cf39425f3d7eba9a54287f3e795a2f23
URL:		http://www.tornadoweb.org/
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
# SO_REUSEPORT option
BuildRequires:	uname(release) >= 3.9
BuildRequires:	python3-twisted
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with doc}
BuildRequires:	python3-sphinxcontrib-asyncio
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-twisted
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it
ideal for long polling, WebSockets, and other applications that
require a long-lived connection to each user.

%description -l pl.UTF-8
Tornado to szkielet WWW oraz asynchroniczna biblioteka sieciowa dla
Pythona, oryginalnie powstałe w FriendFeed. Dzięki użyciu
nieblokującego sieciowego we/wy, Tornado może się skalować do
dziesiątek tysięcy otwartych połączeń, co czyni go idealnym do
zastosowań z długim pobieraniem, WebSockets i innych wymagających
długotrwałego połączenia z każdym użytkownikiem.

%package apidocs
Summary:	API documentation for Python tornado module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona tornado
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for Python tornado module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona tornado.

%prep
%setup -q -n tornado-%{version}

# non-Linux
%{__rm} tornado/platform/windows.py

%build
TORNADO_EXTENSION=1 \
%py3_build

%if %{with tests}
cd build-3/lib*
%{__python3} -m tornado.test.runtests
cd ../..
%endif

%if %{with doc}
sphinx-build-3 -b html -n -d docs/build/doctrees docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install
# just tornado tests with their data
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/tornado/test

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/tornado
%attr(755,root,root) %{py3_sitedir}/tornado/speedups.cpython-*.so
%{py3_sitedir}/tornado/*.py
%{py3_sitedir}/tornado/py.typed
%{py3_sitedir}/tornado/platform
%{py3_sitedir}/tornado/__pycache__
%{py3_sitedir}/tornado-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_images,_modules,_static,guide,releases,*.html,*.js}
%endif
