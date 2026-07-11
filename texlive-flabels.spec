%global tl_name flabels
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Labels for files and folders
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flabels
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flabels.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros for typesetting pretty labels (optionally colored) for the back
of files or binders (currently only the special A4 "Leitz-Ordner" ring
binder is supported).

