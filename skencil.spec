Summary:	Advanced vector graphics program written in Python
Summary(pl):	Zaawansowany program do rysowania grafiki wektorowej napisany w Pythonie
Summary(pt_BR):	Programa para desenhos de gráficos vetoriais baseado em Python
Name:		skencil
Version:	0.6.16
Release:	4
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/sketch/%{name}-%{version}.tar.gz
# Source0-md5:	22db4f78151629df428c387e035fdad2
Source1:	%{name}.desktop
Patch0:		%{name}-python2.4.patch
URL:		http://www.skencil.org/
BuildRequires:	python-Imaging-devel >= 1.0
BuildRequires:	python-devel >= 2.1
BuildRequires:	sed >= 4.0
BuildRequires:	tk-devel
%pyrequires_eq	python
Requires:	python-Imaging
Requires:	python-tkinter >= 2.1
Obsoletes:	sketch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skencil is an interactive X11 drawing program (similar to XFig or
tgif). It features:
- drawing primitives like rectangles, ellipses, bezier curves,
  external images, text
- primitives properties
- transformations: rotation, scaling, shearing, etc.
- special effects like blend groups, converting text to bezier
  objects, text along path and using bezier curves, rectangles and
  ellipses as guides in addition to standard vertical and horizontal
  guide lines
- export file formats (EPS, Adobe Illustrator)
- import file formats (XFig, Adobe Illustrator, WMF, Corels CMX)
- unlimited undo history
- user scripts

%description -l pl
Skencil to interaktywny program do rysunku wektorowego dla systemu
Xwindow (podobnie jak XFig lub tgif). Jego g³ówne funkcje to:
- podstawowe kszta³ty rysunkowe takie jak prostok±ty, elipsy, krzywe
  Beziera, zewnêtrzne pliki z obrazami, tekst
- w³a¶ciwo¶ci kszta³tów
- przekszta³cenia - obrót, skalowanie, etc.
- efekty specjalne takie jak ³±czenie w grupy, konwersja tekstu na
  krzywe Beziera, uk³adanie tekstu wed³ug zadanego kszta³tu, prostok±ty
  oraz elipsy jako dodatkowe linie pomocnicze
- zapis w innych formatach (EPS, Adobe Illustrator)
- odczyt obcych formatów (XFig, Adobe Illustrator, WMF, CMX programu
  Corel Draw)
- nieskoñczona historia zmian pozwalaj±ca na ich cofniêcie
- skrypty u¿ytkownika

%description -l pt_BR
Skencil é um programa para desenhos de gráficos vetoriais que roda
sobre o X. Ele é escrito em inteiramente em Python, uma linguagem de
programação orientada a objeto interpretada.

%prep
%setup -q

sed -i -e 's@/lib/python@/%{_lib}/python@' \
	Pax/Makefile.pre.in \
	Filter/Makefile.pre.in \
	Sketch/Modules/Makefile.pre.in
sed -i -e "s@'lib'@'%{_lib}'@" setup.py
%patch0 -p2

%build
%{__python} setup.py configure \
	--imaging-include=%{py_incdir} \
	--python-setup=%{py_libdir}/config/Setup \
	--tk-flags='-ltk -ltcl -L/usr/X11R6/%{_lib} -lX11' \
	--with-nls
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__python} setup.py install \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

mv -f Doc guides

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS PROJECTS README TODO guides
%attr(755,root,root) %{_bindir}/sk2ps
%attr(755,root,root) %{_bindir}/sk2ppm
%attr(755,root,root) %{_bindir}/sketch
%attr(755,root,root) %{_bindir}/skencil
%attr(755,root,root) %{_bindir}/skshow
%attr(755,root,root) %{_bindir}/skconvert
%dir %{_libdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/sk2ps.py
%attr(755,root,root) %{_libdir}/%{name}-%{version}/sk2ppm.py
%attr(755,root,root) %{_libdir}/%{name}-%{version}/skencil.py
%attr(755,root,root) %{_libdir}/%{name}-%{version}/skshow.py
%attr(755,root,root) %{_libdir}/%{name}-%{version}/skconvert.py
%{_libdir}/%{name}-%{version}/Resources
%{_libdir}/%{name}-%{version}/Script
%dir %{_libdir}/%{name}-%{version}/Sketch
%{_libdir}/%{name}-%{version}/Sketch/VERSION
%{_libdir}/%{name}-%{version}/Sketch/*.py*
%{_libdir}/%{name}-%{version}/Sketch/Base
%{_libdir}/%{name}-%{version}/Sketch/Pixmaps
%{_libdir}/%{name}-%{version}/Sketch/Lib
%{_libdir}/%{name}-%{version}/Sketch/Scripting
%{_libdir}/%{name}-%{version}/Sketch/Graphics
%{_libdir}/%{name}-%{version}/Sketch/UI
%dir %{_libdir}/%{name}-%{version}/Sketch/Modules
%attr(755,root,root) %{_libdir}/%{name}-%{version}/Sketch/Modules/*.so
%{_libdir}/%{name}-%{version}/Plugins
%dir %{_libdir}/%{name}-%{version}/Lib
%attr(755,root,root) %{_libdir}/%{name}-%{version}/Lib/*.so
%{_libdir}/%{name}-%{version}/Lib/*.py*

%{_desktopdir}/%{name}.desktop
