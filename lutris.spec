%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           lutris
Version:        0.3.6.3
Release:        3%{?dist}
Summary:        Install and play any video game easily

License:        GPLv3+
URL:            http://lutris.net
Source0:        http://lutris.net/releases/lutris_%{version}.tar.gz

BuildArch:      noarch

%if 0%{?fedora_version}

BuildRequires:  python-devel, pyxdg

Requires:       pygobject3, pyxdg, PyYAML, gvfs, glib-networking

%endif
%if 0%{?rhel_version} || 0%{?centos_version}

BuildRequires:  python-devel, python3-xdg

Requires:       pygobject3, python3-xdg, PyYAML, gvfs, glib-networking

%endif
%if 0%{?suse_version}

BuildRequires:  python-devel, python-xdg

Requires:		python-gobject, python-gtk, python-xdg, python-PyYAML, gvfs-backends, glib-networking

#!BuildIgnore: rpmlint-mini

%endif

%if 0%{?suse_version}
BuildRequires: update-desktop-files
%endif
# Common build dependencies
BuildRequires:	desktop-file-utils


%description
Install and play any video game easily
 Lutris is a gaming platform for GNU/Linux. Its goal is to make
 gaming on Linux as easy as possible by taking care of installing
 and setting up the game for the user. The only thing you have to
 do is play the game. It aims to support every game that is playable
 on Linux.

%prep
%setup -n %{name} -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

#desktop icon
#rm %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version}
%suse_update_desktop_file -r -i %{name} Network FileTransfer
%endif

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%files
%defattr(-,root,root)
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_bindir}/lutris
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/apps.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/lutris/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*
%{python_sitelib}/%{name}-%{version}-py2.7.egg-info
%{python_sitelib}/lutris/


%changelog
* Thu Oct 30 2014 Mathieu Comandon <strycore@gmail.com> - 0.3.6-1
- Bump to version 0.3.6
- Add OpenSuse compatibility (contribution by @malkavi)

* Fri Sep 12 2014 Mathieu Comandon <strycore@gmail.com> - 0.3.5-1
- Bump version to 0.3.5

* Thu Aug 14 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-3
- Edited Requires to include pygobject3.

* Wed Jun 04 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-2
- Changed build and install step based on template generated by
  rpmdev-newspec.
- Added Requires.
- Ensure package can be built using mock.

* Tue Jun 03 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-1
- Initial version of the package

