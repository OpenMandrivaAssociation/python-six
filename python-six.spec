%define	oname six

Name:		python-%{oname}
Version:	1.16.0
Release:	7
Summary:	Python 2 and 3 compatibility utilities
Source0:	https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/six/
BuildArch:	noarch
Provides:	python3egg(six)
BuildSystem:	python

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports Python 2.4+.

Online documentation is at http://packages.python.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also
be found there.

%prep
%autosetup -p1 -n six-%{version}

%files
%{py_puresitedir}/six-%{version}-*.egg-info
%{py_puresitedir}/six.py*
