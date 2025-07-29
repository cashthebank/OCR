import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("EasyOCR with Streamlit")
#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")
st.markdown("")

#image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])


@st.cache_resource
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by [Aarya]")
