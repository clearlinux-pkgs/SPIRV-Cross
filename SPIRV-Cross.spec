#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SPIRV-Cross
Version  : moltenvk.1.1.5
Release  : 1
URL      : https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/MoltenVK-1.1.5.tar.gz
Source0  : https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/MoltenVK-1.1.5.tar.gz
Summary  : C API for SPIRV-Cross
Group    : Development/Tools
License  : Apache-2.0 CC-BY-4.0 MIT
Requires: SPIRV-Cross-bin = %{version}-%{release}
Requires: SPIRV-Cross-data = %{version}-%{release}
Requires: SPIRV-Cross-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : python3

%description
<!--
SPDX-License-Identifier: CC-BY-4.0
-->
# SPIRV-Cross
SPIRV-Cross is a tool designed for parsing and converting SPIR-V to other shader languages.

%package bin
Summary: bin components for the SPIRV-Cross package.
Group: Binaries
Requires: SPIRV-Cross-data = %{version}-%{release}
Requires: SPIRV-Cross-license = %{version}-%{release}

%description bin
bin components for the SPIRV-Cross package.


%package data
Summary: data components for the SPIRV-Cross package.
Group: Data

%description data
data components for the SPIRV-Cross package.


%package dev
Summary: dev components for the SPIRV-Cross package.
Group: Development
Requires: SPIRV-Cross-bin = %{version}-%{release}
Requires: SPIRV-Cross-data = %{version}-%{release}
Provides: SPIRV-Cross-devel = %{version}-%{release}
Requires: SPIRV-Cross = %{version}-%{release}

%description dev
dev components for the SPIRV-Cross package.


%package license
Summary: license components for the SPIRV-Cross package.
Group: Default

%description license
license components for the SPIRV-Cross package.


%prep
%setup -q -n SPIRV-Cross-MoltenVK-1.1.5
cd %{_builddir}/SPIRV-Cross-MoltenVK-1.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638814824
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1638814824
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SPIRV-Cross
cp %{_builddir}/SPIRV-Cross-MoltenVK-1.1.5/LICENSE %{buildroot}/usr/share/package-licenses/SPIRV-Cross/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/SPIRV-Cross-MoltenVK-1.1.5/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/SPIRV-Cross/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593
cp %{_builddir}/SPIRV-Cross-MoltenVK-1.1.5/LICENSES/CC-BY-4.0.txt %{buildroot}/usr/share/package-licenses/SPIRV-Cross/34c678c18b31bda8b152e1462bad0c0428c69b44
cp %{_builddir}/SPIRV-Cross-MoltenVK-1.1.5/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/SPIRV-Cross/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/spirv-cross

%files data
%defattr(-,root,root,-)
/usr/share/spirv_cross_c/cmake/spirv_cross_cConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_c/cmake/spirv_cross_cConfig.cmake
/usr/share/spirv_cross_core/cmake/spirv_cross_coreConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_core/cmake/spirv_cross_coreConfig.cmake
/usr/share/spirv_cross_cpp/cmake/spirv_cross_cppConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_cpp/cmake/spirv_cross_cppConfig.cmake
/usr/share/spirv_cross_glsl/cmake/spirv_cross_glslConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_glsl/cmake/spirv_cross_glslConfig.cmake
/usr/share/spirv_cross_hlsl/cmake/spirv_cross_hlslConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_hlsl/cmake/spirv_cross_hlslConfig.cmake
/usr/share/spirv_cross_msl/cmake/spirv_cross_mslConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_msl/cmake/spirv_cross_mslConfig.cmake
/usr/share/spirv_cross_reflect/cmake/spirv_cross_reflectConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_reflect/cmake/spirv_cross_reflectConfig.cmake
/usr/share/spirv_cross_util/cmake/spirv_cross_utilConfig-relwithdebinfo.cmake
/usr/share/spirv_cross_util/cmake/spirv_cross_utilConfig.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/spirv_cross/GLSL.std.450.h
/usr/include/spirv_cross/spirv.h
/usr/include/spirv_cross/spirv.hpp
/usr/include/spirv_cross/spirv_cfg.hpp
/usr/include/spirv_cross/spirv_common.hpp
/usr/include/spirv_cross/spirv_cpp.hpp
/usr/include/spirv_cross/spirv_cross.hpp
/usr/include/spirv_cross/spirv_cross_c.h
/usr/include/spirv_cross/spirv_cross_containers.hpp
/usr/include/spirv_cross/spirv_cross_error_handling.hpp
/usr/include/spirv_cross/spirv_cross_parsed_ir.hpp
/usr/include/spirv_cross/spirv_cross_util.hpp
/usr/include/spirv_cross/spirv_glsl.hpp
/usr/include/spirv_cross/spirv_hlsl.hpp
/usr/include/spirv_cross/spirv_msl.hpp
/usr/include/spirv_cross/spirv_parser.hpp
/usr/include/spirv_cross/spirv_reflect.hpp

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SPIRV-Cross/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/SPIRV-Cross/34c678c18b31bda8b152e1462bad0c0428c69b44
/usr/share/package-licenses/SPIRV-Cross/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593
/usr/share/package-licenses/SPIRV-Cross/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3