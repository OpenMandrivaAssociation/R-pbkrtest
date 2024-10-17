%global packname  pbkrtest
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.7
Release:          1
Summary:          Parametric bootstrap and Kenward Roger based methods for mixed model comparison
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-7.tar.gz

Requires:         R-MASS R-lme4 R-parallel 
Requires:         R-Matrix 
Requires:         R-gplots 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-lme4 R-parallel
BuildRequires:    R-Matrix 
BuildRequires:   R-gplots 
%description
Test in linear mixed effects models. . Attention is on linear mixed
effects models as implemented in the lme4 package. . The package
implements a parametric bootstrap test . The package implements a
Kenward-Roger modification of F-tests

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
