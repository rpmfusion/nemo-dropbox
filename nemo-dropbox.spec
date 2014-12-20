Summary:    Dropbox extension for nemo
Name:       nemo-dropbox
Version:    2.4.x
Release:    2%{?dist}
License:    GPLv2+ and LGPLv2+ and MIT
Group:      User Interface/Desktops
URL:        http://cinnamon.linuxmint.com
# To generate tarball
# wget https://github.com/linuxmint/nemo-extensions/tarball/%%{_internal_version} -O nemo-extensions-%%{version}.git%%{_internal_version}.tar.gz
#Source0:   http://leigh123linux.fedorapeople.org/pub/nemo-extensions/source/nemo-extensions-%%{version}.git%%{_internal_version}.tar.gz
Source0:    http://leigh123linux.fedorapeople.org/pub/nemo-extensions/source/nemo-extensions-%{version}.tar.gz


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
%setup -q -n nemo-extensions-%{version}

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
* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-2
- add requires dropbox

* Tue Dec 09 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-1
- First build

