
Summary:	RFC 2425 (and related, i.e. RFC 2426) implementation
Summary(pl):	Implementacja RFC 2425 (i powi±zanych, m.in. RFC 2426)
Name:		libmimedir
Version:	0.3
Release:	0.1
License:	GPL/LGPL
Group:		Libraries
#Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/libmimedir/libmimedir-0.3.tar.gz
# Source0-md5:	aa15d26e678baab21400b4d2af699d0c
Patch0:		%{name}-destdir.patch
BuildRequires:	glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) and related RFCs
like RFC 2426 (vCard MIME Directory Profile).

%description -l pl
Implementacja RFC 2425 (MIME Directory Profile) i powi±zanych RFC
w rodzaju RFC 2426 (vCard MIME Directory Profile).

%package devel
Summary:	Development files of libmimedir library
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki libmimedir
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

%description devel
Development files of libmimedir library.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych biblioteki libmimedir.

%package static
Summary:	Static libmimedir libraries
Summary(pl):	Statyczne biblioteki libmimedir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmimedir libraries.

%description static -l pl
Statyczne biblioteki libmimedir.

%package progs
Summary:	VCard utilites
Summary(pl):	Narzêdzia do VCard
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
VCard utilites.

%description progs -l pl
Narzêdzia do VCard.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*
%{_includedir}/*
