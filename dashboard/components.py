import streamlit as st

def header():

    st.markdown("""
    <h1 style='text-align:center; color:white;'>
        🚖 Uber Real-Time Analytics Dashboard
    </h1>
    """, unsafe_allow_html=True)

    st.caption(
        "Kafka 🟢 | Flink 🟢 | Producer 🟢 | Streamlit 🟢"
    )

    st.markdown("---")