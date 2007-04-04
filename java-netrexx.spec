Summary:	NetRexx - programming language derived from both Rexx and Java
Summary(pl.UTF-8):	NetRexx - język programowania wywodzący się z języka Rexx i Javy
Name:		netrexx
Version:	2.05
Release:	1
License:	IBM proprietary, distributable (see license.txt)
Group:		Development/Languages/Java
Source0:	http://www-306.ibm.com/software/awdtools/netrexx/NetRexx.zip
# Source0-md5:	07622f619758b83d593a127f4a2542f1
Patch0:	%{name}-classpath.patch
URL:		http://www2.hursley.ibm.com/netrexx/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetRexx is a programming language derived from both Rexx and Java. It
is a dialect of Rexx that retains the portability and efficiency of
Java, while being as easy to learn and to use as Rexx.

%description -l pl.UTF-8
NetRexx to język programowania wywodzący się jednocześnie z języka
Rexx oraz Javy. Jest to dialekt języka Rexx zachowujący przenośność i
wydajność Javy, będący jednocześnie łatwy do nauczenia i używania tak
jak Rexx.

%define _noautocompressdoc *.au *.class *.nrx *.txt *.zip

%prep
%setup -q -n NetRexx
%patch0 -p1

%build
find '(' -name '*.sh' -o -name 'nrc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}

install lib/NetRexxC.jar runlib/NetRexxR.jar $RPM_BUILD_ROOT%{_javadir}
install bin/{NetRexxC.sh,nrc} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc read.me.first browse/*
%attr(755,root,root) %{_bindir}/*
%{_javadir}/NetRexx*.jar
