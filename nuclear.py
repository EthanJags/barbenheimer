import streamlit as st
import datetime

# Streamlit app setup
st.title("Nuclear Weapon Command Center")

# Countdown timer setup
start_time = st.session_state.get('start_time', None)
if not start_time:
    st.session_state.start_time = datetime.datetime.now()

elapsed_time = datetime.datetime.now() - st.session_state.start_time
remaining_time = datetime.timedelta(hours=3) - elapsed_time

# Display the timer
hours, remainder = divmod(remaining_time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
st.write(f"Countdown: {hours:02}:{minutes:02}:{seconds:02}")

# Text field for the launch code
launch_code = st.text_input("Enter Launch Code:")

if launch_code:
    if launch_code == "BARBENHEIMER":
        st.write("NUCLEAR WARHEAD LAUNCHED")
    else:
        st.write("WRONG CODE")

# To run this Streamlit app, save it to a file (e.g., `nuclear_app.py`) and run `streamlit run nuclear_app.py` in your terminal.
