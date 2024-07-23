function toggleNav() {
  var navbar = document.getElementById("drop-down");
  if (navbar.classList.contains("open")) {
      navbar.classList.remove("open");
  } else {
      navbar.classList.add("open");
  }
}
