%define		_theme		Linux-Passion

Summary:	Linux Passion KDM theme
Summary(pl):	Motyw KDM Linux Passion
Name:		kdm-theme-%{_theme}
Version:	01
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	28724-Linux-Passion.tar.bz2
# Source0-md5:	eb230edc6c2ca0a9c8f64b16bf96f099
URL:		http://www.kde-look.org/content/show.php?content=28724
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Passion KDM theme.
http://kdelook.org/content/show.php?content=28724

%description -l pl
Motyw KDM Linux Passion.
http://kdelook.org/content/show.php?content=28724

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
