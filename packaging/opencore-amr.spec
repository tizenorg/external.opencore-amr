Name:       opencore-amr
Summary:    opencore AMRNB dev package
Version:    0.1.3
Release:    0
Group:      libdevel
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz


%description
opencore AMRNB dev package


%package devel 
Summary:    opencore AMRNB dev package (Developement)
Group:      TO_BE_FILLED 
Requires:   %{name} = %{version}-%{release}

%description devel
opencore AMRNB dev package (Developement)

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr --mandir=%{_prefix}/share/man --infodir=%{_prefix}/share/info CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}
%make_install

%post

%postun


%files
%manifest opencore-amr.manifest
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrnb.so*
%{_libdir}/libopencore-amrwb.so*
%{_datadir}/license/%{name}

%files devel 
%defattr(-,root,root,-)
%{_includedir}/opencore-amrnb/*.h
%{_includedir}/opencore-amrwb/*.h
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
