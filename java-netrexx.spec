%include	/usr/lib/rpm/macros.java
Summary:	NetRexx - programming language derived from both Rexx and Java
Summary(pl.UTF-8):	NetRexx - język programowania wywodzący się z języka Rexx i Javy
Name:		netrexx
Version:	2.05
Release:	2
License:	IBM proprietary, distributable (see license.txt)
Group:		Development/Languages/Java
Source0:	http://www-306.ibm.com/software/awdtools/netrexx/NetRexx.zip
# Source0-md5:	07622f619758b83d593a127f4a2542f1
Patch0:		%{name}-classpath.patch
URL:		http://www2.hursley.ibm.com/netrexx/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautocompressdoc *.au *.class *.nrx *.txt *.zip

%description
NetRexx is a programming language derived from both Rexx and Java. It
is a dialect of Rexx that retains the portability and efficiency of
Java, while being as easy to learn and to use as Rexx.

%description -l pl.UTF-8
NetRexx to język programowania wywodzący się jednocześnie z języka
Rexx oraz Javy. Jest to dialekt języka Rexx zachowujący przenośność i
wydajność Javy, będący jednocześnie łatwy do nauczenia i używania tak
jak Rexx.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n NetRexx
%patch0 -p1
find '(' -name '*.sh' -o -name 'nrc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}
install lib/NetRexxC.jar runlib/NetRexxR.jar $RPM_BUILD_ROOT%{_javadir}
install bin/{NetRexxC.sh,nrc} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc read.me.first
%attr(755,root,root) %{_bindir}/*
%{_javadir}/NetRexx*.jar

%files doc
%defattr(644,root,root,755)
%doc browse/*
