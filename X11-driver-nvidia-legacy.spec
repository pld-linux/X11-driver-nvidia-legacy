#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	smp		# without smp packages
%bcond_without	kernel		# without kernel packages
%bcond_with	verbose		# verbose build (V=1)
#
### DON'T CHANGE THIS ###############
%define		_nv_ver		1.0
%define		_nv_rel		7184
%define		_min_x11	6.7.0
%define		_rel		1
#####################################
#
%define		oldname 	X11-driver-nvidia

Summary:	Linux Drivers for nVidia TNT/TNT2/GF/old GF2/Quadro Chips
Summary(pl):	Sterowniki do kart graficznych nVidia TNT/TNT2/GeForce/old GF2/Quadro
Name:		X11-driver-nvidia-legacy
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}
License:	nVidia Binary
Group:		X11
# why not pkg0!?
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1.run
# Source0-md5:	68cf7f155786daf6946b9daeb64c7a35
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2.run
# Source1-md5:	332850387c4e7a4619753b856e3199e5
Source2:	%{oldname}-settings.desktop
Source3:	%{oldname}-xinitrc.sh
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-GL.patch
Patch2:		%{name}-verbose.patch
URL:		http://www.nvidia.com/object/linux.html
BuildRequires:	%{kgcc_package}
#BuildRequires:	X11-devel >= %{_min_x11}	# disabled for now
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.7}
BuildRequires:	rpmbuild(macros) >= 1.326
BuildRequires:	sed >= 4.0
BuildConflicts:	XFree86-nvidia
Requires:	X11-Xserver
Requires:	X11-libs >= %{_min_x11}
Requires:	X11-modules >= %{_min_x11}
Provides:	X11-OpenGL-core
Provides:	X11-OpenGL-libGL
Provides:	XFree86-OpenGL-core
Provides:	XFree86-OpenGL-libGL
Obsoletes:	%{oldname} < 1.0.7174
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core
Obsoletes:	X11-OpenGL-libGL
Obsoletes:	XFree86-OpenGL-core
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
#Conflicts:	%{oldname}
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

%description -l pl
Usprawnione sterowniki dla kart graficznych nVidia do serwera X daj±ce
wysokowydajn± akceleracjê OpenGL, obs³ugê AGP i wiele monitorów.

Obs³uguj± karty nVidia TNT/TNT2/GeForce/stare GeForce2/Quadro do
serwera Xorg. Dla kart GF2 (nowych), GF3 i GF4 jest pakiet
X11-driver-nvidia. Karty nVidia NV1 i Riva 128/128ZX s± obs³ugiwane
przez sterownik nv z pakietów Xorg lub XFree86 - NIE s± obs³ugiwane
przez ten pakiet.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag³ówkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	OpenGL-devel-base
Obsoletes:	%{oldname}-devel < 1.0.7174
Obsoletes:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	%{oldname}-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
Base headers (only gl?.h) for OpenGL for X11R6 for nvidia drivers.

%description devel -l pl
Podstawowe pliki nag³ówkowe (tylko gl?.h) OpenGL dla systemu X11R6 dla
sterowników nvidii.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl):	Narzêdzia do zarz±dzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{oldname}-progs < 1.0.7174
Obsoletes:	XFree86-driver-nvidia-progs
Conflicts:	%{oldname}-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl
Narzêdzia do zarz±dzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia-legacy
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_up}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel
Obsoletes:	kernel%{_alt_kernel}-video-nvidia < 1.0.7174
Conflicts:	kernel%{_alt_kernel}-video-nvidia

%description -n kernel%{_alt_kernel}-video-nvidia-legacy
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l pl
Obs³uga architektury nVidia dla j±dra Linuksa. Pakiet wymagany przez
sterownik nVidii dla Xorg/XFree86.

%package -n kernel%{_alt_kernel}-smp-video-nvidia-legacy
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_smp}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel
Obsoletes:	kernel%{_alt_kernel}-smp-video-nvidia < 1.0.7174
Conflicts:	kernel%{_alt_kernel}-smp-video-nvidia

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy
nVidia Architecture support for Linux kernel SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy -l pl
Obs³uga architektury nVidia dla j±dra Linuksa SMP. Pakiet wymagany
przez sterownik nVidii dla Xorg/XFree86.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{_nv_ver}-%{_nv_rel}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2
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
%ifarch %{x8664}
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#install -d $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32%{?with_tls:/tls}/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
%endif

install usr/X11R6/lib/modules/drivers/nvidia_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/drivers
install usr/X11R6/lib/libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/libXvMCNVIDIA.a $RPM_BUILD_ROOT%{_libdir}
install usr/include/GL/*.h	$RPM_BUILD_ROOT/usr/include/GL

ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so

# OpenGL ABI for Linux compatibility
ln -sf %{_libdir}/libGL.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so.1
ln -sf %{_libdir}/libGL.so $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so

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
 *  kernel(24)(-smp)-video-nvidia-legacy-%{version}             *
 *  for this driver to work                            *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-smp-video-nvidia-legacy
%depmod %{_kernel_ver}smp

%postun	-n kernel%{_alt_kernel}-smp-video-nvidia-legacy
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README,NVIDIA_Changelog,XF86Config.sample}
#%%lang(de) %doc usr/share/doc/README.DE
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%dir /usr/%{_lib}/tls
%attr(755,root,root) /usr/%{_lib}/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/tls/libnvidia-tls.so.*.*.*
%ifarch %{x8664}
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#dir %{_libdir32}
#attr(755,root,root) %{_libdir32}/libGL.so.*.*
#attr(755,root,root) %{_libdir32}/libGLcore.so.*.*
#attr(755,root,root) %{_libdir32}/libXvMCNVIDIA.so.*.*
#attr(755,root,root) %{_libdir32}/libnvidia-tls.so.*.*.*
%endif
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so*
%attr(755,root,root) %{_libdir}/modules/drivers/nvidia_drv.o

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-nvidia-legacy
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-video-nvidia-legacy
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
/usr/include/GL/*.h
# -static
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/*.sh
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
