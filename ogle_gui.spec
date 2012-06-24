Summary:	Ogle DVD Player GUI
Summary(pl):	Interfejs u�ytkownika odtwarzacza DVD Ogle
Name:		ogle_gui
Version:	0.8.5
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	92319326640a91a55b3219864710bb50
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	ogle-devel
BuildRequires:	gtk+-devel
%requires_eq	ogle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME GUI for Ogle, (the first) DVD player for Linux that supports DVD
menus!

%description -l pl
Interfejs u�ytkownika dla Ogle, (pierwszego) odtwarzacza DVD dla
Linuksa obs�uguj�cy DVD menu!

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
