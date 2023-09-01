import streamlit as st
from PIL import Image
import replicate
import os
import requests

st.header('Text 2 Image')

with st.form("my_form"):
   api_token = st.text_input("Enter your Replicate API Token:")
   prompt = st.text_input("Enter your prompt:")

   submitted = st.form_submit_button("Submit")
   if submitted:
        os.environ["REPLICATE_API_TOKEN"] = api_token
        output = replicate.run(
            "stability-ai/sdxl:d830ba5dabf8090ec0db6c10fc862c6eb1c929e1a194a5411852d25fd954ac82",
            input={"prompt": prompt}
        )
        image = Image.open(requests.get(output[0], stream=True).raw)
        st.image(image)
