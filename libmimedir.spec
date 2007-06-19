# NOTE: it's totally different than Lev Walkin's libmimedir
#       (libmimedir-vlm.spec)
Summary:	RFC 2425 (and related, i.e. RFC 2426) implementation
Summary(pl.UTF-8):	Implementacja RFC 2425 (i powiązanych, m.in. RFC 2426)
Name:		libmimedir
Version:	0.2.1
%define	snap	20030114
Release:	1.%{snap}.1
License:	LGPL (library), GPL (utilities)
Group:		Libraries
#Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	aa15d26e678baab21400b4d2af699d0c
Patch0:		%{name}-typedef-enum.patch
URL:		http://me.in-berlin.de/~jroger/gnome-pim/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) and related RFCs
like RFC 2426 (vCard MIME Directory Profile). It was written by
Sebastian Rittau.

%description -l pl.UTF-8
Implementacja RFC 2425 (MIME Directory Profile) i powiązanych RFC
w rodzaju RFC 2426 (vCard MIME Directory Profile). Autorem tej
implementacji jest Sebastian Rittau.

%package devel
Summary:	Development files of libmimedir library
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki libmimedir
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0

%description devel
Development files of libmimedir library.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki libmimedir.

%package static
Summary:	Static libmimedir libraries
Summary(pl.UTF-8):	Statyczne biblioteki libmimedir
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmimedir libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libmimedir.

%package progs
Summary:	VCard utilites
Summary(pl.UTF-8):	Narzędzia do VCard
License:	GPL
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
VCard utilites.

%description progs -l pl.UTF-8
Narzędzia do VCard.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README TODO
%attr(755,root,root) %{_libdir}/libmimedir-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimedir.so
%{_libdir}/libmimedir.la
%{_includedir}/mimedir-*
%{_pkgconfigdir}/mimedir-*.pc
%{_gtkdocdir}/mimedir

%files static
%defattr(644,root,root,755)
%{_libdir}/libmimedir.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
