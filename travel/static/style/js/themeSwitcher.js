// document.addEventListener("DOMContentLoaded", function () {
//   const themeSwitcher = document.getElementById("themeSwitcher");
//   const themeLinks = document.querySelectorAll(".theme-item");
//   console.log(themeLinks);

//   themeLinks.forEach((link) => {
//     link.addEventListener("click", function (event) {
//       event.preventDefault();
//       const theme = this.getAttribute("data-theme");
//       const themeStylesheet = document.getElementById("themeStylesheet");

//       if (theme === "green") {
//         themeStylesheet.setAttribute("href", "/style/css/greenTheme.css");
//       } else if (theme === "red") {
//         themeStylesheet.setAttribute("href", "/style/css/redTheme.css");
//       } else if (theme === "blue") {
//         themeStylesheet.setAttribute("href", "/style/css/blueTheme.css");
//       }
//     });
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  const themeSwitcher = document.getElementById("themeSwitcher");
  const themeLinks = document.querySelectorAll(".theme-item");
  const themeStylesheet = document.getElementById("themeStylesheet");

  // Function to apply the theme based on the theme name
  function applyTheme(theme) {
    switch (theme) {
      case "green":
        themeStylesheet.setAttribute("href", "../static/style/css/greenTheme.css");
        break;
      case "red":
        themeStylesheet.setAttribute("href", "../static/style/css/redTheme.css");
        break;
      case "blue":
        themeStylesheet.setAttribute("href", "../static/style/css/blueTheme.css");
        break;
    }
  }

  // Load the saved theme from local storage
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    applyTheme(savedTheme);
  }

  // Add event listeners to theme links
  themeLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault(); // Prevent default action

      // Get the selected theme from the data-theme attribute
      const theme = this.getAttribute("data-theme");
      console.log(theme);
      // Apply the selected theme
      applyTheme(theme);

      // Save the selected theme to local storage
      localStorage.setItem("theme", theme);
    });
  });
});
