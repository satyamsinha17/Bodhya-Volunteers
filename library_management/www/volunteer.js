const volunteers = const volunteers = {{ volunteers | tojson }};

function renderVolunteers() {
	const grid = document.getElementById("volunteersGrid");
	const filteredVolunteers = volunteers.filter((vol) => {
		const searchText = document.getElementById("searchBox").value.toLowerCase();
		return (
			vol.full_name.toLowerCase().includes(searchText) ||
			vol.college_name.toLowerCase().includes(searchText)
		);
	});

	document.getElementById("totalCount").textContent = filteredVolunteers.length;

	grid.innerHTML = filteredVolunteers
		.map(
			(vol, idx) => `
                <div class="volunteer-card" onclick="openModal(${volunteers.indexOf(vol)})">
                    <img src="${vol.picture}" alt="${
				vol.full_name
			}" class="volunteer-image" onerror="this.src='https://via.placeholder.com/180?text=${encodeURIComponent(
				vol.full_name.split(" ")[0]
			)}'">
                    <h3 class="volunteer-name">${vol.full_name}</h3>
                    <p class="volunteer-college">${vol.college_name}</p>
                </div>
            `
		)
		.join("");
}

document.getElementById("searchBox").addEventListener("input", renderVolunteers);

function openModal(index) {
	const vol = volunteers[index];
	document.getElementById("modalAvatar").src = vol.picture;
	document.getElementById("modalName").textContent = vol.full_name;
	document.getElementById("modalRole").textContent = vol.role;
	document.getElementById("modalCollege").textContent = `${vol.college} • ${vol.year}`;
	document.getElementById("modalBio").textContent = vol.bio;
	document.getElementById("modalSkills").innerHTML = vol.skills
		.map((s) => `<span class="skill-tag">${s}</span>`)
		.join("");
	document.getElementById("modalGithub").href = vol.github;
	document.getElementById("modalLinkedin").href = vol.linkedin;
	document.getElementById("volunteerModal").classList.add("active");
}

function closeModal() {
	document.getElementById("volunteerModal").classList.remove("active");
}

document.getElementById("volunteerModal").addEventListener("click", (e) => {
	if (e.target.id === "volunteerModal") closeModal();
});

renderVolunteers();
