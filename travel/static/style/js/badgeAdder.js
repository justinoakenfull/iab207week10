function removeBadge(event) {
  const badge = event.target.closest(".badge");
  if (badge) {
    badge.remove();
  }
}

document.getElementById("artistInput").addEventListener("keypress", function (event) {
  if (event.key == "Enter") {
    event.preventDefault();

    const input = event.target.value.trim();
    if (input !== "") {
      const artistBadges = document.getElementById("artistBadges");
      const badge = document.createElement("span");
      badge.className = "badge rounded-pill text-bg-primary me-2 mb-4 p-2 ps-3 artistPill";
      badge.textContent = input;

      const buttonElement = document.createElement("a");
      buttonElement.classList.add("ms-2");
      buttonElement.onclick = removeBadge;

      // Create the <svg> element
      const iconElement = document.createElement("i");
      iconElement.classList.add("bi", "bi-x-circle-fill");
      iconElement.setAttribute("width", "16");
      iconElement.setAttribute("height", "16");

      buttonElement.appendChild(iconElement);

      // Append the <a> element to the body (or another container)
      badge.appendChild(buttonElement);

      artistBadges.appendChild(badge);

      event.target.value = "";
    }
  }
});
