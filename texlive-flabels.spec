Name:		texlive-flabels
Version:	17272
Release:	2
Summary:	Labels for files and folders
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flabels
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
