Summary:	Interface over GNU patch
Summary(pl):	Interfejs do GNU patch
Name:		xemacs-ediff-pkg
%define 	srcname	ediff
Version:	1.35
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥¨¥Ç¥£¥¿/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/òÅÄÁËÔÏÒÙ/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Tillämpningar/Editorer/Emacs
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/òÅÄÁËÔÏÒÉ/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-pcl-cvs-pkg
Requires:	xemacs-elib-pkg
Requires:	xemacs-dired-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface over GNU patch.

%description -l pl 
Interfejs do GNU patch.

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/ediff; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf lisp/ediff/README lisp/ediff/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/ediff/README.gz lisp/ediff/ChangeLog.gz 
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
