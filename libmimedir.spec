# NOTE: it's totally different than previous packages built from this spec
#       (http://me.in-berlin.de/~jroger/gnome-pim/ up to 0.2.1 version)
Summary:	RFC 2425 implementation
Summary(pl):	Implementacja RFC 2425
Name:		libmimedir
Version:	0.3
Release:	0.99
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/synce/libmimedir-0.3.tar.gz
# Source0-md5:	bb967f6f8931d4efdc34d3729b7f819b
Patch0:		%{name}-destdir.patch
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile).

%description -l pl
Implementacja RFC 2425 (MIME Directory Profile).

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/*
%{_includedir}/*
