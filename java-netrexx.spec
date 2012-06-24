Summary:	NetRexx - programming language derived from both Rexx and Java
Summary(pl):	NetRexx - j�zyk programowania wywodz�cy si� z j�zyka Rexx i Javy
Name:		netrexx
Version:	2.05
Release:	1
License:	IBM proprietary, distributable (see license.txt)
Group:		Development/Languages/Java
Source0:	http://www-306.ibm.com/software/awdtools/netrexx/NetRexx.zip
# Source0-md5:	07622f619758b83d593a127f4a2542f1
URL:		http://www2.hursley.ibm.com/netrexx/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetRexx is a programming language derived from both Rexx and Java. It
is a dialect of Rexx that retains the portability and efficiency of
Java, while being as easy to learn and to use as Rexx.

%description -l pl
NetRexx to j�zyk programowania wywodz�cy si� jednocze�nie z j�zyka
Rexx oraz Javy. Jest to dialekt j�zyka Rexx zachowuj�cy przeno�no�� i
wydajno�� Javy, b�d�cy jednocze�nie �atwy do nauczenia i u�ywania tak
jak Rexx.

%prep
%setup -q -n NetRexx

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
