%define		_theme		Linux-Passion

Summary:	Linux Passion KDM theme
Summary(pl.UTF-8):	Motyw KDM Linux Passion
Name:		kdm-theme-%{_theme}
Version:	01
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/files/28724-Linux%20Passion.tar.gz
Source0:	28724-Linux-Passion.tar.gz
# Source0-md5:	e23a928e15b424948f205e244e750c0b
URL:		http://www.kde-look.org/content/show.php?content=28724
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdm >= 9:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Passion KDM theme.
http://kdelook.org/content/show.php?content=28724

%description -l pl.UTF-8
Motyw KDM Linux Passion.
http://kdelook.org/content/show.php?content=28724

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install Linux\ Passion/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
