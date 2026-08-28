def build_candidate_profile(resume_text, transcript_text, job_description):

    profile = {
        "skills": [],
        "education": [],
        "experience": [],
        "projects": [],
        "claims": [],
        "evidence": []
    }

    resume_lines = [
        line.strip()
        for line in resume_text.splitlines()
        if line.strip()
    ]

    transcript_lines = [
        line.strip()
        for line in transcript_text.splitlines()
        if line.strip()
    ]

    resume_lower = resume_text.lower()


    # ==========================================
    # SKILLS
    # ==========================================

    possible_skills = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "machine learning",
        "data structures",
        "algorithms",
        "html",
        "css",
        "javascript",
        "git",
        "github",
        "cloud",
        "aws",
        "linux",
        "react",
        "node.js"
    ]

    for skill in possible_skills:

        if skill in resume_lower:

            profile["skills"].append(skill)


    # ==========================================
    # EXPERIENCE
    # ==========================================

    experience_keywords = [
        "intern",
        "internship",
        "worked",
        "experience",
        "developer",
        "engineer",
        "company",
        "employment"
    ]

    for line in resume_lines:

        if any(
            keyword in line.lower()
            for keyword in experience_keywords
        ):

            profile["experience"].append(line)


    # ==========================================
    # PROJECTS
    # ==========================================

    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "designed",
        "application",
        "website",
        "system"
    ]

    for line in resume_lines:

        if any(
            keyword in line.lower()
            for keyword in project_keywords
        ):

            profile["projects"].append(line)


    # ==========================================
    # CLAIMS
    # ==========================================

    claim_keywords = [
        "achieved",
        "improved",
        "increased",
        "reduced",
        "led",
        "won",
        "certified",
        "award",
        "rank",
        "successfully"
    ]

    for line in resume_lines:

        if any(
            keyword in line.lower()
            for keyword in claim_keywords
        ):

            profile["claims"].append(line)


    # ==========================================
    # EDUCATION
    # ==========================================

    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "computer science",
        "engineering",
        "university",
        "college",
        "cgpa",
        "gpa",
        "semester",
        "degree"
    ]

    for line in transcript_lines:

        if any(
            keyword in line.lower()
            for keyword in education_keywords
        ):

            profile["education"].append(line)


    # If no specific education lines were found,
    # keep the first few transcript lines as evidence.

    if not profile["education"]:

        profile["education"] = transcript_lines[:5]


    # ==========================================
    # GENERAL EVIDENCE
    # ==========================================

    profile["evidence"] = resume_lines[:20]


    return profile