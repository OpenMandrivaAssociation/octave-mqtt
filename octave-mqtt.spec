%global octpkg mqtt

Summary:	Basic Octave implementation of mqtt toolkit
Name:		octave-mqtt
Version:	0.0.3
Release:	1
License:	GPL-3.0-or-later
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/mqtt/
Source0:	https://downloads.sourceforge.net/project/octave-mqtt/v%{version}/octave-mqtt-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  libpaho-mqtt-c-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Basic Octave implementation of mqtt toolkit.

%files
%license COPYING
%doc NEWS README.md
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

