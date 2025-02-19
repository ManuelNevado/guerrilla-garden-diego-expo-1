import streamlit as st
from pygame import mixer


st.title('////////////////////')

am_button = st.button('Am9')
bdim_button = st.button('Bdim7')
bb_button = st.button('Bb7#11')
cmaj_button = st.button('Cmaj9')
dhalfdim_button = st.button('Dhalf-dim')
eb_button = st.button('E7b13')
fmaj_button = st.button('Fmaj7#11')
fmmaj7_button = st.button('FmMaj7')
gb_button = st.button('G7b5b13')
stop_button = st.button('STOP')


mixer.init()

if am_button:
    mixer.music.load('Am9.wav')
    mixer.music.play(loops=-1)


if bdim_button:
    mixer.music.load('Bb7#11.wav')
    mixer.music.play(loops=-1)


if bb_button:
    mixer.music.load('Bdim7.wav')
    mixer.music.play(loops=-1)

if cmaj_button:
    mixer.music.load('Cmaj9.wav')
    mixer.music.play(loops=-1)

if dhalfdim_button:
    mixer.music.load('D half-dim.wav')
    mixer.music.play(loops=-1)

if eb_button:
    mixer.music.load('E7b13.wav')
    mixer.music.play(loops=-1)

if fmaj_button:
    mixer.music.load('Fmaj7#11.wav')
    mixer.music.play(loops=-1)

if fmmaj7_button:
    mixer.music.load('FmMaj7.wav')
    mixer.music.play(loops=-1)

if gb_button:
    mixer.music.load('G7b5b13.wav')
    mixer.music.play(loops=-1)

if stop_button:
    mixer.music.stop()
