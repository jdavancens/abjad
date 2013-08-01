# -*- encoding: utf-8 -*-
from abjad.tools.pitchtools.IntervalSegment import IntervalSegment


class HarmonicDiatonicIntervalSegment(IntervalSegment):
    '''Abjad model of harmonic diatonic interval segment:

    ::

        >>> pitchtools.HarmonicDiatonicIntervalSegment('m2 M9 m3 M3')
        HarmonicDiatonicIntervalSegment('m2 M9 m3 M3')

    Harmonic diatonic interval segments are immutable.
    '''

    ### CONSTRUCTOR ###

    def __new__(self, arg):
        from abjad.tools import pitchtools
        if isinstance(arg, str):
            harmonic_diatonic_interval_tokens = arg.split()
        else:
            harmonic_diatonic_interval_tokens = arg
        hdis = []
        for token in harmonic_diatonic_interval_tokens:
            hdi = pitchtools.HarmonicDiatonicInterval(token)
            hdis.append(hdi)
        return tuple.__new__(self, hdis)

    ### SPECIAL METHODS ###

    def __copy__(self):
        return type(self)(self.intervals)

    def __repr__(self):
        return "%s('%s')" % (
            self._class_name, ' '.join([str(x) for x in self]))

    ### PUBLIC PROPERTIES ###

    @property
    def harmonic_chromatic_interval_segment(self):
        from abjad.tools import pitchtools
        return pitchtools.HarmonicChromaticIntervalSegment(self)

    @property
    def melodic_chromatic_interval_segment(self):
        from abjad.tools import pitchtools
        return pitchtools.MelodicChromaticIntervalSegment(self)

    @property
    def melodic_diatonic_interval_segment(self):
        from abjad.tools import pitchtools
        return pitchtools.MelodicDiatonicIntervalSegment(self)
