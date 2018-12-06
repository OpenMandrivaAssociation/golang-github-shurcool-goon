# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/go-goon
%global commit          37c2f522c041b74919a9e5e3a6c5c47eb34730a5

%global common_description %{expand:
A deep pretty printer with Go-like notation. It implements the goon 
specification.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A deep pretty printer with Go-like notation
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/go/reflectsource)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git37c2f52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180421git37c2f52
- First package for Fedora

