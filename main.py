import streamlit as st
from pygame import mixer

# Custom CSS for bigger buttons
st.markdown("""
<style>
    .stButton > button {
        width: 180px;
        height: 45px;
        font-size: 16px;
        margin: 5px;
        padding: 8px;
    }
    div.row-widget.stButton {
        text-align: center;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title('////////////////////')

# Create three columns for better button layout
col1, col2, col3 = st.columns(3)

# Distribute buttons across columns
with col1:
    am_button = st.button('Am9')
    cmaj_button = st.button('Cmaj9')
    fmaj_button = st.button('Fmaj7#11')

with col2:
    bdim_button = st.button('Bdim7')
    dhalfdim_button = st.button('Dhalf-dim')
    fmmaj7_button = st.button('FmMaj7')

with col3:
    bb_button = st.button('Bb7#11')
    eb_button = st.button('E7b13')
    gb_button = st.button('G7b5b13')

# Center the stop button
_, center_col, _ = st.columns([1,1,1])
with center_col:
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
