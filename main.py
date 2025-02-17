import streamlit as st
import pandas as pd
import numpy as np
from playsound import playsound


st.title('Guerrilla Gardens')

am_button = st.button('Am')
bdim_button = st.button('B dim')


if am_button:
    while not bdim_button:
        playsound('fart.mp3')

if bdim_button:
    while not am_button:
        playsound('wait.mp3')
