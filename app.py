import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wage = pd.read_csv("datos.csv")

st.title("Analisis Salario")

tab1, tab2 = st.tabs(["Tab1", "Tab2"])



with tab1:
    st.header("Analisis Univariado")
   #analisis univariado
    fig, ax = plt.subplots(1,4, figsize = (10,4))
#años
    ax[0].hist(wage['Años'])
    ax[0].set_title("Experiencia")
    ax[0].set_xlabel("Experiencia")


#sexo
    conteo = wage['Sexo'].value_counts()
    ax[1].bar(conteo.index, conteo.values)
    ax[1].set_title("Sexo")
    ax[1].set_xlabel("Genero")


#salario
    ax[2].hist(wage['educación'])
    ax[2].set_title("educación")
    ax[2].set_xlabel("educación")


    ax[3].hist(wage['Salario'])
    ax[3].set_xlabel('salario')

    fig.tight_layout()
    st.pyplot(fig)



with tab2:
    st.header("Analisis Bivariado")
   #ANALISIS BIVARIADO

    fig, ax = plt.subplots(1,3, figsize = (11,5))

#años vs salario

    sns.scatterplot(data = wage, x ='Años', y = 'Salario', ax = ax[0])      #scatterplot da el tipo de grafica
#sexo vs salario

    sns.violinplot(data=wage, x = 'Sexo', y = 'Salario', ax = ax[1])           #boxplot el tipo de grafica             #violinplot para grafica de forma violín

#educación vs salario

    sns.scatterplot(data = wage, x ='educación', y = 'Salario', ax = ax[2])

    fig.tight_layout() 
    st.pyplot(fig) 

    



