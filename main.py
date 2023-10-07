import streamlit as st
import time

from content.basics import basics

st.title("2100 Midterm Reviewer")
with st.expander("Options"):
    anim_speed = st.number_input("Animation speed (delay in seconds)", value=2.0, step=0.1)

st.subheader("Agile Development")
with st.expander("Video"):
    st.write("Please watch the following video.")
    st.video("https://youtu.be/1kK0tpTUxys?si=rQYmpslyo9752KxM")

basics_containers = basics(st)
while True:  # Active items clock
    time.sleep(anim_speed)
    if st.session_state.get("for_loop_ind_play"):
        basics_containers["for_loop_ind_con"].code(st.session_state["for_loop_ind_gen"].__next__())
