Summary:	RFC 2425 (and related, i.e. RFC 2426) implementation
Summary(pl):	Implementacja RFC 2425 (i powiązanych, m.in. RFC 2426)
Name:		libmimedir
Version:	0.2.0
Release:	1
License:	GPL/LGPL
Group:		Libraries
Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.gz
URL:		http://me.in-berlin.de/~jroger/gnome-pim/
BuildRequires:	glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) and related RFCs
like RFC 2426 (vCard MIME Directory Profile).

%description -l pl
Implementacja RFC 2425 (MIME Directory Profile) i powiązanych RFC
w rodzaju RFC 2426 (vCard MIME Directory Profile).

%package devel
Summary:	Development files of libmimedir library
Summary(pl):	Pliki dla programistów używających biblioteki libmimedir
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel

%description devel
Development files of libmimedir library.

%description devel -l pl
Pliki dla programistów używających biblioteki libmimedir.

%package static
Summary:	Static libmimedir libraries
Summary(pl):	Statyczne biblioteki libmimedir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmimedir libraries.

%description static -l pl
Statyczne biblioteki libmimedir.

%package progs
Summary:	VCard utilites
Summary(pl):	Narzędzia do VCard
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs
VCard utilites.

%description progs -l pl
Narzędzia do VCard.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*.so

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
