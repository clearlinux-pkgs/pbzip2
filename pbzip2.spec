#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD332F1B09A0D9836 (nikolov.javor@gmail.com)
#
Name     : pbzip2
Version  : 1.1.13
Release  : 8
URL      : https://launchpad.net/pbzip2/1.1/1.1.13/+download/pbzip2-1.1.13.tar.gz
Source0  : https://launchpad.net/pbzip2/1.1/1.1.13/+download/pbzip2-1.1.13.tar.gz
Source99 : https://launchpad.net/pbzip2/1.1/1.1.13/+download/pbzip2-1.1.13.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : bzip2-1.0.6
Requires: pbzip2-bin
Requires: pbzip2-doc
BuildRequires : bzip2-dev
Patch1: build.patch

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.  The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be 
decompressed with bzip2).

%package bin
Summary: bin components for the pbzip2 package.
Group: Binaries

%description bin
bin components for the pbzip2 package.


%package doc
Summary: doc components for the pbzip2 package.
Group: Documentation

%description doc
doc components for the pbzip2 package.


%prep
%setup -q -n pbzip2-1.1.13
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492440276
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1492440276
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pbunzip2
/usr/bin/pbzcat
/usr/bin/pbzip2

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
