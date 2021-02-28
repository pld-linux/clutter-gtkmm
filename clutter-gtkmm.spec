#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ wrappers for clutter-gtk library
Summary(pl.UTF-8):	Obudowanie C++ do biblioteki clutter-gtk
Name:		clutter-gtkmm
Version:	1.6.0
Release:	3
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/clutter-gtkmm/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	d4e95d2e90de5114067c9e31fd04979c
URL:		https://developer.gnome.org/clutter-gtkmm/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-gtk-devel >= 1.6.0
BuildRequires:	cluttermm-devel >= 0.9.6
BuildRequires:	gtkmm3-devel >= 3.6.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	clutter-gtk >= 1.6.0
Requires:	cluttermm >= 0.9.6
Requires:	gtkmm3 >= 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for clutter-gtk library.

%description -l pl.UTF-8
Obudowanie C++ do biblioteki clutter-gtk.

%package devel
Summary:	Header files for clutter-gtkmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-gtkmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-gtk-devel >= 1.6.0
Requires:	cluttermm-devel >= 0.9.6
Requires:	gtkmm3-devel >= 3.6.0

%description devel
Header files for clutter-gtkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-gtkmm.

%package static
Summary:	Static clutter-gtkmm library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-gtkmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-gtkmm library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-gtkmm.

%package apidocs
Summary:	clutter-gtkmm API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter-gtkmm
Group:		Documentation
BuildArch:	noarch

%description apidocs
clutter-gtkmm API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter-gtkmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libclutter-gtkmm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gtkmm-1.0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtkmm-1.0.so
%dir %{_libdir}/clutter-gtkmm-1.0
%{_libdir}/clutter-gtkmm-1.0/include
%{_includedir}/clutter-gtkmm-1.0
%{_pkgconfigdir}/clutter-gtkmm-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gtkmm-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/clutter-gtkmm-1.0
%{_datadir}/devhelp/books/clutter-gtkmm-1.0
