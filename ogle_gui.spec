Summary:	Ogle DVD Player GUI
Summary(pl):	Interfejs użytkownika odtwarzacza DVD Ogle
Name:		ogle_gui
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e685aa3046f9da13532ede9300f2f794
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	ogle-devel >= 0.9.1
%requires_eq	ogle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME GUI for Ogle, (the first) DVD player for Linux that supports DVD
menus!

%description -l pl
Interfejs użytkownika dla Ogle, (pierwszego) odtwarzacza DVD dla
Linuksa obsługujący DVD menu!

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ogle/*
%{_datadir}/locale/*/*/*
%{_datadir}/ogle_gui
