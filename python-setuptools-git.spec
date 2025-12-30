Name:		python-setuptools-git
Version:	1.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools-git/setuptools-git-%{version}.tar.gz
Summary:	Setuptools revision control system plugin for Git
URL:		https://pypi.org/project/setuptools-git/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Setuptools revision control system plugin for Git

%files
%{py_sitedir}/setuptools_git
%{py_sitedir}/setuptools_git-*.*-info
