const data = JSON.parse(localStorage.getItem("resumeResult"));

if (data) {
    document.getElementById("score").innerText = data.score;

    document.getElementById("skills").innerText =
        data.skills_found.join(", ");
}
const fb = data.feedback;

document.getElementById("strengths").innerHTML =
  fb.strengths.map(s => `<li>${s}</li>`).join("");

document.getElementById("weakness").innerHTML =
  fb.weakness.map(s => `<li>${s}</li>`).join("");

document.getElementById("improvements").innerHTML =
  fb.improvements.map(s => `<li>${s}</li>`).join("");

document.getElementById("suggestions").innerHTML =
  fb.suggestions.map(s => `<li>${s}</li>`).join("");

  document.getElementById("questions").innerHTML =
        data.interview_questions.map(q => `<li>${q}</li>`).join("");

    // ✅ NEW: JOB ROLE
    document.getElementById("jobRole").innerText =
        data.job_role;