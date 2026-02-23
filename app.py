import streamlit as st

st.set_page_config(page_title="AI Impact Summit 2026", layout="wide")

st.title("AI Impact Summit 2026")
st.markdown("### Empowering Innovation • Digital Transformation • AI for Enterprise")

st.markdown("---")

st.header("About The Summit")
st.write("""
AI Impact Summit 2026 brings together global AI leaders,
enterprise innovators, policymakers, startups, and researchers.
""")

st.header("Key Speakers")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("AI Industry Leader")
    st.write("Global AI Strategy & Innovation")

with col2:
    st.subheader("Government Policy Expert")
    st.write("AI Governance & Regulation")

with col3:
    st.subheader("Tech Founder")
    st.write("AI Startups & Innovation")

st.header("Agenda")
st.subheader("Day 1")
st.write("- AI in Governance")
st.write("- AI for Infrastructure")
st.write("- AI Startups")

st.subheader("Day 2")
st.write("- Generative AI & LLMs")
st.write("- Enterprise AI")
st.write("- Responsible AI")

st.header("Register")
name = st.text_input("Full Name")
email = st.text_input("Email")

if st.button("Submit"):
    st.success(f"Thank you {name}, registration received!")

st.caption("© 2026 AI Impact Summit")
