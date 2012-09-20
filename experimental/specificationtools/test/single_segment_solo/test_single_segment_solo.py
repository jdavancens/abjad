from abjad.tools import *
from experimental import *


def test_single_segment_solo_01():
    '''Single division with duration less than segment.
    Division interprets cyclically.
    Division truncates at end of score.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)

    segment = score_specification.make_segment('red')
    segment.set_time_signatures([(4, 8), (3, 8)])
    segment.set_divisions([(3, 16)], contexts=segment.v1)
    segment.set_rhythm(library.thirty_seconds)

    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)

    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_02():
    '''Single division with duration equal to segment.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    
    segment = score_specification.make_segment('red')
    segment.set_time_signatures([(4, 8), (3, 8)])
    segment.set_divisions([(14, 16)], contexts=segment.v1)
    segment.set_rhythm(library.thirty_seconds)

    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)

    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_03():
    '''Single division with duration greater than segment.
    Division truncates at end of score.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    
    segment = score_specification.make_segment('red')
    segment.set_time_signatures([(4, 8), (3, 8)])
    segment.set_divisions([(20, 16)], contexts=segment.v1)
    segment.set_rhythm(library.thirty_seconds)

    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)

    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)
