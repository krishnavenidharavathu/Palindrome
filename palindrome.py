import streamlit as st
st.title("Fib series")
a=st.text_input(label="enter the postion of number")
st.button("submit",type="primary")
b=a[::-1]
if (a==b):
    st.title("palindrome")
else:
    st.title("Not palindrome")
