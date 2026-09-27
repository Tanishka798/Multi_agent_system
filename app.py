import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="Multi-Agent Research System", page_icon="🔎", layout="wide")

st.title("🔎 Multi-Agent Research System")
st.caption("Search agent → Reader agent → Writer chain → Critic chain")

with st.sidebar:
    st.header("About")
    st.write(
        "This app runs a 4-stage pipeline:\n\n"
        "1. **Search Agent** – finds relevant sources\n"
        "2. **Reader Agent** – scrapes the best URL\n"
        "3. **Writer Chain** – drafts a research report\n"
        "4. **Critic Chain** – reviews and scores the report"
    )

topic = st.text_input("Enter a research topic", placeholder="e.g. climate change")
run_button = st.button("Run Research Pipeline", type="primary", disabled=not topic.strip())

if "state" not in st.session_state:
    st.session_state.state = None

if run_button and topic.strip():
    progress_placeholder = st.empty()
    status = st.status("Running pipeline...", expanded=True)

    try:
        with status:
            st.write("Step 1: Search agent is working...")
            st.write("Step 2: Reader agent will scrape the top result...")
            st.write("Step 3: Writer will draft the report...")
            st.write("Step 4: Critic will review the report...")
            st.write("This may take a minute — running all steps now.")

            result = run_research_pipeline(topic.strip())
            st.session_state.state = result

        status.update(label="Pipeline complete ✅", state="complete", expanded=False)
    except Exception as e:
        status.update(label="Pipeline failed ❌", state="error", expanded=True)
        st.error(f"Something went wrong: {e}")

state = st.session_state.state

if state:
    tab_report, tab_critic, tab_search, tab_scraped = st.tabs(
        ["📄 Report", "🧐 Critic Review", "🔍 Search Results", "📚 Scraped Content"]
    )

    with tab_report:
        st.subheader("Final Research Report")
        st.markdown(state.get("report", "No report generated."))
        st.download_button(
            "Download Report (.md)",
            data=state.get("report", ""),
            file_name=f"{topic.strip().replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

    with tab_critic:
        st.subheader("Critic's Evaluation")
        st.markdown(state.get("critic_report", "No critic review generated."))

    with tab_search:
        st.subheader("Raw Search Results")
        st.text_area(
            "Search Agent Output",
            value=state.get("search_results", ""),
            height=300,
        )

    with tab_scraped:
        st.subheader("Scraped Content")
        st.text_area(
            "Reader Agent Output",
            value=state.get("scraped_content", ""),
            height=300,
        )
else:
    st.info("Enter a topic and click **Run Research Pipeline** to get started.")