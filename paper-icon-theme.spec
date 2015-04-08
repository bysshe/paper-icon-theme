# Spec file for package paper-icon-theme
#
# Copyright (c) 2015 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:           paper-icon-theme
Version:        1.0
Release:        3%{?dist}

Summary:        Paper Icon theme
License:    CC-BY-SA-4.0

Url:        http://snwh.org/paper-icon-theme
Source:        %{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme, gnome-icon-theme
BuildArch:      noarch


%description
Icon theme for the Paper-Gtk-theme, inspired by Google's Material design.

%prep
%setup -q

# Delete dead icon symlinks
find -L . -type l -delete

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Paper/ $RPM_BUILD_ROOT%{_datadir}/icons/

%files
%doc AUTHORS LICENSE
%{_datadir}/icons/Paper/

%changelog
* Tue Apr 07 2015 Liam Bulkley <liam@fightingcrane.com> 1.0-3
- Updated a few icons (hewittsamuel@gmail.com)

* Sun Apr 05 2015 Liam Bulkley <liam@fightingcrane.com> 1.0-2
- new package built with tito
titofied for copr
