
Summary:	RFC 2425 (and related, i.e. RFC 2426) implementation
Summary(pl):	Implementacja RFC 2425 (i powiązanych, m.in. RFC 2426)
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
Implementacja RFC 2425 (MIME Directory Profile) i powiązanych RFC
w rodzaju RFC 2426 (vCard MIME Directory Profile).

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
