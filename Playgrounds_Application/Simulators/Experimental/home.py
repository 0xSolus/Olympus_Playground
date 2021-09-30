# ==============THE LIBRARIES
# region Description: Import all required libraries for this simulator
from pycoingecko import CoinGeckoAPI # Coin gecko API: Pulls live data from coin gecko
import math  # Needed for basic math operations\n",
import pandas as pd  # Needed fpr dataframe creation and operations\n",
import numpy as np  # Needed for array manipulations\n",
from itertools import islice  # Needed for more complex row and coloumn slicing\n",
import matplotlib.pyplot as plt  # Needed for quickly ploting results"
import pathlib  # url management
import plotly.express as px  # cleaner graphs
import plotly.graph_objects as go  # cleaner graphs
import streamlit as st
from PIL import Image
import pathlib
from pathlib import Path
# endregion


data_metrics_mission = Path(__file__).parents[1] / 'Assets/ark_transparent.png'
data_metrics_mission  = Image.open(data_metrics_mission)

data_metrics_vision = Path(__file__).parents[1] / 'Assets/Asset_1.png'
data_metrics_vision  = Image.open(data_metrics_vision)

def app():
    # region Description: All about staking
    st.title('Welcome to your Playground!')
    st.write(
        '''
        Olympus Playground is an interactive projection calculator for staking and bonding ohm in OlympusDAO protocol.
        The educational materials provided are sourced from the awesome gitbook created by OlympusDAO.

        Special thanks to the Data and Metrics team, without which this app will not exist! 
        ''')
    st.write('------------------')
    col1, col2 = st.columns((1,1.5))
    with col1:
        st.image(data_metrics_mission)
    with col2:
        #st.write(' ')
        #st.write(' ')
        #st.write(' ')
        #st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.subheader('Vision')
        st.write('''
        - Provide an advanced interactive simulation environment for the Olympus Protocol
        
        - Foster a community of research, development, and knowledge symmetry 

        - Reduce the barrier of entry and learning curve for the protocol by creating an intuitive yet highly descriptive simulation environment 

        - Leverage the knowledge generated by sherpa academy and provide an environment to practice lessons learned 
        ''')
    st.write('------------------')
    col3, col4 = st.columns((1,1))
    with col3:
        st.write(' ')
        st.write(' ')
        st.subheader('Mission')
        st.write('''
        Provide an isolated environment for ohmies to:
        - Speculate on a vast number of scenarios

        - Simulate staking outcomes based on interactive input parameters

        - Simulate bonding outcomes based on interactive input parameters

        - Design and simulate income strategies

        - Set goals and simulate metrics required to reach them
        ''')
    with col4:
        st.image(data_metrics_vision)
    st.write('------------------')