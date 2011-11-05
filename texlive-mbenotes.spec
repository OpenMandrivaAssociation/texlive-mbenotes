# revision 24321
# category Package
# catalog-ctan /macros/latex/contrib/mbenotes
# catalog-date 2011-10-17 17:40:54 +0200
# catalog-license lppl1.2
# catalog-version 2
Name:		texlive-mbenotes
Version:	2
Release:	1
Summary:	Notes in tables or images
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mbenotes
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mbenotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mbenotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a command \tabnote, which stores notes for
later processing by the command \thetabnotes, and a
corresponding \imgnote for images. The package is derived from
mechanisms in the package endnotes.

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
%{_texmfdistdir}/tex/latex/mbenotes/mbenotes.sty
%doc %{_texmfdistdir}/doc/latex/mbenotes/README
%doc %{_texmfdistdir}/doc/latex/mbenotes/mbe.pdf
%doc %{_texmfdistdir}/doc/latex/mbenotes/mbenotes.pdf
%doc %{_texmfdistdir}/doc/latex/mbenotes/mbenotes.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
