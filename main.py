import streamlit as st
import pandas as pd
import numpy as np
from playsound import playsound
from pygame import mixer


st.title('Guerrilla Gardens')

am_button = st.button('Am')
bdim_button = st.button('B dim')

mixer.init()

if am_button:
    mixer.music.load('fart.mp3')
    mixer.music.play(loops=-1)


if bdim_button:
    mixer.music.load('wait.mp3')
    mixer.music.play(loops=-1)
