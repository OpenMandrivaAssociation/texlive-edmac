# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/edmac
# catalog-date 2007-01-02 10:01:06 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-edmac
Version:	20070102
Release:	1
Summary:	Typeset scholarly edition
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/edmac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmac.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A macro package for typesetting scholarly critical editions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
