import streamlit as st
import pandas as pd
from pandasai.llm import OpenAI,Falcon,Starcoder
from pandasai import SmartDataframe
import matplotlib.pyplot as plt


st.title("CSV Analyzer")

llm=OpenAI(api_token=OPENAI_API_KEY)

llm_model = st.radio("LLM Model",["OpenAI", "Falcon", "Starcoder"],horizontal=True)

if llm_model is not None:
    if llm_model=="OpenAI":
        llm=OpenAI(api_token=OPENAI_API_KEY)
    elif llm_model=="Falcon":
        llm=Falcon(api_token=HUGGINGFACE_API_KEY)
    else:
        llm=Starcoder(api_token=HUGGINGFACE_API_KEY)
else:
    st.write(":red[Please Select LLM Model]")


csv_file = st.file_uploader("Click to Browse CSV File",type="csv")

if csv_file is not None:
    df=pd.read_csv(csv_file)
    model=SmartDataframe(df,config={"llm":llm})
    st.write(df.head(5))


prompt=st.text_input(label="Prompt")
button=st.button(label="Generate Response")

if button:
    if prompt:
        with st.spinner("Generating response..."):
            response=model.chat(prompt)
            if response==None:
                img= plt.imread('temp_chart.png')
                st.image(img)
            else:
                st.text_input(label="Output",value=response)
    else:
        st.write(":red[Please Write the Prompt]")







