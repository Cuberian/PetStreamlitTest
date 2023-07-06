import streamlit as st

x = st.slider("Выберите свой возраст", min_value=18, max_value=60)

if x < 30:
    st.write("Какой вы молодой!")
if 30 <= x < 50:
    st.write("В расцвете сил!")
if x >= 50:
    st.write("Старичок, пора в гробик на бочок!")
