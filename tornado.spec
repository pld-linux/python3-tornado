Summary:	Scalable, non-blocking web server and tools
Name:		tornado
Version:	2.3.0
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/HTTP
Source0:	https://github.com/downloads/facebook/tornado/%{name}-%{version}.tar.gz
# Source0-md5:	490ccc2da9d6de9c37c7df05c1197ac5
URL:		http://ipython.org
BuildRequires:	python3-devel
BuildRequires:	python3-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python3-%{mname} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools that power FriendFeed. The FriendFeed application is
written using a web framework that looks a bit like web.py or Google's
webapp, but with additional tools and optimizations to take advantage
of the underlying non-blocking infrastructure.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python3 ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%defattr(644,root,root,755)
%doc docs/README.txt
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/*.egg-info
