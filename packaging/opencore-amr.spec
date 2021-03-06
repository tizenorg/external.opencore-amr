Name:       opencore-amr
Summary:    opencore AMRNB dev package
Version:    0.1.2
Release:    2
Group:      libdevel
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/opencore-amr.manifest
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(vconf)

BuildRequires:  cmake
BuildRequires:  gettext-devel

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
cp %{SOURCE1001} .
./autogen.sh
./configure --prefix=/usr --mandir=%{_prefix}/share/man --infodir=%{_prefix}/share/info CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post

%postun


%files
%manifest opencore-amr.manifest
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrnb.so.0
%{_libdir}/libopencore-amrnb.so.0.0.2
%{_libdir}/libopencore-amrwb.so.0
%{_libdir}/libopencore-amrwb.so.0.0.2

%files devel 
%manifest opencore-amr.manifest
%defattr(-,root,root,-)
%{_includedir}/opencore-amrnb/*.h
%{_includedir}/opencore-amrwb/*.h
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
