import streamlit as st
coluna = st.columns(4)

numero1=st.text_input('digite um numero')
numero2=st.text_input('digite um numero2')

with coluna[0]:
    st.write('somar')

    if st.button('enviar '):
        resultado= int(numero1)+ int(numero2)
        st.text(f'o resultado é {resultado}')
    

with coluna[1]:
    st.write('subtração')
    if st.button('enviar  '):
        resultado= int(numero1)- int(numero2)
        st.text(f'o resultado é {resultado}')
    
with coluna[2]:
    st.write('multiplicação')
    if st.button('enviar   '):
        resultado= int(numero1)* int(numero2)
        st.text(f'o resultado é {resultado}')
    
with coluna[3]:
    st.write('divisão    ')
    if st.button('enviar'):
        resultado= int(numero1)/ int(numero2)
        st.text(f'o resultado é {resultado}')
    

