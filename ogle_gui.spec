Summary:	Ogle DVD Player GUI
Summary(pl):	Interfejs u¿ytkownika odtwarzacza DVD Ogle
Name:		ogle_gui
Version:	0.7.5
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/%{name}-%{version}.tar.gz
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	gnome-libs-devel
BuildRequires:	ogle-devel
%requires_eq	ogle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME GUI for Ogle, (the first) DVD player for Linux that supports DVD
menus!

%description -l pl
Interfejs u¿ytkownika dla Ogle, (pierwszego) odtwarzacza DVD dla
Linuxa obs³uguj±cy DVD menu!

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/ogle
%{_pixmapsdir}/ogle_gui
