# ==================================================
# PROMPT WARS — DEBATE ENGINE
# ==================================================

def run_debate(agent_results):

    technical = agent_results[0]
    hr = agent_results[1]
    hiring = agent_results[2]
    skeptic = agent_results[3]

    debate = []

    # ==================================================
    # DEBATE POINT 1
    # ==================================================

    if hiring["score"] >= technical["score"]:

        debate.append(
            "💼 Hiring Manager agrees with 🔧 Technical Agent: "
            f"the technical assessment of {technical['score']}/10 "
            "supports progressing the candidate. "
            "The Hiring Manager considers the technical evidence "
            "sufficient for further evaluation."
        )

    else:

        debate.append(
            "💼 Hiring Manager challenges 🔧 Technical Agent: "
            "the technical assessment may not demonstrate enough "
            "role-specific readiness."
        )


    # ==================================================
    # DEBATE POINT 2
    # ==================================================

    if skeptic["score"] < hiring["score"]:

        debate.append(
            "🔎 Skeptic challenges 💼 Hiring Manager: "
            "the positive hiring assessment may be too optimistic. "
            "The Skeptic identified evidence gaps that should be "
            "verified before making a final hiring decision."
        )

    else:

        debate.append(
            "🔎 Skeptic agrees with 💼 Hiring Manager: "
            "the available evidence provides reasonable support "
            "for progressing the candidate."
        )


    # ==================================================
    # DEBATE POINT 3
    # ==================================================

    if hr["score"] >= skeptic["score"]:

        debate.append(
            "👥 HR / Culture Agent responds to 🔎 Skeptic: "
            "the concerns are worth checking, but the available "
            "professional and educational evidence still suggests "
            "reasonable potential for workplace fit."
        )

    else:

        debate.append(
            "👥 HR / Culture Agent supports 🔎 Skeptic: "
            "the limited evidence means communication, teamwork, "
            "and professional behaviour should be tested directly "
            "during an interview."
        )


    # ==================================================
    # DEBATE POINT 4 — POSITION CHANGE
    # ==================================================

    if skeptic["score"] < hiring["score"]:

        debate.append(
            "🔄 Position update — 💼 Hiring Manager: "
            "After considering the Skeptic's concerns, the Hiring "
            "Manager maintains the recommendation to interview, "
            "but agrees that the candidate's claims should be "
            "verified before a final hiring decision."
        )

    else:

        debate.append(
            "🔄 Position update — 🔎 Skeptic: "
            "After reviewing the other agents' evidence, the "
            "Skeptic acknowledges that the candidate has enough "
            "supporting evidence to justify an interview, while "
            "remaining cautious about unverified claims."
        )


    # ==================================================
    # DEBATE POINT 5 — FINAL CROSS CHECK
    # ==================================================

    highest = max(
        technical["score"],
        hr["score"],
        hiring["score"],
        skeptic["score"]
    )

    lowest = min(
        technical["score"],
        hr["score"],
        hiring["score"],
        skeptic["score"]
    )

    difference = highest - lowest


    if difference >= 3:

        debate.append(
            "⚖️ Cross-check: there is meaningful disagreement "
            "between the agents. The final decision should give "
            "additional weight to the specific evidence and "
            "concerns rather than relying on the scores alone."
        )

    else:

        debate.append(
            "⚖️ Cross-check: agent assessments are relatively close. "
            "The final decision can rely more heavily on the "
            "evidence and specific concerns identified."
        )


    return debate