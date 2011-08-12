%define	oname	six

Name:		python-%{oname}
Version:	1.0.0
Release:	1
Summary:	Python 2 and 3 compatibility utilities
Source0:	http://pypi.python.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz
License:	UNKNOWN
Group:		Development/Libraries
Url:		http://pypi.python.org/pypi/six/
BuildArch:	noarch

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports Python 2.4+.

Online documentation is at http://packages.python.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also be
found there.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README
%{py_puresitedir}/six.py*
%{py_puresitedir}/six*.egg-info

%changelog
* Thu Oct 21 2010 Alexandre Lissy <alissy@mandriva.com> 1.0.0-1
- Initial release
