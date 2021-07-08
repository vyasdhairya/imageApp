# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:01:02 2021

@author: Dhairya
"""

import cv2
import streamlit as st
st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
