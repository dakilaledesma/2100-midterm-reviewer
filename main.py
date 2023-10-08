import streamlit as st
import time

from content import *

st.set_page_config(layout="wide")

st.title("2100 Midterm Reviewer")
st.markdown("""
    This reviewer was written in "pure" Python using Streamlit. You can check out the source code 
    [here](https://github.com/dakilaledesma/2100-midterm-reviewer). 
""")

with st.sidebar:
    st.subheader("Table of Contents")
    st.markdown("""
    - [Agile Development](#agile-development)
        - Video
    - [Git & GitHub](#git-github)
        - Slides
    - [Python Basics](#python-basics)
        - Variables
        - Default Data types
        - Common Operators
        - If Statements
        - Loops
    - [Functions](#functions)
        - Basics
        - Recursion (know concept for midterm)
        - Optional reading: Why use recursion?
    - [Further Concepts](#further-concepts)
        - Multiple Assignment
        - Mutability
        - Multidimensional Collections
        - Scope
        - Exceptions and try-except statements
    """)

    st.markdown("""---""")
    st.subheader("Settings")
    anim_speed = st.number_input("Simulation speed (delay in seconds)", value=2.0, step=0.1)
    # play_anims = st.checkbox("Play/Pause animations", value=False)

st.header("Agile Development")
with st.expander("Video"):
    st.write("Please watch the following video.")
    st.video("https://youtu.be/1kK0tpTUxys?si=rQYmpslyo9752KxM")

st.header("Git & GitHub")
with st.expander("Slides"):
    st.write("View on Google Slides: https://docs.google.com/presentation/d/1Zo8uy1fdvfM-9QcEVi7CCmkf6pwRCLYt8bFitXJkXrM/edit?usp=sharing")
    st.markdown("""
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRHUWwG8P0gU7ALloqr57kUIpyRHn_xpUAP2vtejHTYsA9k5DYrT4xy4aiQZy1VdNVhj_xe2lOSnv3-/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    """, unsafe_allow_html=True)

st.header("Python Basics")
st.write("The following are the basic building blocks of Python. You should be familiar with these concepts.")
basics_containers = basics(st)

st.header("Functions")
functions_containers = funcs(st)

st.header("Further Concepts")
further_concepts_containers = further_concepts(st)


while True:  # Simulation/animations clock
    time.sleep(anim_speed)
    if st.session_state.get("for_loop_ind_play"):
        basics_containers["for_loop_ind_con"].code(st.session_state["for_loop_ind_gen"].__next__())

    if st.session_state.get("for_loop_val_play"):
        basics_containers["for_loop_val_con"].code(st.session_state["for_loop_val_gen"].__next__())
    # basics_containers["for_loop_ind_con"].code(st.session_state["for_loop_ind_gen"].__next__())
