#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LVM2
Version  : 2.02.186
Release  : 93
URL      : https://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.02.186.tgz
Source0  : https://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.02.186.tgz
Summary  : lvm2 application library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: LVM2-bin = %{version}-%{release}
Requires: LVM2-config = %{version}-%{release}
Requires: LVM2-lib = %{version}-%{release}
Requires: LVM2-license = %{version}-%{release}
Requires: LVM2-man = %{version}-%{release}
Requires: LVM2-python = %{version}-%{release}
Requires: LVM2-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : ctags
BuildRequires : kmod
BuildRequires : libaio-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : ruby
BuildRequires : sed
BuildRequires : systemd-dev
BuildRequires : thin-provisioning-tools
Patch1: 0001-Fix-cache-dirs.patch
Patch2: 0002-Add-malloc_trim-call.patch
Patch3: 0003-Don-t-insert-version.patch
Patch4: 0004-remove-obsolete-udev-option.patch
Patch5: CVE-2020-8991.patch

%description
This tree contains the LVM2 and device-mapper tools and libraries.
For more information about LVM2 read the changelog in the WHATS_NEW file.
Installation instructions are in INSTALL.

%package bin
Summary: bin components for the LVM2 package.
Group: Binaries
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
Requires: LVM2-license = %{version}-%{release}

%description lib
lib components for the LVM2 package.


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

%description python3
python3 components for the LVM2 package.


%prep
%setup -q -n LVM2.2.02.186
cd %{_builddir}/LVM2.2.02.186
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583343373
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
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
--enable-udev_sync
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make unit-test

%install
export SOURCE_DATE_EPOCH=1583343373
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LVM2
cp %{_builddir}/LVM2.2.02.186/COPYING %{buildroot}/usr/share/package-licenses/LVM2/c14c50b6a56cc96c54353b985b104941ca8b86a3
cp %{_builddir}/LVM2.2.02.186/COPYING.BSD %{buildroot}/usr/share/package-licenses/LVM2/a0d7ec1f083b527a6fe3fee041d01eef016aa871
cp %{_builddir}/LVM2.2.02.186/COPYING.LIB %{buildroot}/usr/share/package-licenses/LVM2/caeb68c46fa36651acf592771d09de7937926bb3
cp %{_builddir}/LVM2.2.02.186/tools/license.inc %{buildroot}/usr/share/package-licenses/LVM2/7c3f71e2821b69adeaef9563e74971395dd94eef
%make_install install_systemd_units install_tmpfiles_configuration
## Remove excluded files
rm -f %{buildroot}/etc/lvm/lvm.conf
rm -f %{buildroot}/etc/lvm/lvmlocal.conf
rm -f %{buildroot}/etc/lvm/profile/command_profile_template.profile
rm -f %{buildroot}/etc/lvm/profile/metadata_profile_template.profile
rm -f %{buildroot}/etc/lvm/profile/thin-generic.profile
rm -f %{buildroot}/etc/lvm/profile/thin-performance.profile
rm -f %{buildroot}/usr/lib/systemd/system/lvm2-monitor.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/bin/lvmconf
/usr/bin/lvmconfig
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
/usr/lib/udev/rules.d/95-dm-notify.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libdevmapper-event.h
/usr/include/libdevmapper.h
/usr/include/lvm2app.h
/usr/include/lvm2cmd.h
/usr/lib64/pkgconfig/devmapper-event.pc
/usr/lib64/pkgconfig/devmapper.pc
/usr/lib64/pkgconfig/lvm2app.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/lvmetad
/usr/lib/systemd/system/blk-availability.service
/usr/lib/systemd/system/dm-event.service
/usr/lib/systemd/system/dm-event.socket
/usr/lib/systemd/system/lvm2-lvmetad.service
/usr/lib/systemd/system/lvm2-lvmetad.socket
/usr/lib/systemd/system/lvm2-pvscan@.service
/usr/lib/udev/rules.d/69-dm-lvm-metad.rules

%files extras-lib
%defattr(-,root,root,-)
/usr/lib64/libdevmapper-event-lvm2.so.2.02
/usr/lib64/libdevmapper-event.so.1.02
/usr/lib64/libdevmapper.so.1.02

%files lib
%defattr(-,root,root,-)
/usr/lib64/device-mapper/libdevmapper-event-lvm2mirror.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2raid.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2snapshot.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2thin.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2vdo.so
/usr/lib64/libdevmapper-event-lvm2.so
/usr/lib64/libdevmapper-event-lvm2mirror.so
/usr/lib64/libdevmapper-event-lvm2raid.so
/usr/lib64/libdevmapper-event-lvm2snapshot.so
/usr/lib64/libdevmapper-event-lvm2thin.so
/usr/lib64/libdevmapper-event-lvm2vdo.so
/usr/lib64/libdevmapper-event.so
/usr/lib64/libdevmapper.so
/usr/lib64/liblvm2app.so
/usr/lib64/liblvm2app.so.2.2
/usr/lib64/liblvm2cmd.so
/usr/lib64/liblvm2cmd.so.2.02

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LVM2/7c3f71e2821b69adeaef9563e74971395dd94eef
/usr/share/package-licenses/LVM2/a0d7ec1f083b527a6fe3fee041d01eef016aa871
/usr/share/package-licenses/LVM2/c14c50b6a56cc96c54353b985b104941ca8b86a3
/usr/share/package-licenses/LVM2/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/lvm.conf.5
/usr/share/man/man7/lvmcache.7
/usr/share/man/man7/lvmraid.7
/usr/share/man/man7/lvmreport.7
/usr/share/man/man7/lvmsystemid.7
/usr/share/man/man7/lvmthin.7
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
/usr/share/man/man8/lvmconf.8
/usr/share/man/man8/lvmconfig.8
/usr/share/man/man8/lvmdiskscan.8
/usr/share/man/man8/lvmdump.8
/usr/share/man/man8/lvmetad.8
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
