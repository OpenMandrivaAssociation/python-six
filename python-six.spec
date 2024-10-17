%define	oname six

Name:		python-%{oname}
Version:	1.16.0
Release:	6
Summary:	Python 2 and 3 compatibility utilities
Source0:	https://files.pythonhosted.org/packages/71/39/171f1c67cd00715f190ba0b100d606d440a28c93c7714febeca8b79af85e/six-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/six/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
Provides:	python3egg(six)

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
%setup -n six-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/six-%{version}-*.egg-info
%{py_puresitedir}/six.py*
