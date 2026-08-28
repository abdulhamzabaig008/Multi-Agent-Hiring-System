import streamlit as st
import plotly.express as px

from utils.document_parser import extract_text
from profile_builder import build_candidate_profile
from agents import run_independent_agents
from debate import run_debate
from decision import make_final_decision


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Multi-Agent Candidate Evaluation System",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==================================================
# SESSION STATE
# ==================================================

if "evaluation_report" not in st.session_state:
    st.session_state.evaluation_report = None
# ==================================================
# SESSION STATE
# ==================================================

if "evaluation_report" not in st.session_state:
    st.session_state.evaluation_report = None
# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Candidate Evaluation")

    st.divider()

    st.markdown("### 📋 Evaluation Pipeline")

    st.markdown("""
    **1. 📄 Documents**  
    Resume + Transcript + Job Description

    **2. 👤 Candidate Profile**  
    Extract facts, skills and claims

    **3. 🤖 Independent Agents**  
    🔧 Technical  
    👥 HR / Culture  
    💼 Hiring Manager  
    🔎 Skeptic

    **4. ⚔️ Debate**  
    Agents challenge each other

    **5. ⚖️ Final Decision**  
    Evidence + disagreement + confidence
    """)

    st.divider()

    st.markdown("### 🔐 Key Principle")

    st.info(
        "Agents evaluate independently first. "
        "They only see each other's conclusions "
        "during the debate stage."
    )

    st.divider()

    st.caption(
        "Prompt Wars • AI Hiring Evaluation Prototype"
    )
    st.divider()

    st.markdown("### 📥 Export")

    if st.session_state.evaluation_report:

        data = st.session_state.evaluation_report
        final = data["final_decision"]

        report = f"""
PROMPT WARS
CANDIDATE EVALUATION REPORT
===========================

FINAL RECOMMENDATION
--------------------
Recommendation: {final["recommendation"]}
Confidence: {final["confidence"]}
Decision Score: {final["decision_score"]}

STRENGTHS
---------
"""

        for strength in final["strengths"]:
            report += f"- {strength}\n"

        report += """
CONCERNS
--------
"""

        for concern in final["concerns"]:
            report += f"- {concern}\n"

        report += """
AGENT ASSESSMENTS
-----------------
"""

        for agent in data["agent_results"]:

            report += f"""
{agent["agent"]}
Score: {agent["score"]}/10

Opinion:
{agent["opinion"]}

Evidence:
"""

            for evidence in agent["evidence"]:
                report += f"- {evidence}\n"

        report += """
MULTI-AGENT DEBATE
------------------
"""

        for i, point in enumerate(data["debate"], 1):
            report += f"\nDebate Point {i}:\n{point}\n"

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="prompt_wars_report.txt",
            mime="text/plain"
        )

    else:

        st.caption(
            "Run an evaluation first to enable download."
        )



# ==================================================
# SIDEBAR
# ==================================================

st.markdown(
    """
    <h1 style="
        font-size: 42px;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 5px;
    ">
        Multi-Agent Candidate Evaluation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption(
    "AI-powered hiring analysis using independent personas, "
    "evidence-based reasoning, and multi-agent debate."
)
# ==================================================
# EVALUATION PIPELINE
# ==================================================

st.markdown("### 🔄 Evaluation Pipeline")

step1, step2, step3, step4, step5 = st.columns(5)

with step1:
    st.markdown("## 📄")
    st.caption("Documents")

with step2:
    st.markdown("## 👤")
    st.caption("Profile")

with step3:
    st.markdown("## 🤖")
    st.caption("Agents")

with step4:
    st.markdown("## ⚔️")
    st.caption("Debate")

with step5:
    st.markdown("## ⚖️")
    st.caption("Decision")

st.divider()



# ==================================================
# CANDIDATE DOCUMENTS
# ==================================================

st.header("📄 Candidate Documents")

col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx", "txt"]
    )

with col2:
    transcript = st.file_uploader(
        "🎓 Upload Transcript",
        type=["pdf", "docx", "txt"]
    )


# ==================================================
# JOB DESCRIPTION
# ==================================================

st.header("💼 Target Role")

job_description = st.text_area(
    "Job Description",
    height=180,
    placeholder="Paste the job description here..."
)


# ==================================================
# EVALUATION
# ==================================================

if st.button(
    "🚀 Evaluate Candidate",
    use_container_width=True
):

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------

    if resume is None:
        st.error("Please upload the resume.")
        st.stop()

    if transcript is None:
        st.error("Please upload the transcript.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter the job description.")
        st.stop()


    # --------------------------------------------------
    # READ DOCUMENTS
    # --------------------------------------------------

    with st.spinner("📖 Reading candidate documents..."):

        resume_text = extract_text(resume)
        transcript_text = extract_text(transcript)

    st.success("Documents successfully read! ✅")


    # --------------------------------------------------
    # BUILD PROFILE
    # --------------------------------------------------

    with st.spinner("👤 Building candidate profile..."):

        profile = build_candidate_profile(
            resume_text,
            transcript_text,
            job_description
        )

    st.success("Candidate profile created! ✅")


    # --------------------------------------------------
    # INDEPENDENT AGENTS
    # --------------------------------------------------

    with st.spinner(
        "🤖 Running four independent evaluations..."
    ):

        agent_results = run_independent_agents(
            profile,
            job_description
        )

    st.success(
        "All four agents completed their independent evaluations! ✅"
    )


    # ==================================================
    # INDEPENDENT OPINIONS
    # ==================================================

    st.divider()

    st.header("🤖 Independent Agent Opinions")
    st.info(
    "🔒 Independent Stage: Each persona evaluates the candidate "
    "without access to the conclusions of the other agents. "
    "The debate happens only after all four evaluations are complete."
    )

    st.caption(
        "Each agent evaluates the candidate independently "
        "before seeing the other agents' conclusions."
    )


    agent_icons = {
        "Technical Agent": "🔧",
        "HR / Culture Agent": "👥",
        "Hiring Manager Agent": "💼",
        "Skeptic Agent": "🔎"
    }


    columns = st.columns(4)


    for column, result in zip(
        columns,
        agent_results
    ):

        with column:

            icon = agent_icons.get(
                result["agent"],
                "🤖"
            )

            st.subheader(
                f"{icon} {result['agent']}"
            )

            st.metric(
                "Assessment",
                f"{result['score']}/10"
            )

            st.write(
                result["opinion"]
            )

            st.markdown("**📌 Evidence**")


            for evidence in result["evidence"]:

                st.markdown(
                    f"> {evidence}"
                )


    # ==================================================
    # SCORE OVERVIEW
    # ==================================================

    st.divider()

    st.header("📊 Agent Assessment Overview")

    agent_names = []
    agent_scores = []


    for result in agent_results:

        agent_names.append(
            result["agent"]
        )

        agent_scores.append(
            result["score"]
        )


    chart_data = {
        "Agent": agent_names,
        "Score": agent_scores
    }


    fig = px.bar(
        chart_data,
        x="Score",
        y="Agent",
        orientation="h",
        range_x=[0, 10],
        text="Score"
    )


    fig.update_layout(
        height=280,
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=20
        ),
        xaxis_title="Assessment Score",
        yaxis_title=""
    )


    fig.update_traces(
        textposition="outside"
    )


    st.plotly_chart(
        fig,
        use_container_width=False
    )


    st.caption(
        "Scores represent independent assessments. "
        "They are NOT simply averaged to produce the final decision."
    )


    # ==================================================
    # DEBATE
    # ==================================================

    st.divider()

    st.header("⚔️ Multi-Agent Debate")
    st.success(
    "🔓 Debate Stage: Agents can now respond to, challenge, "
    "and reconsider the findings of other agents."
)

    st.caption(
        "The debate begins only after all four independent "
        "evaluations have been completed."
    )


    with st.spinner(
        "⚔️ Agents are debating their findings..."
    ):

        debate = run_debate(
            agent_results
        )


    for i, point in enumerate(
        debate,
        1
    ):

        st.markdown(
            f"### Debate Point {i}"
        )

        st.info(
            point
        )


    # ==================================================
    # FINAL DECISION
    # ==================================================

    with st.spinner(
        "⚖️ Reaching final decision..."
    ):

        final_decision = make_final_decision(
            agent_results,
            debate
        )
        st.session_state.evaluation_report = {
        "final_decision": final_decision,
        "agent_results": agent_results,
        "debate": debate
        }
        # Save final results for download
        st.session_state.evaluation_report = {
        "final_decision": final_decision,
        "agent_results": agent_results,
        "debate": debate
        }


    st.divider()

    st.header("⚖️ Final Decision")


    # --------------------------------------------------
    # FINAL RECOMMENDATION
    # --------------------------------------------------

    recommendation = final_decision[
        "recommendation"
    ]


    if recommendation == "STRONG HIRE":

        st.success(
            f"### 🟢 {recommendation}"
        )

    elif recommendation == "HIRE / INTERVIEW":

        st.success(
            f"### 🟢 {recommendation}"
        )

    elif recommendation == "INTERVIEW WITH CAUTION":

        st.warning(
            f"### 🟡 {recommendation}"
        )

    else:

        st.error(
            f"### 🔴 {recommendation}"
        )


    # --------------------------------------------------
    # CONFIDENCE AND SCORE
    # --------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Recommendation",
            recommendation
        )


    with col2:

        st.metric(
            "Confidence",
            final_decision["confidence"]
        )


    
    st.markdown("### 🧠 Why this decision?")

    st.info(
    "The final recommendation is based on the independent "
    "agent assessments, their supporting evidence, the debate "
    "between agents, and identified concerns. The four scores "
    "are not simply averaged."
    )
    


    # ==================================================
    # STRENGTHS
    # ==================================================

    st.subheader("💪 Strengths")


    if final_decision["strengths"]:

        for strength in final_decision["strengths"]:

            st.success(
                f"✓ {strength}"
            )

    else:

        st.write(
            "No major strengths identified."
        )


    # ==================================================
    # CONCERNS
    # ==================================================

    st.subheader("⚠️ Concerns")


    if final_decision["concerns"]:

        for concern in final_decision["concerns"]:

            st.warning(
                f"• {concern}"
            )

    else:

        st.write(
            "No major concerns identified."
        )


    # ==================================================
    # DISAGREEMENT
    # ==================================================

    st.subheader(
        "🔎 Unresolved Disagreement"
    )


    if final_decision["disagreement"]:

        st.error(
            "The agents had significant disagreement. "
            "This should be verified during an interview."
        )

    else:

        st.success(
            "The agents reached broad agreement."
        )


    # ==================================================
    # CANDIDATE PROFILE
    # ==================================================

    st.divider()

    st.header("👤 Candidate Profile")


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("🛠️ Skills")


        if profile["skills"]:

            for skill in profile["skills"]:

                st.write(
                    f"• {skill}"
                )

        else:

            st.write(
                "No skills detected."
            )


        st.subheader("💼 Experience")


        if profile["experience"]:

            for item in profile["experience"][:5]:

                st.write(
                    f"• {item}"
                )

        else:

            st.write(
                "No clear experience detected."
            )


    with col2:

        st.subheader("🚀 Projects")


        if profile["projects"]:

            for item in profile["projects"][:5]:

                st.write(
                    f"• {item}"
                )

        else:

            st.write(
                "No clear projects detected."
            )


        st.subheader(
            "🏆 Claims / Achievements"
        )


        if profile["claims"]:

            for item in profile["claims"][:5]:

                st.write(
                    f"• {item}"
                )

        else:

            st.write(
                "No major claims detected."
            )


    # ==================================================
    # EDUCATION
    # ==================================================

    st.subheader("🎓 Education")


    if profile["education"]:

        for education in profile["education"]:

            st.write(
                f"• {education}"
            )

    else:

        st.write(
            "No education information detected."
        )
# ==================================================
# SOURCE EVIDENCE
# ==================================================

st.divider()

st.header("📚 Candidate Evidence")

if st.session_state.get("evaluation_report"):

    saved_results = st.session_state.evaluation_report["agent_results"]

    for result in saved_results:

        st.markdown(f"### 🤖 {result['agent']}")

        evidence = result.get("evidence", [])

        if evidence:
            for item in evidence:
                st.markdown(f"📌 **{item}**")
        else:
            st.caption("No evidence available.")

else:

    st.info("Run an evaluation to view candidate evidence.")


# ==================================================
# COMPLETION
# ==================================================

st.divider()

