# ==================================================
# PROMPT WARS — INDEPENDENT AI AGENTS
# ==================================================

import re


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def text_contains(text, keywords):
    """
    Check whether any keyword appears in the text.
    """
    text = text.lower()

    for keyword in keywords:
        if keyword.lower() in text:
            return True

    return False


def find_evidence(text, keywords, label):
    """
    Find simple evidence sentences from the candidate
    documents based on relevant keywords.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+|\n+",
        text
    )

    evidence = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        lower_sentence = sentence.lower()

        for keyword in keywords:

            if keyword.lower() in lower_sentence:

                evidence.append(
                    f"{label}: {sentence}"
                )

                break

        if len(evidence) >= 2:
            break

    return evidence


# ==================================================
# TECHNICAL AGENT
# ==================================================

def technical_agent(profile, job_description):

    score = 5

    evidence = []

    skills = profile.get(
        "skills",
        []
    )

    projects = profile.get(
        "projects",
        []
    )

    experience = profile.get(
        "experience",
        []
    )


    # ----------------------------------------------
    # SKILL EVIDENCE
    # ----------------------------------------------

    if len(skills) >= 3:

        score += 2

        evidence.append(
            "Resume/profile contains multiple technical skills: "
            + ", ".join(skills[:5])
        )

    elif len(skills) >= 1:

        score += 1

        evidence.append(
            "Resume/profile lists technical skills including: "
            + ", ".join(skills[:3])
        )

    else:

        score -= 2

        evidence.append(
            "No clear technical skills were identified in the profile."
        )


    # ----------------------------------------------
    # PROJECT EVIDENCE
    # ----------------------------------------------

    if len(projects) >= 2:

        score += 1

        evidence.append(
            f"Candidate profile contains {len(projects)} "
            "project-related entries."
        )

    elif len(projects) == 1:

        score += 1

        evidence.append(
            "Candidate profile contains a project entry."
        )

    else:

        evidence.append(
            "No clear project evidence was identified."
        )


    # ----------------------------------------------
    # EXPERIENCE
    # ----------------------------------------------

    if len(experience) >= 1:

        score += 1

        evidence.append(
            "The profile contains experience-related information."
        )


    score = max(
        1,
        min(score, 10)
    )


    if score >= 8:

        opinion = (
            "The candidate demonstrates strong technical "
            "preparation based on the available skills, "
            "projects, and experience evidence."
        )

    elif score >= 6:

        opinion = (
            "The candidate demonstrates moderate technical "
            "readiness, although some areas may require "
            "further verification."
        )

    else:

        opinion = (
            "The available documents provide limited evidence "
            "of technical readiness for the target role."
        )


    return {
        "agent": "Technical Agent",
        "score": score,
        "opinion": opinion,
        "evidence": evidence[:3]
    }


# ==================================================
# HR / CULTURE AGENT
# ==================================================

def hr_agent(profile, job_description):

    score = 5

    evidence = []

    claims = profile.get(
        "claims",
        []
    )

    experience = profile.get(
        "experience",
        []
    )

    education = profile.get(
        "education",
        []
    )


    # ----------------------------------------------
    # EXPERIENCE
    # ----------------------------------------------

    if len(experience) >= 2:

        score += 2

        evidence.append(
            "Multiple experience entries provide evidence "
            "of exposure to professional or collaborative work."
        )

    elif len(experience) == 1:

        score += 1

        evidence.append(
            "An experience entry is present in the candidate profile."
        )

    else:

        evidence.append(
            "Limited direct work-experience evidence was identified."
        )


    # ----------------------------------------------
    # CLAIMS / ACHIEVEMENTS
    # ----------------------------------------------

    if len(claims) >= 2:

        score += 1

        evidence.append(
            "The profile contains multiple achievement or "
            "claim-related entries."
        )

    elif len(claims) == 1:

        evidence.append(
            "The profile contains an achievement or claim."
        )

    else:

        evidence.append(
            "No significant achievement claims were identified."
        )


    # ----------------------------------------------
    # EDUCATION
    # ----------------------------------------------

    if len(education) >= 1:

        score += 1

        evidence.append(
            "The transcript/profile provides formal education evidence."
        )


    score = max(
        1,
        min(score, 10)
    )


    if score >= 8:

        opinion = (
            "The candidate shows positive indicators of "
            "professional readiness and potential cultural fit."
        )

    elif score >= 6:

        opinion = (
            "The candidate shows some positive professional "
            "indicators, but communication and teamwork should "
            "be validated during an interview."
        )

    else:

        opinion = (
            "The available documents provide limited evidence "
            "about communication, teamwork, and workplace fit."
        )


    return {
        "agent": "HR / Culture Agent",
        "score": score,
        "opinion": opinion,
        "evidence": evidence[:3]
    }


# ==================================================
# HIRING MANAGER AGENT
# ==================================================

def hiring_manager_agent(profile, job_description):

    score = 5

    evidence = []

    skills = profile.get(
        "skills",
        []
    )

    projects = profile.get(
        "projects",
        []
    )

    experience = profile.get(
        "experience",
        []
    )


    # ----------------------------------------------
    # ROLE MATCHING
    # ----------------------------------------------

    job_lower = job_description.lower()

    matching_skills = []


    for skill in skills:

        if skill.lower() in job_lower:

            matching_skills.append(
                skill
            )


    if matching_skills:

        score += 2

        evidence.append(
            "Role-relevant skills identified: "
            + ", ".join(matching_skills[:5])
        )

    elif skills:

        score += 1

        evidence.append(
            "Candidate has technical skills, although "
            "direct job-description matches are limited."
        )

    else:

        score -= 1

        evidence.append(
            "No clear role-relevant skills were identified."
        )


    # ----------------------------------------------
    # PROJECTS
    # ----------------------------------------------

    if len(projects) >= 1:

        score += 1

        evidence.append(
            "Project experience provides evidence of practical application."
        )

    else:

        evidence.append(
            "No clear project evidence was identified."
        )


    # ----------------------------------------------
    # EXPERIENCE
    # ----------------------------------------------

    if len(experience) >= 1:

        score += 1

        evidence.append(
            "Candidate profile contains experience-related evidence."
        )


    score = max(
        1,
        min(score, 10)
    )


    if score >= 8:

        opinion = (
            "The candidate appears worth progressing to the "
            "next hiring stage based on the available role-relevant evidence."
        )

    elif score >= 6:

        opinion = (
            "The candidate may be worth interviewing, but "
            "some role-specific capabilities should be verified."
        )

    else:

        opinion = (
            "The available evidence does not strongly establish "
            "that the candidate is ready for the target role."
        )


    return {
        "agent": "Hiring Manager Agent",
        "score": score,
        "opinion": opinion,
        "evidence": evidence[:3]
    }


# ==================================================
# SKEPTIC AGENT
# ==================================================

def skeptic_agent(profile, job_description):

    score = 7

    evidence = []

    skills = profile.get(
        "skills",
        []
    )

    projects = profile.get(
        "projects",
        []
    )

    claims = profile.get(
        "claims",
        []
    )

    experience = profile.get(
        "experience",
        []
    )


    # ----------------------------------------------
    # EVIDENCE GAPS
    # ----------------------------------------------

    if not skills:

        score -= 2

        evidence.append(
            "No clear technical skills were identified."
        )


    if not projects:

        score -= 1

        evidence.append(
            "No project evidence was identified."
        )


    if not experience:

        score -= 1

        evidence.append(
            "No clear work-experience evidence was identified."
        )


    # ----------------------------------------------
    # CLAIM VERIFICATION
    # ----------------------------------------------

    if claims:

        evidence.append(
            f"The candidate profile contains {len(claims)} "
            "claim/achievement entries that should be verified "
            "against supporting evidence."
        )

        score -= 1

    else:

        evidence.append(
            "No major achievement claims were identified for verification."
        )


    # ----------------------------------------------
    # DEFAULT EVIDENCE
    # ----------------------------------------------

    if not evidence:

        evidence.append(
            "The candidate profile contains evidence across "
            "skills, projects, experience, and claims."
        )


    score = max(
        1,
        min(score, 10)
    )


    if score >= 8:

        opinion = (
            "I found relatively few obvious evidence gaps, "
            "although claims should still be verified."
        )

    elif score >= 6:

        opinion = (
            "The candidate appears plausible, but several "
            "claims or capabilities should be verified before hiring."
        )

    else:

        opinion = (
            "There are significant evidence gaps that make "
            "the candidate's claims difficult to validate."
        )


    return {
        "agent": "Skeptic Agent",
        "score": score,
        "opinion": opinion,
        "evidence": evidence[:3]
    }


# ==================================================
# RUN ALL FOUR AGENTS INDEPENDENTLY
# ==================================================

def run_independent_agents(
    profile,
    job_description
):

    technical = technical_agent(
        profile,
        job_description
    )


    hr = hr_agent(
        profile,
        job_description
    )


    hiring_manager = hiring_manager_agent(
        profile,
        job_description
    )


    skeptic = skeptic_agent(
        profile,
        job_description
    )


    # IMPORTANT:
    # Each agent was evaluated independently.
    # No agent receives another agent's result here.

    return [
        technical,
        hr,
        hiring_manager,
        skeptic
    ]