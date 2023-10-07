import streamlit as st
import time

from content.basics import basics

st.set_page_config(layout="wide")

st.title("2100 Midterm Reviewer")
st.markdown("""
    This reviewer was written in "pure" Python using Streamlit. For advanced users, you can check out the source code 
    [here](https://github.com/dakilaledesma/2100-midterm-reviewer) (though it is not for the faint of heart). 
""")

with st.sidebar:
    st.subheader("Settings")
    anim_speed = st.number_input("Simulation speed (delay in seconds)", value=2.0, step=0.1)
    # play_anims = st.checkbox("Play/Pause animations", value=False)

st.header("Agile Development")
with st.expander("Video"):
    st.write("Please watch the following video.")
    st.video("https://youtu.be/1kK0tpTUxys?si=rQYmpslyo9752KxM")

st.header("Python Basics")
basics_containers = basics(st)


while True:  # Simulation/animations clock
    time.sleep(anim_speed)
    if st.session_state.get("for_loop_ind_play"):
        basics_containers["for_loop_ind_con"].code(st.session_state["for_loop_ind_gen"].__next__())

    if st.session_state.get("for_loop_val_play"):
        basics_containers["for_loop_val_con"].code(st.session_state["for_loop_val_gen"].__next__())
    # basics_containers["for_loop_ind_con"].code(st.session_state["for_loop_ind_gen"].__next__())
