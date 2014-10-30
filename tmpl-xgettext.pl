#!/usr/bin/perl

# A script to fetch gettext strings from a htmltmpl template.
# The strings must be in the special htmltmpl format:
#
#   [string]
#
# It uses stdin and stdout and takes no parameters.
#
# Usage:
#
#   cat template.tmpl | perl tmpl-xgettext.pl | xgettext -o file.po -
#
# Copyright Tomas Styblo, htmltmpl templating engine, 2001
# http://htmltmpl.sourceforge.net/
# tripie@cpan.org
# LICENSE: GNU GPL
# CVS: $Id: tmpl-xgettext.pl,v 1.1 2001/11/26 08:45:10 tripiecz Exp $

use strict;

main();

#################
### FUNCTIONS ###
#################

sub main {
    my $data = '';
    while(<>) {
        $data .= $_;
    }

    my $test = '
[[Pokusny]] [[retezec]]. A ted [[test
na vice radcich]].

Eskejpnuta \\[[pitomost]].
Test [[delsi vec [[ test]].
Test [[delsi vec \\[[ test]].
Vnitrni eskejp [[delsi vec test\\]] pokus]] cont.
Textik ]].
Textik \\]].
Pokus \a \b.
Non \\\\[[eskejp]].
Plain \\eskejp.
';

    my @gt_strings = ();
    my $res = parse_gettext($data, \@gt_strings);
    print "RESULT: $res\n";
    my $string;
    foreach $string (@gt_strings) {
        $string =~ s/\r?\n/\\n/g;
        print "gettext(\"$string\")\n";
    }
}

sub parse_gettext {
    my ($str, $gt_strings) = @_;
    my @chars = split(//, $str);
    my $escaped = 0;
    my $gt_mode = 0;
    my $gt_index = -1;
    my $i = 0;
    my $buf = '';

    while(1) {
        if ($i == @chars) {
            last;
        }
        if ($chars[$i] eq '\\') {
            $escaped = 0;
            if ($chars[$i+1] eq '\\') {
                $buf .= '\\';
                $i += 2;
                next;
            }
            elsif ($chars[$i+1] eq '[' || $chars[$i+1] eq ']') {
                $escaped = 1;
            }
            else {
                $buf .= '\\';
            }
        }
        elsif ($chars[$i] eq '[' && $chars[$i+1] eq '[') {
            if ($gt_mode) {
                if ($escaped) {
                    $escaped = 0;
                    $buf .= '[';
                    $gt_strings->[$gt_index] .= '[';
                }
                else {
                    $buf .= '[';
                    $gt_strings->[$gt_index] .= '[';                  
                }
            }
            else {
                if ($escaped) {
                    $escaped = 0;
                    $buf .= '[';
                }
                else {
                    $gt_mode = 1;
                    $gt_index++;
                    $i += 2;
                    next;
                }
            }
        }
        elsif ($chars[$i] eq ']' && $chars[$i+1] eq ']') {
            if ($gt_mode) {
                if ($escaped) {
                    $escaped = 0;
                    $buf .= ']';
                    $gt_strings->[$gt_index] .= ']';
                }
                else {
                    $gt_mode = 0;
                    $i += 2;
                    next;
                }
            }
            else {
                if ($escaped) {
                    $escaped = 0;
                    $buf .= ']';
                }
                else {
                    $buf .= ']';
                }
            }
        }
        else {
            $escaped = 0;
            if ($gt_mode) {
                $gt_strings->[$gt_index] .= $chars[$i];
            }
            $buf .= $chars[$i];
        }
        $i++;
    }
    return $buf;
}
