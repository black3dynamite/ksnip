%define    packager           Damir Porobic <damir.porobic@gmx.com>
%define  __spec_install_post %{nil}
%define    debug_package     %{nil}
%define  __os_install_post   %{_dbpath}/brp-compress
%define  _signature           gpg
%define  _gpg_name            Ksnip


Name:    ksnip
Summary: Screenshot Tool
Version: X.X.X
Release: 1
Source0: %{name}-%{version}.tar.gz
URL:     https://github.com/ksnip/ksnip
License: GPLV2+
Group:   Application/Utility
BuildRequires: update-desktop-files


%description
Screenshot tool that provides many annotation features for your screenshots.

%prep
%setup

%build
cmake .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cp /usr/local/kImageAnnotator/translations/kImageAnnotator_*.qm $RPM_BUILD_ROOT/usr/share/ksnip/translations/
%suse_update_desktop_file -r %{name} Utility DesktopUtility

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_usr}/bin/%{name}
%{_usr}/share/applications/%{name}.desktop
%{_usr}/share/pixmaps/%{name}.svg
%{_usr}/share/%{name}/translations/*.qm
%{_usr}/share/metainfo/%{name}.appdata.xml

%changelog
