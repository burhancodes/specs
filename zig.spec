%global debug_package %{nil}

Name:           zig
Version:        0.14.0
Release:        1%{?dist}
Summary:        General-purpose programming language designed for robustness, optimality, and maintainability

License:        MIT
URL:            https://ziglang.org/
Source0:        https://ziglang.org/download/%{version}/zig-linux-x86_64-%{version}.tar.xz

Provides:       zig(lang) = %{version}
ExclusiveArch:  x86_64

%description
Zig is a general-purpose programming language and toolchain for maintaining
robust, optimal, and reusable software.

%prep
%setup -q -n zig-linux-x86_64-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/zig
mkdir -p %{buildroot}%{_docdir}/%{name}

install -D -m755 zig %{buildroot}%{_bindir}/zig

cp -p LICENSE %{buildroot}%{_docdir}/%{name}/
cp -p README.md %{buildroot}%{_docdir}/%{name}/
cp -a lib/* %{buildroot}%{_libdir}/zig/

ln -s %{_libdir}/zig %{buildroot}%{_bindir}/lib

%files
%doc %{_docdir}/%{name}/README.md
%license %{_docdir}/%{name}/LICENSE
%{_bindir}/zig
%{_bindir}/lib
%{_libdir}/zig/

%changelog
%autochangelog
