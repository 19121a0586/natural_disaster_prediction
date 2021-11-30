import streamlit
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Earthquake prediction")
df=pd.read_csv("japanearthquake.csv")
st.write(df)
st.write(df.shape)
import pickle 
pickle_in=open('finalized_model.sav','rb')
classifier=pickle.load(pickle_in)
Lat=st.number_input("latitude")
if st.button("Predict"): 
        result = classifier.predict([[Lat]])
        st.success('earthquake prediction {}'.format(result))
        print(result)