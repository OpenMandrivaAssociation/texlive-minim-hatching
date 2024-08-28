Name:		texlive-minim-hatching
Version:	70885
Release:	1
Summary:	Create tiling patterns with the minim-mp MetaPost processor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minim-hatching
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-hatching.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-hatching.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small proof-of-concept library of tiling patterns for
use with the minim-mp MetaPost processor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/minim-hatching
%doc %{_texmfdistdir}/doc/latex/minim-hatching

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
