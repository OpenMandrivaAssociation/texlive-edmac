Name:		texlive-edmac
Version:	61719
Release:	1
Summary:	Typeset scholarly edition
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/edmac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A macro package for typesetting scholarly critical editions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/edmac/edmac.tex
%{_texmfdistdir}/tex/generic/edmac/edmacfss.sty
%{_texmfdistdir}/tex/generic/edmac/edstanza.tex
%{_texmfdistdir}/tex/generic/edmac/tabmac.tex
%doc %{_texmfdistdir}/doc/latex/edmac/COPYRIGHT
%doc %{_texmfdistdir}/doc/latex/edmac/braonain.tex
%doc %{_texmfdistdir}/doc/latex/edmac/copying
%doc %{_texmfdistdir}/doc/latex/edmac/ed-nfss.txt
%doc %{_texmfdistdir}/doc/latex/edmac/edmac.doc
%doc %{_texmfdistdir}/doc/latex/edmac/edstanza.doc
%doc %{_texmfdistdir}/doc/latex/edmac/edszadoc.tex
%doc %{_texmfdistdir}/doc/latex/edmac/features.tex
%doc %{_texmfdistdir}/doc/latex/edmac/readme
#- source
%doc %{_texmfdistdir}/source/latex/edmac/edmac.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
