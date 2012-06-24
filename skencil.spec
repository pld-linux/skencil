%define		snap 20050103
#
Summary:	Advanced vector graphics program written in Python
Summary(pl):	Zaawansowany program do rysowania grafiki wektorowej napisany w Pythonie
Summary(pt_BR):	Programa para desenhos de gr�ficos vetoriais baseado em Python
Name:		skencil
Version:	0.7.12
Release:	0.%{snap}.2
License:	GPL
Group:		Applications/Graphics
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	4a6e4a53254f1d442cc1b2c613a09345
Source1:	%{name}.desktop
Patch0:		%{name}-libart2.patch
URL:		http://www.skencil.org
BuildRequires:	python-Imaging-devel >= 1.0
BuildRequires:	python-devel >= 2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python
Requires:	python-Imaging
Requires:	python-pygtk-gtk >= 2.0
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
Skencil to interaktywny program do rysunku wektorowego dla
X11 (podobnie jak XFig lub tgif). Jego g��wne funkcje to:
- podstawowe kszta�ty rysunkowe takie jak prostok�ty, elipsy, krzywe
  Beziera, zewn�trzne pliki z obrazami, tekst
- w�a�ciwo�ci kszta�t�w
- przekszta�cenia - obr�t, skalowanie, etc.
- efekty specjalne takie jak ��czenie w grupy, konwersja tekstu na
  krzywe Beziera, uk�adanie tekstu wed�ug zadanego kszta�tu, prostok�ty
  oraz elipsy jako dodatkowe linie pomocnicze
- zapis w innych formatach (EPS, Adobe Illustrator)
- odczyt obcych format�w (XFig, Adobe Illustrator, WMF, CMX programu
  Corel Draw)
- niesko�czona historia zmian pozwalaj�ca na ich cofni�cie
- skrypty u�ytkownika

%description -l pt_BR
Skencil � um programa para desenhos de gr�ficos vetoriais que roda
sobre o X. Ele � escrito em inteiramente em Python, uma linguagem de
programa��o orientada a objeto interpretada.

%prep
%setup -q -n %{name}

sed -i -e 's@/lib/python@/%{_lib}/python@' \
	Filter/Makefile.pre.in \
	Sketch/Modules/Makefile.pre.in
sed -i -e "s@'lib'@'%{_lib}'@" setup.py
%patch0 -p0

%build
#%{__python} setup.py configure \
#	--imaging-include=%{py_incdir} \
#	--python-setup=%{py_libdir}/config/Setup \
#	--tk-flags='-ltk -ltcl -L/usr/X11R6/%{_lib} -lX11' \
#	--with-nls
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir}}

%{__python} setup.py install \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install Sketch/VERSION $RPM_BUILD_ROOT%{_libdir}/%{name}-cvs/Sketch
cp -r Sketch/{Modules,Lib,Pixmaps} $RPM_BUILD_ROOT%{_libdir}/%{name}-cvs/Sketch
cp -r Filter $RPM_BUILD_ROOT%{_libdir}/%{name}-cvs/Sketch

mv -f Doc guides
ln -s %{_libdir}/%{name}-cvs/skencil.py $RPM_BUILD_ROOT%{_bindir}/skencil

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO guides
#attr(755,root,root) %{_bindir}/sk2ps
#attr(755,root,root) %{_bindir}/sk2ppm
#attr(755,root,root) %{_bindir}/sketch
%attr(755,root,root) %{_bindir}/skencil
#attr(755,root,root) %{_bindir}/skshow
#attr(755,root,root) %{_bindir}/skconvert
%dir %{_libdir}/%{name}-cvs
#attr(755,root,root) %{_libdir}/%{name}-cvs/sk2ps.py
#attr(755,root,root) %{_libdir}/%{name}-cvs/sk2ppm.py
%attr(755,root,root) %{_libdir}/%{name}-cvs/skencil.py
#attr(755,root,root) %{_libdir}/%{name}-cvs/skshow.py
#attr(755,root,root) %{_libdir}/%{name}-cvs/skconvert.py
#%{_libdir}/%{name}-cvs/Resources
#%{_libdir}/%{name}-cvs/Script
%dir %{_libdir}/%{name}-cvs/Sketch
%{_libdir}/%{name}-cvs/Sketch/VERSION
%{_libdir}/%{name}-cvs/Sketch/*.py*
%{_libdir}/%{name}-cvs/Sketch/Base
%{_libdir}/%{name}-cvs/Sketch/Editor
%{_libdir}/%{name}-cvs/Sketch/Filter
%{_libdir}/%{name}-cvs/Sketch/Pixmaps
%{_libdir}/%{name}-cvs/Sketch/Lib
#%{_libdir}/%{name}-cvs/Sketch/Scripting
%{_libdir}/%{name}-cvs/Sketch/Graphics
%{_libdir}/%{name}-cvs/Sketch/UI
%dir %{_libdir}/%{name}-cvs/Sketch/Modules
%attr(755,root,root) %{_libdir}/%{name}-cvs/Sketch/Modules/*.so
%{_libdir}/%{name}-cvs/Sketch/Plugin
#%dir %{_libdir}/%{name}-cvs/Lib
#attr(755,root,root) %{_libdir}/%{name}-cvs/Lib/*.so
#%{_libdir}/%{name}-cvs/Lib/*.py*

%{_desktopdir}/%{name}.desktop
