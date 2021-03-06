Summary:	Application Framework for Python 3 and PyQt
Summary(pl.UTF-8):	Szkielet dla aplikacji opartych na Pythonie 3 i PyQt
Name:		python3-dip
Version:	0.4.4
Release:	1
License:	GPL v2 with exception or commercial
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/dip/dip-gpl-%{version}.tar.gz
# Source0-md5:	a53944cfc1e915ae337fec7106bd0651
URL:		http://www.riverbankcomputing.com/static/Docs/dip/
BuildRequires:	python3-devel >= 3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
Requires:	python3-PyQt4 >= 4.7.5
Requires:	QtGui >= 4.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dip is an application framework for Python and PyQt.

This version supports Python 3.x.

%description -l pl.UTF-8
dip to szkielet dla aplikacji opartych na Pythonie i PyQt.

Ta wersja jest przeznaczona dla Pythona 3.x.

%prep
%setup -q -n dip-gpl-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

# distinguish from python 2 version
mv $RPM_BUILD_ROOT%{_bindir}/dip-automate{,-3}
mv $RPM_BUILD_ROOT%{_bindir}/dip-builder{,-3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog GPL-Exception.txt LICENSE-Commercial.txt NEWS README doc/_build/html
%attr(755,root,root) %{_bindir}/dip-automate-3
%attr(755,root,root) %{_bindir}/dip-builder-3
%{py3_sitescriptdir}/dip
%{py3_sitescriptdir}/dip_gpl-%{version}-py*.egg-info
