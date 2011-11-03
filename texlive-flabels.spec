# revision 17272
# category Package
# catalog-ctan /macros/latex/contrib/flabels
# catalog-date 2010-02-28 22:13:22 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-flabels
Version:	1.0
Release:	1
Summary:	Labels for files and folders
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flabels
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Macros for typesetting pretty labels (optionally colored) for
the back of files or binders (currently only the special A4
"Leitz-Ordner" ring binder is supported).

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
%{_texmfdistdir}/tex/latex/flabels/flabels.sty
%doc %{_texmfdistdir}/doc/latex/flabels/README
%doc %{_texmfdistdir}/doc/latex/flabels/flabels.pdf
%doc %{_texmfdistdir}/doc/latex/flabels/makedoc
%doc %{_texmfdistdir}/doc/latex/flabels/makedoc-patched
%doc %{_texmfdistdir}/doc/latex/flabels/makedoc.bat
#- source
%doc %{_texmfdistdir}/source/latex/flabels/flabels.dtx
%doc %{_texmfdistdir}/source/latex/flabels/flabels.ins
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
