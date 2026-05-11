import streamlit as st
from app.core.ingest import IngestEngine
from app.core.generator import SOPGenerator
from app.config import PATHS

st.set_page_config(page_title="NexusFlow AI", page_icon="🚀")

st.title("🚀 NexusFlow AI Command Center")

# Sidebar for Ingestion
with st.sidebar:
    st.header("📥 Ingestion")
    if st.button("Sync /uploads folder"):
        with st.spinner("Processing files..."):
            IngestEngine().run()
            st.success("Knowledge Base Updated!")

# Main UI
tab1, tab2 = st.tabs(["Generate SOP", "Onboarding Guide"])

with tab1:
    st.subheader("Standard Operating Procedures")
    topic = st.text_input("Enter the process name (e.g., Project Alpha Deployment)")
    if st.button("Build SOP"):
        if topic:
            gen = SOPGenerator()
            with st.spinner("Llama is drafting your SOP..."):
                # Dynamically passing template and category
                result = gen.generate_sop(
                    topic, 
                    template_name="sop_template.md", 
                    category="sops"
                )
                st.markdown(result)
        else:
            st.warning("Please enter a process name.")

with tab2:
    st.subheader("Employee Onboarding")
    onboard_topic = st.text_input("Who is onboarding? (e.g., Junior Dev Onboarding)")
    if st.button("Build Guide"):
        if onboard_topic:
            gen = SOPGenerator()
            with st.spinner("Creating onboarding plan..."):
                # Dynamically passing template and category
                result = gen.generate_sop(
                    onboard_topic, 
                    template_name="onboarding_template.md", 
                    category="onboarding"
                )
                st.markdown(result)
        else:
            st.warning("Please enter an onboarding role or name.")

st.divider()
st.caption("Running 100% locally on Ollama | F: Drive Storage")