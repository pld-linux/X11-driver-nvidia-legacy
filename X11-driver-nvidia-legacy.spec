#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# without kernel packages
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

%if %{without kernel}
%undefine	with_dist_kernel
%endif
%if "%{_alt_kernel}" != "%{nil}"
%undefine	with_userspace
%endif
%if %{without userspace}
# nothing to be placed to debuginfo package
%define		_enable_debug_packages	0
%endif

%define		oldname 	X11-driver-nvidia
%define		pname	X11-driver-nvidia-legacy
%define		rel	2
Summary:	Linux Drivers for nVidia TNT/TNT2/GF/old GF2/Quadro Chips
Summary(pl.UTF-8):	Sterowniki do kart graficznych nVidia TNT/TNT2/GeForce/old GF2/Quadro
Name:		%{pname}%{_alt_kernel}
Version:	71.86.04
Release:	%{rel}
License:	nVidia Binary
Group:		X11
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{version}/NVIDIA-Linux-x86-%{version}-pkg1.run
# Source0-md5:	25bab42ae5295fc5b4baf01a774da25e
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}-pkg2.run
# Source1-md5:	a970dc3f2d8938472027b5a60db39b69
Source2:	%{oldname}-settings.desktop
Source3:	%{oldname}-xinitrc.sh
Patch0:		%{pname}-gcc34.patch
Patch1:		%{pname}-GL.patch
Patch2:		%{pname}-verbose.patch
URL:		http://www.nvidia.com/object/unix.html
%if %{with kernel}
BuildRequires:	%{kgcc_package}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.7}
BuildRequires:	rpmbuild(macros) >= 1.452
%endif
BuildRequires:	sed >= 4.0
BuildConflicts:	XFree86-nvidia
Requires:	X11-Xserver
Requires:	X11-libs >= 6.7.0
Requires:	X11-modules >= 6.7.0
Provides:	X11-OpenGL-core
Provides:	X11-OpenGL-libGL
Provides:	XFree86-OpenGL-core
Provides:	XFree86-OpenGL-libGL
Obsoletes:	%{oldname} < 1.0.7174
Obsoletes:	Mesa
Obsoletes:	Mesa-libGL
Obsoletes:	X11-OpenGL-core
Obsoletes:	X11-OpenGL-libGL
Obsoletes:	XFree86-OpenGL-core
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%ifarch %{x8664}
%define		_libdir32	%{_prefix}/lib
%endif

%description
This driver set adds improved 2D functionality to the Xorg X server as
well as high performance OpenGL acceleration, AGP support, support for
most flat panels, and multiple monitor support.

Hardware: nVidia TNT, TNT2, GeForce, old GeForce2 or Quadro based
graphics accelerator. New GeForce2, GeForce3 and GeForce4 adapters are
supported by X11-driver-nvidia package. The nVidia NV1 and RIVA
128/128ZX chips are supported in the base Xorg or XFree86 install and
are not supported by this driver set.

%description -l pl.UTF-8
Usprawnione sterowniki dla kart graficznych nVidia do serwera X dające
wysokowydajną akcelerację OpenGL, obsługę AGP i wiele monitorów.

Obsługują karty nVidia TNT/TNT2/GeForce/stare GeForce2/Quadro do
serwera Xorg. Dla kart GF2 (nowych), GF3 i GF4 jest pakiet
X11-driver-nvidia. Karty nVidia NV1 i Riva 128/128ZX są obsługiwane
przez sterownik nv z pakietów Xorg lub XFree86 - NIE są obsługiwane
przez ten pakiet.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl.UTF-8):	Pliki nagłówkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{pname} = %{version}-%{release}
Provides:	OpenGL-devel-base
Obsoletes:	%{oldname}-devel < 1.0.7174
Obsoletes:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	%{oldname}-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
Base headers (only gl?.h) for OpenGL for X11R6 for nvidia drivers.

%description devel -l pl.UTF-8
Podstawowe pliki nagłówkowe (tylko gl?.h) OpenGL dla systemu X11R6 dla
sterowników nvidii.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl.UTF-8):	Narzędzia do zarządzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{pname} = %{version}-%{release}
Obsoletes:	%{oldname}-progs < 1.0.7174
Obsoletes:	XFree86-driver-nvidia-progs
Conflicts:	%{oldname}-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl.UTF-8
Narzędzia do zarządzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia-legacy
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de.UTF-8):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl.UTF-8):	Moduł jądra dla obsługi kart graficznych nVidia
Release:	%{rel}@%{_kernel_vermagic}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:Requires:	kernel%{_alt_kernel}(vermagic) = %{_kernel_ver}}
Obsoletes:	XFree86-nvidia-kernel
Obsoletes:	kernel%{_alt_kernel}-smp-video-nvidia-legacy
Obsoletes:	kernel%{_alt_kernel}-video-nvidia < 1.0.7174
Conflicts:	kernel%{_alt_kernel}-video-nvidia

%description -n kernel%{_alt_kernel}-video-nvidia-legacy
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l de.UTF-8
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l pl.UTF-8
Obsługa architektury nVidia dla jądra Linuksa. Pakiet wymagany przez
sterownik nVidii dla Xorg/XFree86.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{version}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{version}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{version}-pkg2
%endif
%patch0 -p1
%patch1 -p1
%if %{with verbose}
%patch2 -p0
%endif
sed -i 's:-Wpointer-arith::' usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
cat >> Makefile <<'EOF'

$(obj)/nv-kernel.o: $(src)/nv-kernel.o.bin
	cp $< $@
EOF
mv nv-kernel.o{,.bin}
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/modules/{drivers,extensions} \
	$RPM_BUILD_ROOT{/usr/include/GL,/usr/%{_lib}/tls,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},/etc/X11/xinit/xinitrc.d}

ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_prefix}/../lib

install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}
install usr/share/pixmaps/nvidia-settings.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/nvidia-settings.desktop
install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/nvidia-settings.sh
install usr/lib/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}
install usr/lib/tls/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}/tls
install usr/lib/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/modules/extensions

install usr/X11R6/lib/modules/drivers/nvidia_drv.so $RPM_BUILD_ROOT%{_libdir}/modules/drivers
install usr/X11R6/lib/libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/libXvMCNVIDIA.a $RPM_BUILD_ROOT%{_libdir}
install usr/include/GL/*.h	$RPM_BUILD_ROOT/usr/include/GL

ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so

# OpenGL ABI for Linux compatibility
ln -sf %{_libdir}/libGL.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so.1
ln -sf %{_libdir}/libGL.so $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so
%endif

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  You must install:                                  *
 *  kernel-video-nvidia-legacy-%{version}             *
 *  for this driver to work                            *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README,NVIDIA_Changelog,XF86Config.sample}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%dir /usr/%{_lib}/tls
%attr(755,root,root) /usr/%{_lib}/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/tls/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so*
%attr(755,root,root) %{_libdir}/modules/drivers/nvidia_drv.so
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-nvidia-legacy
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*
%endif

%if %{with userspace}
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
/usr/include/GL/*.h
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/*.sh
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%endif
