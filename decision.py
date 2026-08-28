def make_final_decision(agent_results, debate):

    technical = agent_results[0]
    hr = agent_results[1]
    hiring = agent_results[2]
    skeptic = agent_results[3]

    strengths = []
    concerns = []

    # ==========================================
    # START WITH HIRING MANAGER
    # ==========================================

    decision_score = hiring["score"]


    # ==========================================
    # TECHNICAL EVIDENCE
    # ==========================================

    if technical["score"] >= 7:

        decision_score += 1

        strengths.append(
            "Technical Agent found strong evidence of relevant skills."
        )

    else:

        decision_score -= 1

        concerns.append(
            "Technical Agent found limited evidence of role-relevant skills."
        )


    # ==========================================
    # HR EVIDENCE
    # ==========================================

    if hr["score"] >= 7:

        decision_score += 1

        strengths.append(
            "HR Agent found positive evidence of professional or teamwork fit."
        )

    else:

        decision_score -= 1

        concerns.append(
            "HR Agent found limited evidence of communication or teamwork."
        )


    # ==========================================
    # SKEPTIC WEIGHT
    # ==========================================

    if skeptic["score"] <= 5:

        decision_score -= 2

        concerns.append(
            "Skeptic Agent identified evidence gaps requiring verification."
        )

    elif skeptic["score"] >= 7:

        strengths.append(
            "Skeptic Agent did not identify major evidence concerns."
        )


    # ==========================================
    # DETECT DISAGREEMENT
    # ==========================================

    scores = [
        technical["score"],
        hr["score"],
        hiring["score"],
        skeptic["score"]
    ]

    highest_score = max(scores)
    lowest_score = min(scores)

    score_gap = highest_score - lowest_score

    if score_gap >= 3:

        disagreement = True

        concerns.append(
            f"Agents disagreed significantly, with a "
            f"{score_gap}-point difference between the highest "
            f"and lowest assessments."
        )

    else:

        disagreement = False


    # ==========================================
    # FINAL RECOMMENDATION
    # ==========================================

    if decision_score >= 9:

        recommendation = "STRONG HIRE"
        confidence = "High"

    elif decision_score >= 7:

        recommendation = "HIRE / INTERVIEW"
        confidence = "Medium-High"

    elif decision_score >= 5:

        recommendation = "INTERVIEW WITH CAUTION"
        confidence = "Medium"

    else:

        recommendation = "DO NOT HIRE"
        confidence = "Low"


    # ==========================================
    # RETURN FINAL REPORT
    # ==========================================

    return {

        "recommendation": recommendation,

        "confidence": confidence,

        "decision_score": decision_score,

        "strengths": strengths,

        "concerns": concerns,

        "disagreement": disagreement

    }