Summary:	Ogle DVD Player GUI
Summary(pl.UTF-8):	Interfejs użytkownika odtwarzacza DVD Ogle
Name:		ogle_gui
Version:	0.9.2
Release:	10
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e685aa3046f9da13532ede9300f2f794
Source1:	%{name}.desktop
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-cvs-20070625.patch
Patch2:		am.patch
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.19
BuildRequires:	ogle-devel >= 0.9.1
BuildRequires:	pkgconfig
%requires_eq	ogle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME GUI for Ogle, (the first) DVD player for Linux that supports DVD
menus!

%description -l pl.UTF-8
Interfejs użytkownika dla Ogle, (pierwszego) odtwarzacza DVD dla
Linuksa obsługujący DVD menu!

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

cat >> acinclude.m4 <<EOF
AC_DEFUN([AM_PATH_GTK],[$3])
AC_DEFUN([AM_PATH_LIBGLADE],[$2])
EOF

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ogle/*
%{_datadir}/ogle_gui
%{_desktopdir}/*.desktop
