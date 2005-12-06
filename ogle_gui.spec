Summary:	Ogle DVD Player GUI
Summary(pl):	Interfejs u¿ytkownika odtwarzacza DVD Ogle
Name:		ogle_gui
Version:	0.9.2
Release:	7.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e685aa3046f9da13532ede9300f2f794
Source1:	%{name}.desktop
Patch0:		%{name}-libdir.patch
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
# for AM_PATH_GTK
BuildRequires:	gtk+-devel
# for AM_PATH_LIBGLADE
BuildRequires:	libglade-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	ogle-devel >= 0.9.1
%requires_eq	ogle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME GUI for Ogle, (the first) DVD player for Linux that supports DVD
menus!

%description -l pl
Interfejs u¿ytkownika dla Ogle, (pierwszego) odtwarzacza DVD dla
Linuksa obs³uguj±cy DVD menu!

%prep
%setup -q
%patch0 -p0

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --enable-gtk2

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
