import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CABEÇALHO DO FORM
st.markdown("<h1 style='text-align: center;'>ANÁLISE FINANCEIRA MARACANÃ</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Escolha Público Pagante e Ticket Médio</h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
st.markdown("---")

import streamlit as st

with st.form("captura"):

    publico_alvo = st.slider("Defina o Público Pagante da Partida", min_value=10000, max_value=65000, step=1000)
    ticket_medio = st.slider("Defina o Ticket Médio da Partida", min_value=10, max_value=100, step=1)
    button = st.form_submit_button("Calcular!")

if button:
    renda_bruta = ticket_medio*publico_alvo
    despesa_fixa = 596440
    despesa_ingresso = 2*publico_alvo
    if publico_alvo <= 40000:
       despesa_operacional = 400000
    else:
        despesa_operacional = 740000
    
    despesa_bruta = (despesa_fixa + despesa_ingresso + despesa_operacional + 0.05*publico_alvo*ticket_medio)
    despesa_bruta_1 = 1.05*(despesa_fixa + despesa_ingresso + despesa_operacional)
    despesa_bruta_2 = (despesa_fixa + despesa_ingresso + despesa_operacional)
    
    #Considerando Público Pagante escolhido, qual o ticket médio e a renda bruta de breakeven
    breakeven_ticket = round(despesa_bruta_1/publico_alvo, 0)
    breakeven_renda = breakeven_ticket*publico_alvo
    
    #Considerando Ticket Médio escolhido, qual o público pagante e a renda bruta de breakeven
    estimativa_publico = (despesa_fixa + 400000)/(0.95*ticket_medio - 2)
    if estimativa_publico <= 40000:
        breakeven_publico = estimativa_publico        
    else:
      breakeven_publico = (despesa_fixa + 740000)/(0.95*ticket_medio - 2)

    if breakeven_publico > 65000:
        breakeven_publico = 0
    else:
        breakeven_publico = breakeven_publico

    breakeven_renda_2 = breakeven_publico * ticket_medio
    
    if renda_bruta > despesa_bruta:
        renda_liquida = 0.96*(renda_bruta - despesa_bruta)
    else:
        renda_liquida = (renda_bruta - despesa_bruta)

    fontsize = 25
    st.markdown("<h4 style='text-align: center;'>Público Pagante e Ticket Médio Escolhidos</b></h4>", unsafe_allow_html=True)
    markdown_amount = f"<div style='text-align:center; font-size:{fontsize}px'>{publico_alvo:.0f}</div>"
    markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {ticket_medio:.0f}</div>"
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(markdown_amount, unsafe_allow_html=True)
    with col2:
        st.markdown(markdown_amount_2, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Rendas Bruta e Líquida para Público Pagante e Ticket Médio Escolhidos</b></h4>", unsafe_allow_html=True)
    markdown_amount = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {renda_bruta:.0f}</div>"
    markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {renda_liquida:.0f}</div>"

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(markdown_amount, unsafe_allow_html=True)
    with col4:
        st.markdown(markdown_amount_2, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Ticket Médio e Renda de Breakeven para Público Pagante Escolhido</b></h4>", unsafe_allow_html=True)
    markdown_amount = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {breakeven_ticket:.0f}</div>"
    markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {breakeven_renda:.0f}</div>"

    col5, col6 = st.columns(2)
    with col5:
        st.markdown(markdown_amount, unsafe_allow_html=True)
    with col6:
        st.markdown(markdown_amount_2, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Público Pagante e Renda de Breakeven para Ticket Médio Escolhido</b></h4>", unsafe_allow_html=True)
    markdown_amount = f"<div style='text-align:center; font-size:{fontsize}px'>{breakeven_publico:.0f}</div>"
    markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {breakeven_renda_2:.0f}</div>"

    col7, col8 = st.columns(2)
    with col7:
        st.markdown(markdown_amount, unsafe_allow_html=True)
    with col8:
        st.markdown(markdown_amount_2, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("<h3 style='text-align: center;'>Rendas Bruta e Líquida para Tickets Médios Diversos e Público Pagante Escolhido</b></h3>", unsafe_allow_html=True)

    if publico_alvo <= 40000:
        rendabruta_values = (30*publico_alvo, 35*publico_alvo, 40*publico_alvo, 45*publico_alvo, 50*publico_alvo, 
                             55*publico_alvo, 60*publico_alvo, 70*publico_alvo, 80*publico_alvo, 90*publico_alvo, 
                             100*publico_alvo)
        if 30*publico_alvo >= breakeven_renda:
            rendaliquida_30 = int(0.96*(0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int(0.96*(0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int(0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (30*publico_alvo < breakeven_renda and 35*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int(0.96*(0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int(0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (35*publico_alvo < breakeven_renda  and 40*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int(0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (40*publico_alvo < breakeven_renda and 45*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (45*publico_alvo < breakeven_renda and 50*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (50*publico_alvo < breakeven_renda and 55*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (55*publico_alvo < breakeven_renda and 60*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (60*publico_alvo < breakeven_renda and 70*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (70*publico_alvo < breakeven_renda and 80*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (80*publico_alvo < breakeven_renda and 90*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (90*publico_alvo < breakeven_renda and 100*publico_alvo >= breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int((0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        else:
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int((0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int((0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
    else:
        rendabruta_values = (30*publico_alvo, 35*publico_alvo, 40*publico_alvo, 45*publico_alvo, 50*publico_alvo, 
        55*publico_alvo, 60*publico_alvo, 70*publico_alvo, 80*publico_alvo, 90*publico_alvo, 
        100*publico_alvo)
        if 30*publico_alvo > breakeven_renda:
            rendaliquida_30 = int(0.96*(0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int(0.96*(0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int(0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (30*publico_alvo < breakeven_renda and 35*publico_alvo > breakeven_renda):
            rendaliquida_30 = (0.95*30*publico_alvo - despesa_bruta_2)
            rendaliquida_35 = (0.96*(0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = (0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = (0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = (0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = (0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = (0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = (0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = (0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = (0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = (0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (35*publico_alvo < breakeven_renda and 40*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int(0.96*(0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (40*publico_alvo < breakeven_renda and 
              45*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int(0.96*(0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (45*publico_alvo < breakeven_renda and 50*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int(0.96*(0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (50*publico_alvo < breakeven_renda and 55*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int(0.96*(0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (55*publico_alvo < breakeven_renda and 
              60*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int(0.96*(0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (60*publico_alvo < breakeven_renda and 70*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int(0.96*(0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (70*publico_alvo < breakeven_renda and 80*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int(0.96*(0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (80*publico_alvo < breakeven_renda and
              90*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int(0.96*(0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        elif (90*publico_alvo < breakeven_renda and 100*publico_alvo > breakeven_renda):
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int((0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int(0.96*(0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
        else:
            rendaliquida_30 = int((0.95*30*publico_alvo - despesa_bruta_2))
            rendaliquida_35 = int((0.95*35*publico_alvo - despesa_bruta_2))
            rendaliquida_40 = int((0.95*40*publico_alvo - despesa_bruta_2))
            rendaliquida_45 = int((0.95*45*publico_alvo - despesa_bruta_2))
            rendaliquida_50 = int((0.95*50*publico_alvo - despesa_bruta_2))
            rendaliquida_55 = int((0.95*55*publico_alvo - despesa_bruta_2))
            rendaliquida_60 = int((0.95*60*publico_alvo - despesa_bruta_2))
            rendaliquida_70 = int((0.95*70*publico_alvo - despesa_bruta_2))
            rendaliquida_80 = int((0.95*80*publico_alvo - despesa_bruta_2))
            rendaliquida_90 = int((0.95*90*publico_alvo - despesa_bruta_2))
            rendaliquida_100 = int((0.95*100*publico_alvo - despesa_bruta_2))
            rendaliquida_values = (rendaliquida_30, rendaliquida_35, rendaliquida_40, rendaliquida_45, rendaliquida_50, 
                                   rendaliquida_55, rendaliquida_60, rendaliquida_70, rendaliquida_80, rendaliquida_90, 
                                   rendaliquida_100)
    
    #Gráfico 1 - público fixo
    plt.rcParams["figure.figsize"] = [7, 5.0]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams['figure.constrained_layout.use'] = True
    plt.rcParams.update({'font.size': 9})

    ticket = [30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100]
    rendabruta_values = (round(30*publico_alvo/1000, 0), round(35*publico_alvo/1000, 0), round(40*publico_alvo/1000, 0), round(45*publico_alvo/1000, 0), round(50*publico_alvo/1000, 0), 
                        round(55*publico_alvo/1000, 0), round(60*publico_alvo/1000, 0), round(70*publico_alvo/1000, 0), round(80*publico_alvo/1000, 0), round(90*publico_alvo/1000, 0), 
                        round(100*publico_alvo/1000, 0))
    rendaliquida_values = (round(rendaliquida_30/1000, 0), round(rendaliquida_35/1000, 0), round(rendaliquida_40/1000, 0), round(rendaliquida_45/1000, 0), round(rendaliquida_50/1000, 0), 
                            round(rendaliquida_55/1000, 0), round(rendaliquida_60/1000, 0), round(rendaliquida_70/1000, 0), round(rendaliquida_80/1000, 0), round(rendaliquida_90/1000, 0), 
                            round(rendaliquida_100/1000, 0))

    ind = np.arange(len(ticket)) # the x locations for the groups
    width = 0.2 # the width of the bars
    objects = ('Renda Bruta', 'Renda Líquida')

    fig, ax = plt.subplots(layout='constrained')
    rects1 = ax.bar(ind - width/2, rendabruta_values, width, zorder=1, color='lightcoral', alpha=1)
    rects2 = ax.bar(ind + width/2, rendaliquida_values, width, zorder=1, color='skyblue', alpha=1)

    plt.xlabel('Ticket Médio')
    ax.set_ylabel('Renda (R$ mil)')
    ax.set_title('Rendas Bruta e Líquida - Público Fixo', fontsize = 13, fontweight="bold")
    ax.set_xticks(ind)
    ax.set_xticklabels(('30', '35', '40', '45', '50', '55', '60', '70', '80', '90', '100'))
    ax.legend(labels=objects, bbox_to_anchor=(1.04, 0.5), loc='center left', borderaxespad=0, fontsize=9.5, frameon=False)
    ax.autoscale(enable=None, tight=False)

    def autolabel(rects, xpos='center'):
        ha = {'center': 'center', 'right': 'center', 'left': 'center'}
        offset = {'center': 0, 'right': 0, 'left': 0}
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(offset[xpos]*3, 3), # use 3 points offset
                textcoords="offset points", # in both directions
                ha=ha[xpos], va='bottom')

    autolabel(rects1, "left")
    autolabel(rects2, "right")
    st.pyplot(fig)
    fig.savefig("Público_Fixo.png", dpi=600, bbox_inches="tight")

 
### AGORA O TICKET     

    if 20000*ticket_medio >= (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = int(0.96*(20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000)))
        rendaliquida_25k = int(0.96*(25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000)))
        rendaliquida_30k = int(0.96*(30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000)))
        rendaliquida_35k = int(0.96*(35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000)))
        rendaliquida_40k = int(0.96*(40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000)))
        rendaliquida_45k = int(0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000)))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 20000*ticket_medio < (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000) and 25000*ticket_medio >= (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = 0.96*(25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = 0.96*(30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = 0.96*(35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = 0.96*(40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = 0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = 0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000))
        rendaliquida_55k = 0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000))
        rendaliquida_60k = 0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000))
        rendaliquida_65k = 0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 25000*ticket_medio < (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000) and 30000*ticket_medio >= (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = int(0.96*(30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000)))
        rendaliquida_35k = int(0.96*(35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000)))
        rendaliquida_40k = int(0.96*(40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000)))
        rendaliquida_45k = int(0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000)))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 30000*ticket_medio < (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000) and 35000*ticket_medio >= (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = int(0.96*(35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000)))
        rendaliquida_40k = int(0.96*(40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000)))
        rendaliquida_45k = int(0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000)))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 35000*ticket_medio < (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000) and 40000*ticket_medio >= (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = int(0.96*(40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000)))
        rendaliquida_45k = int(0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000)))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 40000*ticket_medio < (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000) and 45000*ticket_medio >= (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = int(0.96*(45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000)))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 45000*ticket_medio < (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000) and 50000*ticket_medio >= (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = (45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = int(0.96*(50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000)))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 50000*ticket_medio < (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000) and 55000*ticket_medio >= (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = (45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = (50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000))
        rendaliquida_55k = int(0.96*(55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000)))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 55000*ticket_medio < (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000) and 60000*ticket_medio >= (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = (45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = (50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000))
        rendaliquida_55k = (55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000))
        rendaliquida_60k = int(0.96*(60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000)))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    elif 60000*ticket_medio < (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000) and 65000*ticket_medio >= (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = (45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = (50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000))
        rendaliquida_55k = (55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000))
        rendaliquida_60k = (60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000))
        rendaliquida_65k = int(0.96*(65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000)))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)

    else:
        #20000*ticket_medio >= (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000):
        rendabruta_values = (20000*ticket_medio, 25000*ticket_medio, 30000*ticket_medio, 35000*ticket_medio, 40000*ticket_medio, 
                             45000*ticket_medio, 50000*ticket_medio, 55000*ticket_medio, 60000*ticket_medio, 65000*ticket_medio)
        rendaliquida_20k = (20000*ticket_medio - (despesa_fixa + 0.05*20000*ticket_medio + 2*20000 +400000))
        rendaliquida_25k = (25000*ticket_medio - (despesa_fixa + 0.05*25000*ticket_medio + 2*25000 +400000))
        rendaliquida_30k = (30000*ticket_medio - (despesa_fixa + 0.05*30000*ticket_medio + 2*30000 +400000))
        rendaliquida_35k = (35000*ticket_medio - (despesa_fixa + 0.05*35000*ticket_medio + 2*35000 +400000))
        rendaliquida_40k = (40000*ticket_medio - (despesa_fixa + 0.05*40000*ticket_medio + 2*40000 +400000))
        rendaliquida_45k = (45000*ticket_medio - (despesa_fixa + 0.05*45000*ticket_medio + 2*45000 +740000))
        rendaliquida_50k = (50000*ticket_medio - (despesa_fixa + 0.05*50000*ticket_medio + 2*50000 +740000))
        rendaliquida_55k = (55000*ticket_medio - (despesa_fixa + 0.05*55000*ticket_medio + 2*55000 +740000))
        rendaliquida_60k = (60000*ticket_medio - (despesa_fixa + 0.05*60000*ticket_medio + 2*60000 +740000))
        rendaliquida_65k = (65000*ticket_medio - (despesa_fixa + 0.05*65000*ticket_medio + 2*65000 +740000))
        rendaliquida_values = (rendaliquida_20k, rendaliquida_25k, rendaliquida_30k, rendaliquida_35k, rendaliquida_40k, 
                                   rendaliquida_45k, rendaliquida_50k, rendaliquida_55k, rendaliquida_60k, rendaliquida_65k)


    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>Rendas Bruta e Líquida para  Públicos Pagantes Diversos e Ticket Médio Escolhido</b></h3>", unsafe_allow_html=True)


#Gráfico 2 - Ticket fixo
    plt.rcParams["figure.figsize"] = [7, 5]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams['figure.constrained_layout.use'] = True
    plt.rcParams.update({'font.size': 9})

    publico = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
    rendabruta_values = (round(20000*ticket_medio/1000, 0), round(25000*ticket_medio/1000, 0), round(30000*ticket_medio/1000, 0), round(35000*ticket_medio/1000, 0), round(40000*ticket_medio/1000, 0), 
                        round(45000*ticket_medio/1000, 0), round(50000*ticket_medio/1000, 0), round(55000*ticket_medio/1000, 0), round(60000*ticket_medio/1000, 0), round(65000*ticket_medio/1000, 0))
    rendaliquida_values = (round(rendaliquida_20k/1000, 0), round(rendaliquida_25k/1000, 0), round(rendaliquida_30k/1000, 0), round(rendaliquida_35k/1000, 0), round(rendaliquida_40k/1000, 0), 
                            round(rendaliquida_45k/1000, 0), round(rendaliquida_50k/1000, 0), round(rendaliquida_55k/1000, 0), round(rendaliquida_60k/1000, 0), round(rendaliquida_65k/1000, 0))

    ind = np.arange(len(publico)) # the x locations for the groups
    width = 0.2 # the width of the bars
    objects = ('Renda Bruta', 'Renda Líquida')

    fig, ax = plt.subplots(layout='constrained')
    rects1 = ax.bar(ind - width/2, rendabruta_values, width, zorder=1, color='lightcoral', alpha=1)
    rects2 = ax.bar(ind + width/2, rendaliquida_values, width, zorder=1, color='skyblue', alpha=1)

    plt.xlabel('Público Pagante')
    ax.set_ylabel('Renda (R$ mil)')
    ax.set_title('Rendas Bruta e Líquida - Ticket Fixo', fontsize = 13, fontweight="bold")
    ax.set_xticks(ind)
    ax.set_xticklabels(('20k', '25k', '30k', '35k', '40k', '45k', '50k', '55k', '60k', '65k'))
    ax.legend(labels=objects, bbox_to_anchor=(1.04, 0.5), loc='center left', borderaxespad=0, fontsize=9.5, frameon=False)
    ax.autoscale(enable=None, tight=False)

    def autolabel(rects, xpos='center'):
        ha = {'center': 'center', 'right': 'center', 'left': 'center'}
        offset = {'center': 0, 'right': 0, 'left': 0}
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(offset[xpos]*3, 3), # use 3 points offset
                textcoords="offset points", # in both directions
                ha=ha[xpos], va='bottom')

    autolabel(rects1, "left")
    autolabel(rects2, "right")
    st.pyplot(fig)
    fig.savefig("Ticket_Fixo.png", dpi=600, bbox_inches="tight")

