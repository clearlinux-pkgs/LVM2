#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
Name     : LVM2
Version  : 2.03.22
Release  : 117
URL      : https://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.03.22.tgz
Source0  : https://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.03.22.tgz
Summary  : device-mapper event library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: LVM2-bin = %{version}-%{release}
Requires: LVM2-config = %{version}-%{release}
Requires: LVM2-lib = %{version}-%{release}
Requires: LVM2-libexec = %{version}-%{release}
Requires: LVM2-license = %{version}-%{release}
Requires: LVM2-man = %{version}-%{release}
Requires: LVM2-python = %{version}-%{release}
Requires: LVM2-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : dbus-python
BuildRequires : kmod
BuildRequires : libaio-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : python3-dev
BuildRequires : pyudev
BuildRequires : readline-dev
BuildRequires : ruby
BuildRequires : sed
BuildRequires : systemd-dev
BuildRequires : thin-provisioning-tools
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-cache-dirs.patch
Patch2: 0002-Add-malloc_trim-call.patch

%description
This tree contains the LVM2 and device-mapper tools and libraries.
This is development branch, for stable 2.02 release see stable-2.02 branch.

%package bin
Summary: bin components for the LVM2 package.
Group: Binaries
Requires: LVM2-libexec = %{version}-%{release}
Requires: LVM2-config = %{version}-%{release}
Requires: LVM2-license = %{version}-%{release}

%description bin
bin components for the LVM2 package.


%package config
Summary: config components for the LVM2 package.
Group: Default

%description config
config components for the LVM2 package.


%package dev
Summary: dev components for the LVM2 package.
Group: Development
Requires: LVM2-lib = %{version}-%{release}
Requires: LVM2-bin = %{version}-%{release}
Provides: LVM2-devel = %{version}-%{release}
Requires: LVM2 = %{version}-%{release}

%description dev
dev components for the LVM2 package.


%package extras
Summary: extras components for the LVM2 package.
Group: Default

%description extras
extras components for the LVM2 package.


%package extras-lib
Summary: extras-lib components for the LVM2 package.
Group: Default

%description extras-lib
extras-lib components for the LVM2 package.


%package lib
Summary: lib components for the LVM2 package.
Group: Libraries
Requires: LVM2-libexec = %{version}-%{release}
Requires: LVM2-license = %{version}-%{release}

%description lib
lib components for the LVM2 package.


%package libexec
Summary: libexec components for the LVM2 package.
Group: Default
Requires: LVM2-config = %{version}-%{release}
Requires: LVM2-license = %{version}-%{release}

%description libexec
libexec components for the LVM2 package.


%package license
Summary: license components for the LVM2 package.
Group: Default

%description license
license components for the LVM2 package.


%package man
Summary: man components for the LVM2 package.
Group: Default

%description man
man components for the LVM2 package.


%package python
Summary: python components for the LVM2 package.
Group: Default
Requires: LVM2-python3 = %{version}-%{release}
Provides: lvm2-python

%description python
python components for the LVM2 package.


%package python3
Summary: python3 components for the LVM2 package.
Group: Default
Requires: python3-core
Requires: pygobject-python3
Requires: pypi(dbus_python)
Requires: pypi(pyudev)

%description python3
python3 components for the LVM2 package.


%prep
%setup -q -n LVM2.2.03.22
cd %{_builddir}/LVM2.2.03.22
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a LVM2.2.03.22 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707086521
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --libdir=/usr/lib64 \
--sbindir=/usr/bin \
--with-usrlibdir=/usr/lib64 \
--with-default-locking-dir=/run/lock/lvm \
--with-default-run-dir=/run/lvm \
--with-systemdsystemunitdir=/usr/lib/systemd/system \
--enable-applib \
--enable-cmdlib \
--enable-dmeventd \
--enable-lvmetad \
--enable-pkgconfig \
--enable-python3-bindings \
--enable-testing \
--enable-udev_sync \
--enable-dbus-service
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --libdir=/usr/lib64 \
--sbindir=/usr/bin \
--with-usrlibdir=/usr/lib64 \
--with-default-locking-dir=/run/lock/lvm \
--with-default-run-dir=/run/lvm \
--with-systemdsystemunitdir=/usr/lib/systemd/system \
--enable-applib \
--enable-cmdlib \
--enable-dmeventd \
--enable-lvmetad \
--enable-pkgconfig \
--enable-python3-bindings \
--enable-testing \
--enable-udev_sync \
--enable-dbus-service
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make unit-test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707086521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LVM2
cp %{_builddir}/LVM2.%{version}/COPYING %{buildroot}/usr/share/package-licenses/LVM2/c14c50b6a56cc96c54353b985b104941ca8b86a3 || :
cp %{_builddir}/LVM2.%{version}/COPYING.BSD %{buildroot}/usr/share/package-licenses/LVM2/a0d7ec1f083b527a6fe3fee041d01eef016aa871 || :
cp %{_builddir}/LVM2.%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/LVM2/caeb68c46fa36651acf592771d09de7937926bb3 || :
pushd ../buildavx2/
%make_install_v3 install_systemd_units install_tmpfiles_configuration
popd
%make_install install_systemd_units install_tmpfiles_configuration
## Remove excluded files
rm -f %{buildroot}*/etc/lvm/lvm.conf
rm -f %{buildroot}*/etc/lvm/lvmlocal.conf
rm -f %{buildroot}*/etc/lvm/profile/command_profile_template.profile
rm -f %{buildroot}*/etc/lvm/profile/metadata_profile_template.profile
rm -f %{buildroot}*/etc/lvm/profile/thin-generic.profile
rm -f %{buildroot}*/etc/lvm/profile/thin-performance.profile
rm -f %{buildroot}*/usr/lib/systemd/system/lvm2-monitor.service
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dmeventd
/V3/usr/bin/dmsetup
/V3/usr/bin/lvm
/usr/bin/blkdeactivate
/usr/bin/dmeventd
/usr/bin/dmsetup
/usr/bin/dmstats
/usr/bin/fsadm
/usr/bin/lvchange
/usr/bin/lvconvert
/usr/bin/lvcreate
/usr/bin/lvdisplay
/usr/bin/lvextend
/usr/bin/lvm
/usr/bin/lvm_import_vdo
/usr/bin/lvmconfig
/usr/bin/lvmdevices
/usr/bin/lvmdiskscan
/usr/bin/lvmdump
/usr/bin/lvmsadc
/usr/bin/lvmsar
/usr/bin/lvreduce
/usr/bin/lvremove
/usr/bin/lvrename
/usr/bin/lvresize
/usr/bin/lvs
/usr/bin/lvscan
/usr/bin/pvchange
/usr/bin/pvck
/usr/bin/pvcreate
/usr/bin/pvdisplay
/usr/bin/pvmove
/usr/bin/pvremove
/usr/bin/pvresize
/usr/bin/pvs
/usr/bin/pvscan
/usr/bin/vgcfgbackup
/usr/bin/vgcfgrestore
/usr/bin/vgchange
/usr/bin/vgck
/usr/bin/vgconvert
/usr/bin/vgcreate
/usr/bin/vgdisplay
/usr/bin/vgexport
/usr/bin/vgextend
/usr/bin/vgimport
/usr/bin/vgimportclone
/usr/bin/vgimportdevices
/usr/bin/vgmerge
/usr/bin/vgmknodes
/usr/bin/vgreduce
/usr/bin/vgremove
/usr/bin/vgrename
/usr/bin/vgs
/usr/bin/vgscan
/usr/bin/vgsplit

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/lvm2.conf
/usr/lib/udev/rules.d/10-dm.rules
/usr/lib/udev/rules.d/11-dm-lvm.rules
/usr/lib/udev/rules.d/13-dm-disk.rules
/usr/lib/udev/rules.d/69-dm-lvm.rules
/usr/lib/udev/rules.d/95-dm-notify.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libdevmapper-event.h
/usr/include/libdevmapper.h
/usr/include/lvm2cmd.h
/usr/lib64/pkgconfig/devmapper-event.pc
/usr/lib64/pkgconfig/devmapper.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/lvmdbusd
/usr/lib/systemd/system/blk-availability.service
/usr/lib/systemd/system/dm-event.service
/usr/lib/systemd/system/dm-event.socket
/usr/lib/systemd/system/lvm2-lvmdbusd.service
/usr/share/dbus-1/system-services/com.redhat.lvmdbus1.service
/usr/share/dbus-1/system.d/com.redhat.lvmdbus1.conf

%files extras-lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdevmapper-event.so.1.02
/V3/usr/lib64/libdevmapper.so.1.02
/usr/lib64/libdevmapper-event.so.1.02
/usr/lib64/libdevmapper.so.1.02

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/device-mapper/libdevmapper-event-lvm2mirror.so
/V3/usr/lib64/device-mapper/libdevmapper-event-lvm2raid.so
/V3/usr/lib64/device-mapper/libdevmapper-event-lvm2snapshot.so
/V3/usr/lib64/device-mapper/libdevmapper-event-lvm2thin.so
/V3/usr/lib64/device-mapper/libdevmapper-event-lvm2vdo.so
/V3/usr/lib64/libdevmapper-event-lvm2.so.2.03
/V3/usr/lib64/liblvm2cmd.so.2.03
/usr/lib64/device-mapper/libdevmapper-event-lvm2mirror.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2raid.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2snapshot.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2thin.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2vdo.so
/usr/lib64/libdevmapper-event-lvm2.so
/usr/lib64/libdevmapper-event-lvm2.so.2.03
/usr/lib64/libdevmapper-event-lvm2mirror.so
/usr/lib64/libdevmapper-event-lvm2raid.so
/usr/lib64/libdevmapper-event-lvm2snapshot.so
/usr/lib64/libdevmapper-event-lvm2thin.so
/usr/lib64/libdevmapper-event-lvm2vdo.so
/usr/lib64/libdevmapper-event.so
/usr/lib64/libdevmapper.so
/usr/lib64/liblvm2cmd.so
/usr/lib64/liblvm2cmd.so.2.03

%files libexec
%defattr(-,root,root,-)
/usr/libexec/lvresize_fs_helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LVM2/a0d7ec1f083b527a6fe3fee041d01eef016aa871
/usr/share/package-licenses/LVM2/c14c50b6a56cc96c54353b985b104941ca8b86a3
/usr/share/package-licenses/LVM2/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/lvm.conf.5
/usr/share/man/man7/lvmautoactivation.7
/usr/share/man/man7/lvmcache.7
/usr/share/man/man7/lvmraid.7
/usr/share/man/man7/lvmreport.7
/usr/share/man/man7/lvmsystemid.7
/usr/share/man/man7/lvmthin.7
/usr/share/man/man7/lvmvdo.7
/usr/share/man/man8/blkdeactivate.8
/usr/share/man/man8/dmeventd.8
/usr/share/man/man8/dmsetup.8
/usr/share/man/man8/dmstats.8
/usr/share/man/man8/fsadm.8
/usr/share/man/man8/lvchange.8
/usr/share/man/man8/lvconvert.8
/usr/share/man/man8/lvcreate.8
/usr/share/man/man8/lvdisplay.8
/usr/share/man/man8/lvextend.8
/usr/share/man/man8/lvm-config.8
/usr/share/man/man8/lvm-dumpconfig.8
/usr/share/man/man8/lvm-fullreport.8
/usr/share/man/man8/lvm-lvpoll.8
/usr/share/man/man8/lvm.8
/usr/share/man/man8/lvm_import_vdo.8
/usr/share/man/man8/lvmconfig.8
/usr/share/man/man8/lvmdbusd.8
/usr/share/man/man8/lvmdevices.8
/usr/share/man/man8/lvmdiskscan.8
/usr/share/man/man8/lvmdump.8
/usr/share/man/man8/lvmsadc.8
/usr/share/man/man8/lvmsar.8
/usr/share/man/man8/lvreduce.8
/usr/share/man/man8/lvremove.8
/usr/share/man/man8/lvrename.8
/usr/share/man/man8/lvresize.8
/usr/share/man/man8/lvs.8
/usr/share/man/man8/lvscan.8
/usr/share/man/man8/pvchange.8
/usr/share/man/man8/pvck.8
/usr/share/man/man8/pvcreate.8
/usr/share/man/man8/pvdisplay.8
/usr/share/man/man8/pvmove.8
/usr/share/man/man8/pvremove.8
/usr/share/man/man8/pvresize.8
/usr/share/man/man8/pvs.8
/usr/share/man/man8/pvscan.8
/usr/share/man/man8/vgcfgbackup.8
/usr/share/man/man8/vgcfgrestore.8
/usr/share/man/man8/vgchange.8
/usr/share/man/man8/vgck.8
/usr/share/man/man8/vgconvert.8
/usr/share/man/man8/vgcreate.8
/usr/share/man/man8/vgdisplay.8
/usr/share/man/man8/vgexport.8
/usr/share/man/man8/vgextend.8
/usr/share/man/man8/vgimport.8
/usr/share/man/man8/vgimportclone.8
/usr/share/man/man8/vgimportdevices.8
/usr/share/man/man8/vgmerge.8
/usr/share/man/man8/vgmknodes.8
/usr/share/man/man8/vgreduce.8
/usr/share/man/man8/vgremove.8
/usr/share/man/man8/vgrename.8
/usr/share/man/man8/vgs.8
/usr/share/man/man8/vgscan.8
/usr/share/man/man8/vgsplit.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
