# -*- encoding: utf-8 -*-
from abjad.tools import contexttools


def apply_dynamic_marks(score):

    voice = score['Bell Voice']
    dynamic = contexttools.DynamicMark('ppp')
    dynamic.attach(voice[0][1])
    dynamic = contexttools.DynamicMark('pp')
    dynamic.attach(voice[8][1])
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[18][1])
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[26][1])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[34][1])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[42][1])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[52][1])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[60][1])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[68][1])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[76][1])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[84][1])
    dynamic = contexttools.DynamicMark('pp')
    dynamic.attach(voice[-1][0])

    voice = score['First Violin Voice']
    dynamic = contexttools.DynamicMark('ppp')
    dynamic.attach(voice[6][1])
    dynamic = contexttools.DynamicMark('pp')
    dynamic.attach(voice[15][0])
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[22][3])
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[31][0])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[38][3])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[47][0])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[55][2])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[62][2])

    voice = score['Second Violin Voice']
    dynamic = contexttools.DynamicMark('pp')
    dynamic.attach(voice[7][0])
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[12][0])
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[16][0])
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[25][1])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[34][1])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[44][1])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[54][0])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[62][1])

    voice = score['Viola Voice']
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[8][0])
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[19][1])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[30][0])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[36][0])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[42][0])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[52][0])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[62][0])

    voice = score['Cello Voice']
    dynamic = contexttools.DynamicMark('p')
    dynamic.attach(voice[10][0])
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[21][0])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[31][0])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[43][0])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[52][1])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[62][0])

    voice = score['Bass Voice']
    dynamic = contexttools.DynamicMark('mp')
    dynamic.attach(voice[14][0])
    dynamic = contexttools.DynamicMark('mf')
    dynamic.attach(voice[27][0])
    dynamic = contexttools.DynamicMark('f')
    dynamic.attach(voice[39][0])
    dynamic = contexttools.DynamicMark('ff')
    dynamic.attach(voice[51][0])
    dynamic = contexttools.DynamicMark('fff')
    dynamic.attach(voice[62][0])
