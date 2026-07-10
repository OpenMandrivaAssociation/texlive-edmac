%global tl_name edmac
%global tl_revision 72250

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.17
Release:	%{tl_revision}.1
Summary:	Typeset critical editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/edmac
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the type example package for typesetting scholarly critical
editions.

