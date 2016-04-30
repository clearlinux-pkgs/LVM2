Name     : LVM2
Version  : 2.02.151
Release  : 57
URL      : http://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.02.151.tgz
Source0  : http://mirrors.kernel.org/sourceware/lvm2/releases/LVM2.2.02.151.tgz
Summary  : lvm2 application library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: LVM2-bin
Requires: LVM2-python
Requires: LVM2-config
Requires: LVM2-lib
Requires: LVM2-doc
BuildRequires : kmod
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : python-dev
BuildRequires : readline-dev
BuildRequires : ruby
BuildRequires : sed
BuildRequires : systemd-dev
Patch1: debian-dirs.patch
Patch2: 0001-use-ruby-newer-than-1.9.patch
Patch3: trim.patch

%description
This tree contains the LVM2 and device-mapper tools and libraries.
For more information about LVM2 read the changelog in the WHATS_NEW file.
Installation instructions are in INSTALL.

%package bin
Summary: bin components for the LVM2 package.
Group: Binaries
Requires: LVM2-config

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
Requires: LVM2-lib
Requires: LVM2-bin
Provides: LVM2-devel

%description dev
dev components for the LVM2 package.


%package doc
Summary: doc components for the LVM2 package.
Group: Documentation

%description doc
doc components for the LVM2 package.


%package extras
Summary: extras components for the LVM2 package.
Group: Default

%description extras
extras components for the LVM2 package.


%package lib
Summary: lib components for the LVM2 package.
Group: Libraries
Requires: LVM2-config

%description lib
lib components for the LVM2 package.

%package lib-extra
Summary: lib components for the LVM2 package.
Group: Libraries

%description lib-extra
lib components for the LVM2 package.


%package python
Summary: python components for the LVM2 package.
Group: Default
Provides: lvm2-python

%description python
python components for the LVM2 package.


%prep
%setup -q -n LVM2.2.02.151
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="$CFLAGS -ffunction-sections -Os "
export FCFLAGS="$CFLAGS -ffunction-sections -Os "
export FFLAGS="$CFLAGS -ffunction-sections -Os "
export CXXFLAGS="$CXXFLAGS -ffunction-sections -Os "
%configure --disable-static --enable-applib \
--enable-cmdlib \
--enable-pkgconfig \
--enable-dmeventd \
--enable-lvmetad \
--enable-testing \
--enable-udev_sync \
--sbindir=/usr/bin \
--enable-python2-bindings \
--libdir=/usr/lib64 \
--with-usrlibdir=/usr/lib64 \
--with-default-run-dir=/run/lvm \
--with-default-locking-dir=/run/lock/lvm \
--with-systemdsystemunitdir=/usr/lib/systemd/system
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make unit-test memcheck

%install
rm -rf %{buildroot}
%make_install install install_systemd_units install_tmpfiles_configuration
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/sysinit.target.wants
ln -s ../blk-availability.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/blk-availability.service
ln -s ../lvm2-monitor.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/lvm2-monitor.service
ln -s ../lvm2-lvmetad.socket %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/lvm2-lvmetad.socket
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../dm-event.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/dm-event.socket
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/lvmetad
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
/usr/bin/lvmchange
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
%exclude /usr/lib/systemd/system/blk-availability.service
%exclude /usr/lib/systemd/system/dm-event.service
%exclude /usr/lib/systemd/system/dm-event.socket
%exclude /usr/lib/systemd/system/lvm2-lvmetad.service
%exclude /usr/lib/systemd/system/lvm2-lvmetad.socket
%exclude /usr/lib/systemd/system/lvm2-monitor.service
%exclude /usr/lib/systemd/system/lvm2-pvscan@.service
%exclude /usr/lib/systemd/system/sockets.target.wants/dm-event.socket
%exclude /usr/lib/systemd/system/sysinit.target.wants/blk-availability.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/lvm2-lvmetad.socket
%exclude /usr/lib/systemd/system/sysinit.target.wants/lvm2-monitor.service
%exclude /usr/lib/udev/rules.d/69-dm-lvm-metad.rules
/usr/lib/tmpfiles.d/lvm2.conf
/usr/lib/udev/rules.d/10-dm.rules
/usr/lib/udev/rules.d/11-dm-lvm.rules
/usr/lib/udev/rules.d/13-dm-disk.rules
/usr/lib/udev/rules.d/95-dm-notify.rules

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/lvmetad
/usr/lib/systemd/system/blk-availability.service
/usr/lib/systemd/system/dm-event.service
/usr/lib/systemd/system/dm-event.socket
/usr/lib/systemd/system/lvm2-lvmetad.service
/usr/lib/systemd/system/lvm2-lvmetad.socket
/usr/lib/systemd/system/lvm2-monitor.service
/usr/lib/systemd/system/lvm2-pvscan@.service
/usr/lib/systemd/system/sockets.target.wants/dm-event.socket
/usr/lib/systemd/system/sysinit.target.wants/blk-availability.service
/usr/lib/systemd/system/sysinit.target.wants/lvm2-lvmetad.socket
/usr/lib/systemd/system/sysinit.target.wants/lvm2-monitor.service
/usr/lib/udev/rules.d/69-dm-lvm-metad.rules

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libdevmapper.so.*
/usr/lib64/*.so.*
/usr/lib64/device-mapper/libdevmapper-event-lvm2mirror.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2raid.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2snapshot.so
/usr/lib64/device-mapper/libdevmapper-event-lvm2thin.so

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

%files lib-extra
/usr/lib64/libdevmapper.so.*
