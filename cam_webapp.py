# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 01:03:38 2021

@author: Dhairya
"""

  
import streamlit as st

from PIL import Image
import numpy as np
import cv2

DEMO_IMAGE = 'djv.png'

#title of the web-app
st.title('QR Code Decoding with OpenCV')

@st.cache
def show_qr_detection(img,pts):
    
    pts = np.int32(pts).reshape(-1, 2)
    
    for j in range(pts.shape[0]):
        
        cv2.line(img, tuple(pts[j]), tuple(pts[(j + 1) % pts.shape[0]]), (255, 0, 0), 5)
        
    for j in range(pts.shape[0]):
        cv2.circle(img, tuple(pts[j]), 10, (255, 0, 255), -1)


@st.cache
def qr_code_dec(image):
    
    decoder = cv2.QRCodeDetector()
    
    data, vertices, rectified_qr_code = decoder.detectAndDecode(image)
    
    if len(data) > 0:
        print("Decoded Data: '{}'".format(data))

    # Show the detection in the image:
        show_qr_detection(image, vertices)
        
        rectified_image = np.uint8(rectified_qr_code)
        
        decoded_data = 'Decoded data: '+ data
        
        rectified_image = cv2.putText(rectified_image,decoded_data,(50,350),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 2,
            color = (250,225,100),thickness =  3, lineType=cv2.LINE_AA)
        
        
    return decoded_data


    
    
st.markdown("**Warning** Only add QR-code Images, other images will give out an error")


#uploading the imges
img_file_buffer = st.file_uploader("Upload an image which you want to Decode", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))


st.subheader('Orginal Image')

#display the image
st.image(image, caption="Original Image", use_column_width=True) 



st.subheader('Decoded data')

decoded_data = qr_code_dec(image)
st.markdown(decoded_data)
