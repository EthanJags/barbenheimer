import streamlit as st
import datetime

# Custom CSS for spy-themed nuclear terminal
st.markdown(
    """
    <style>
        /* Set a spy/terminal-like font for the entire page */
        body {
            background-color: black;
            color: green;  /* Set text color to green */
            font-family: 'Courier New', Courier, monospace;
        }

        /* Input box styling */
        .stTextInput input {
            background-color: #222;
            color: green;
            border: 2px solid green;
        }

        /* Buttons */
        .stButton>button {
            background-color: green;
            color: black;
            border: 2px solid white;
            box-shadow: 0px 0px 10px rgba(0, 255, 0, 0.5);
        }

        .stButton>button:hover {
            background-color: #222;
            color: green;
            border: 2px solid green;
            cursor: pointer;
        }

        /* Explicitly set headers to green */
        h1, h2, h3, h4, h5, h6 {
            color: green;
        }

        /* Set markdown color to green */
        .stMarkdown {
            color: green;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

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
launch_code = st.text_input("Enter Nuclear Code:")

# Add a button for submitting the launch code
if st.button("Submit Code"):
    if launch_code == "BARBENHEIMER":
        st.markdown("""
            <style>
                .big-text {
                    font-size: 50px;
                    color: red;
                    animation: blinker 1s linear infinite;
                }

                @keyframes blinker {
                    50% { opacity: 0; }
                }
            </style>
            <div class="big-text">NUCLEAR WARHEAD LAUNCHED</div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .wrong-text {
                    font-size: 40px;
                    color: green;
                }
            </style>
            <div class="wrong-text">WRONG CODE</div>
            """, unsafe_allow_html=True)

# Note: Use with caution and responsibility.
