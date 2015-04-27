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
Version:        1.5
Release:        1%{?dist}

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
* Mon Apr 27 2015 Liam Bulkley <liam@fightingcrane.com> 1.5-1
- Merge branch 'master' of https://github.com/snwh/paper-icon-theme
  (liam@fightingcrane.com)
- More symlinks (hewittsamuel@gmail.com)
- Added icons. (hewittsamuel@gmail.com)
- Added a bunch of symlinks (hewittsamuel@gmail.com)
- Added some symlinks (hewittsamuel@gmail.com)
- Added some icons (hewittsamuel@gmail.com)
- Added icons. (hewittsamuel@gmail.com)
- Added icons completed others. (hewittsamuel@gmail.com)

* Fri Apr 24 2015 Liam Bulkley <liam@fightingcrane.com> 1.4-1
- 

* Fri Apr 24 2015 Liam Bulkley <liam@fightingcrane.com> 1.3-1
- 

* Thu Apr 23 2015 Liam Bulkley <liam@fightingcrane.com> 1.2-1
- Merge branch 'master' of https://github.com/snwh/paper-icon-theme
  (liam@fightingcrane.com)
- Updated internet-mail (hewittsamuel@gmail.com)
- Added icons (hewittsamuel@gmail.com)
- Fixed rendering issues in vector icons (hewittsamuel@gmail.com)
- Re-rendered panel icons (hewittsamuel@gmail.com)
- Added symlinks for chrome beta & unstable (hewittsamuel@gmail.com)

* Sat Apr 11 2015 Liam Bulkley <liam@fightingcrane.com> 1.1-1
- Merge branch 'master' of https://github.com/snwh/paper-icon-theme
  (liam@fightingcrane.com)
- Fixed typo (hewittsamuel@gmail.com)
- Added 22px panel icons. (hewittsamuel@gmail.com)

* Tue Apr 07 2015 Liam Bulkley <liam@fightingcrane.com> 1.0-3
- Updated a few icons (hewittsamuel@gmail.com)

* Sun Apr 05 2015 Liam Bulkley <liam@fightingcrane.com> 1.0-2
- new package built with tito
titofied for copr
