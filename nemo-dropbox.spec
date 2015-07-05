Summary:    Dropbox extension for nemo
Name:       nemo-dropbox
Version:    2.6.0
Release:    1%{?dist}
License:    GPLv2+ and LGPLv2+ and MIT
Group:      User Interface/Desktops
URL:        http://cinnamon.linuxmint.com
# To generate tarball
# wget https://github.com/linuxmint/nemo-extensions/tarball/%%{_internal_version} -O nemo-extensions-2.6.x.git%%{_internal_version}.tar.gz
#Source0:   http://leigh123linux.fedorapeople.org/pub/nemo-extensions/source/nemo-extensions-2.6.x.git%%{_internal_version}.tar.gz
Source0:    http://leigh123linux.fedorapeople.org/pub/nemo-extensions/source/nemo-extensions-2.6.x.tar.gz

ExclusiveArch:  i686 x86_64

BuildRequires:  nemo-devel
BuildRequires:  python-docutils
BuildRequires:  autoconf
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
%setup -q -n nemo-extensions-2.6.x

%build
pushd nemo-dropbox
autoreconf -fi
%configure
make %{?_smp_mflags}
popd

%install
pushd nemo-dropbox
%{make_install}
popd

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

rm -rf ${RPM_BUILD_ROOT}%{_bindir}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc nemo-dropbox/{AUTHORS,ChangeLog,COPYING,NEWS,README}
%{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so


%changelog
* Sun Jul 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0

* Wed Jan 07 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- use internal version
- add ExclusiveArch

* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-2
- add requires dropbox

* Tue Dec 09 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-1
- First build

