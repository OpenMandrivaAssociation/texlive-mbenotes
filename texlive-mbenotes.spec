# revision 31813
# category Package
# catalog-ctan /macros/latex/contrib/mbenotes
# catalog-date 2013-10-02 17:34:38 +0200
# catalog-license lppl1.2
# catalog-version 2
Name:		texlive-mbenotes
Version:	2
Release:	13
Summary:	Notes in tables or images
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mbenotes
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mbenotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mbenotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \tabnote, which stores notes for
later processing by the command \thetabnotes, and a
corresponding \imgnote for images. The package is derived from
mechanisms in the package endnotes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mbenotes/mbenotes.sty
%doc %{_texmfdistdir}/doc/latex/mbenotes/README
%doc %{_texmfdistdir}/doc/latex/mbenotes/mbenotes.pdf
%doc %{_texmfdistdir}/doc/latex/mbenotes/mbenotes.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
