import streamlit as st
import numpy as np


def calc_log(x):
    return np.log(x)


# ЗДЕСЬ НАЧИНАЕТСЯ ОПИСАНИЕ ИНТЕРФЕЙСА

# добавить слайдер с выбором от 18 до 60
x = st.slider("Выберите свой возраст", min_value=18, max_value=60)

# обработка результатов выбора
if x < 30:
    st.write("Какой вы молодой!")
if 30 <= x < 50:
    st.write("В расцвете сил!")
if x >= 50:
    st.write("Старичок, пора в гробик на бочок!")

# задаем заголовок и в поле ввода считываем значние в переменную value
st.header("Посчитать вам логариф от числа?")
value = st.number_input("Введите число", 1, 1000)

if value:
    st.write(value, " логарифм будет: ", calc_log(value))
