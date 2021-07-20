package gdl_deva;

use Font::TTF::Scripts::GDL;

use strict;
use vars qw($VERSION @ISA);
@ISA = qw(Font::TTF::Scripts::GDL);

$VERSION = "0.01";  # RMH   2016-02-17     Original based on existing code
           "0.02";  # JDC   2017-08-10     Modified for Annapurna (Devanagari)

*read_font = \&Font::TTF::Scripts::GDL::read_font;

sub make_name
{
    my ($self, $gname, $uni, $glyph) = @_;
    # Standard protocols:
    $gname =~ s/[:\(\)\{\}]//g;     # Eliminate problematic chars
    $gname =~ s{/.*$}{}o;           # Take first name if there are several 
    
    if ($gname =~ /^Dev[A-Z]/)
    {
        # Special processing for SIL names:
        $gname =~ s/\./_/og;   # Replace dot separators with underscore (do not lc)
        $gname;
    }
    elsif ($gname =~ /^NorthIndic[A-Z]/)
    {
        # Special processing for SIL names:
        $gname =~ s/\./_/og;   # Replace dot separators with underscore (do not lc)
        $gname;
    }
    else
    {
        $self->SUPER::make_name($gname, $uni, $glyph);
    }
}

1;

=head1 AUTHOR

Bob Hallissy L<http://scripts.sil.org/>.
(see CONTRIBUTORS for other authors).

=head1 LICENSING

Copyright (c) 2016-2017, SIL International (http://www.sil.org)

This script is released under the terms of the MIT License.
For details, see the full text of the license in the file LICENSE.

=cut
