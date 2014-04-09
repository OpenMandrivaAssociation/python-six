%define	oname	six

Name:		python-%{oname}
Version:	1.6.1
Release:	1
Summary:	Python 2 and 3 compatibility utilities

Source0:	http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/six/
BuildArch:	noarch
BuildRequires:  python-devel

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports Python 2.4+.

Online documentation is at http://packages.python.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also
be found there.

%package -n python3-six
Summary: %{summary} / Python 3 library

BuildRequires: python3-devel

%description -n python3-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

%prep
%setup -qc 
mv %{oname}-%{version} python2
cp -a python2 python3

%build
pushd python2
python setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
python setup.py install --root=%{buildroot}
popd

pushd python3
python3 setup.py install --root=%{buildroot}
popd

%files
%doc python2/LICENSE python2/README python3/documentation/index.rst
%{py_puresitedir}/*

%files -n python3-six
%doc python3/LICENSE python3/README python2/documentation/index.rst
%{py3_puresitedir}/*

