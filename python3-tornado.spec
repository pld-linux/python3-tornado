%define	module	tornado
Summary:	Scalable, non-blocking web server and tools
Name:		python3-tornado
Version:	2.3
Release:	1
License:	Apache v2.0
Group:          Libraries/Python
Source0:	https://github.com/downloads/facebook/tornado/%{module}-%{version}.tar.gz
# Source0-md5:	810c3ecd425924fbf0aa1fa040f93ad1
URL:		http://ipython.org
BuildRequires:	python3-devel
BuildRequires:	python3-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools that power FriendFeed. The FriendFeed application is
written using a web framework that looks a bit like web.py or Google's
webapp, but with additional tools and optimizations to take advantage
of the underlying non-blocking infrastructure.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python3 ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*.egg-info
