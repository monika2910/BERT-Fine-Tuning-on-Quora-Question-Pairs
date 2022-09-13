import streamlit as st
import helper_bert

import transformers




st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    result = helper_bert.check_similarity(q1,q2)
    #result = model2.predict(query)[0]
    print("in app.py")
    print(result)
    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


