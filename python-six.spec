%define	oname six

Name:		python-%{oname}
Version:	1.17.0
Release:	2
Summary:	Python 2 and 3 compatibility utilities
Source0:	https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/six/
BuildArch:	noarch
BuildRequires:	python
BuildSystem:	python
# For bootstrapping -- this is usually autodetected, but to avoid circular build
# dependencies, six needs to be buildable before packaging is built.
Provides:	python%{pyver}dist(six) = %{version}

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports Python 2.4+.

Online documentation is at http://packages.python.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also
be found there.

%files
%{py_puresitedir}/six-%{version}-*.egg-info
%{py_puresitedir}/six.py*
%{py_puresitedir}/__pycache__/six.*
