const fileInput = document.getElementById("resumeFile");
const fileName = document.getElementById("fileName");
const loading = document.getElementById("loading");
const dropZone = document.getElementById("dropZone");

// click to open file
dropZone.addEventListener("click", () => fileInput.click());

// show file name
fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        fileName.innerText = fileInput.files[0].name;
    }
});

// drag & drop support
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.style.borderColor = "#60a5fa";
});

dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;

    if (fileInput.files.length > 0) {
        fileName.innerText = fileInput.files[0].name;
    }
});

function uploadResume() {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload a PDF resume");
        return;
    }

    loading.style.display = "block";

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        loading.style.display = "none";

        localStorage.setItem("resumeResult", JSON.stringify(data));
        window.location.href = "dashboard.html";
    })
    .catch(err => {
        loading.style.display = "none";
        alert("Server error");
    });
}