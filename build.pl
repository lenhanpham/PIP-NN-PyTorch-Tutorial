#!/usr/bin/env perl
use feature qw(say);

die "Usage:\n\t\$ perl degree [molecule]\n" if $#ARGV < 1;

$degree = shift;
@atoms = @ARGV;
$conf = join "_", @atoms;
$conf .= "_$degree";

$src = "basis_$conf.f90";
die "Cannot open file $src, $!" unless -e $src;

$module = "pip_$conf";

`f2py --overwrite-signature $src -m $module -h $module.pyf`;
`f2py -c $src $module.pyf`;

say "Done!";
