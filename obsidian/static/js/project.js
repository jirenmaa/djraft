/* Project specific Javascript goes here. */
function profileDropdown() {
  let el = document.getElementById("profile-setting-dropdown");
  if (el.classList.contains("hidden")) {
    el.classList.remove("hidden");
    el.classList.add("active");
  } else {
    el.classList.remove("active");
    el.classList.add("hidden");
  }
}
