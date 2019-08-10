Summary:    Dropbox extension for nemo
Name:       nemo-dropbox
Version:    4.0.0
Release:    5%{?dist}
License:    GPLv2+ and LGPLv2+ and MIT
URL:        https://github.com/linuxmint/nemo-extensions
Source0:    %url/archive/%{version}.tar.gz#/nemo-extensions-%{version}.tar.gz
Patch0:     use_python2.patch

ExclusiveArch:  i686 x86_64

BuildRequires:  nemo-devel
BuildRequires:  python2-docutils
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel

Requires:       dropbox >= 1:2.10.0

%description
Dropbox extension for nemo file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%autosetup -p1 -n nemo-extensions-%{version}

%build
pushd nemo-dropbox
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build V=1
popd

%install
pushd nemo-dropbox
%make_install
popd

#Remove libtool archives.
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f

rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}

%ldconfig_scriptlets

%files
%doc nemo-dropbox/{AUTHORS,ChangeLog,NEWS,README}
%license nemo-dropbox/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so


%changelog
* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 4.0.0-4
- exclude archs again

* Sun Apr 07 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 4.0.0-3
- build for all archs

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8.0-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Tue Jul 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-2
- Fix build for f29 python changes

* Tue May 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0

* Sun Aug 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- rebuilt

* Fri Jun 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0

* Sun Jul 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0

* Wed Jan 07 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- use internal version
- add ExclusiveArch

* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-2
- add requires dropbox

* Tue Dec 09 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-1
- First build

