# revision 17272
# category Package
# catalog-ctan /macros/latex/contrib/flabels
# catalog-date 2010-02-28 22:13:22 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-flabels
Version:	1.0
Release:	2
Summary:	Labels for files and folders
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flabels
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros for typesetting pretty labels (optionally colored) for
the back of files or binders (currently only the special A4
"Leitz-Ordner" ring binder is supported).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751918
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718455
- texlive-flabels
- texlive-flabels
- texlive-flabels
- texlive-flabels

