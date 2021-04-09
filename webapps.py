import streamlit as st
import cv2
from PIL import Image
import numpy as np

def segment(our_image):
    img = np.array(our_image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Z = gray.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 3
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((gray.shape))
    ret, res2 = cv2. threshold(res2,res2.max()-15,255,cv2.THRESH_BINARY)
    return res2


def main():
    """Image App"""

    st.title("Created By Dhairya Vyas")

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Image App</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)

    if st.button("Segmented"):
        result_img= segment(our_image)
        st.image(result_img)


if __name__ == '__main__':
    main()