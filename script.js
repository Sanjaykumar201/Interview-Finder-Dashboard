// page navigation
let currentPage = 1;

function goToPage(page) {
  document
    .querySelectorAll(".page")
    .forEach((p) => p.classList.remove("active"));
  document.getElementById("page" + page).classList.add("active");
  currentPage = page;
}

// skill toggle
function toggleSkill(btn) {
  btn.classList.toggle("active");
}

// validation (name, age, location, college required)
function validateAndGo() {
  let name = document.getElementById("name").value.trim();
  let age = document.getElementById("age").value.trim();
  let location = document.getElementById("location").value.trim();
  let college = document.getElementById("college").value.trim();

  if (name === "" || age === "" || location === "" || college === "") {
    alert("Please fill all required fields");
    return;
  }

  goToPage(3);
}

// internship selection
let selectedInternship = "";

function selectInternship(data) {
  selectedInternship = data;
}

// resume choice
let resumeType = "";

function chooseResume(type) {
  resumeType = type;
}

// apply system
let count = 0;

function applyNow() {
  if (selectedInternship === "") {
    alert("Please select an internship first");
    return;
  }

  if (resumeType === "") {
    alert("Choose resume option (Upload or Profile)");
    return;
  }

  document.getElementById("status").innerText = "Successfully Applied ✔";

  count++;

  let li = document.createElement("li");
  li.innerText = selectedInternship + " - Applied";
  document.getElementById("list").appendChild(li);

  document.getElementById("count").innerText = count;
}
