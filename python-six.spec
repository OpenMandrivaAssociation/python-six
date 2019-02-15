%define	oname six

Name:		python-%{oname}
Version:	1.12.0
Release:	1
Summary:	Python 2 and 3 compatibility utilities
Source0:	http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/six/
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
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

%package -n python2-six
Summary:	%{summary} / Python 2 library
Group:		Development/Python

%description -n python2-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

%prep
%setup -qc
mv %{oname}-%{version} python2
cp -a python2 python3

%build
cd python2
%{__python2} setup.py build
cd -

cd python3
%{__python} setup.py build
cd -

%install
cd python2
%{__python2} setup.py install --root=%{buildroot}
cd -

cd python3
%{__python} setup.py install --root=%{buildroot}
cd -

%files
%doc python3/LICENSE python3/documentation/index.rst
%{py_puresitedir}/six-%{version}-*.egg-info
%{py_puresitedir}/six.py*
%{py_puresitedir}/__pycache__/*.pyc

%files -n python2-six
%doc python2/LICENSE python2/documentation/index.rst
%{py2_puresitedir}/six-%{version}-*.egg-info
%{py2_puresitedir}/six.py*
