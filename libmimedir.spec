Summary:	RFC 2425 (and related, i.e. RFC 2426) implementation
Name:		libmimedir
Version:	0.2.0
Release:	1
License:	GPL/LGPL
Group:		Libraries
Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.gz
URL:		http://me.in-berlin.de/~jroger/gnome-pim/
Requires(post):	/sbin/ldconfig
BuildRequires:	glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) and related RFCs like
RFC 2426 (vCard MIME Directory Profile).

%package devel
Summary:	Development files of libmimedir library
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel

%description devel
Development files of libmimedir library.

%package static
Summary:	Static libmimedir libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmimedir libraries.

%package progs
Summary:	VCard utilites
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs
VCard utilites.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
