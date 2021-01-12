/**
 * Greet user
 */
function greetUser() {
  var myDate = new Date();
  var hrs = myDate.getHours();
  var greet;

  if (hrs < 12) greet = "Good Morning,";
  else if (hrs >= 12 && hrs <= 17) greet = "Good Afternoon,";
  else if (hrs >= 17 && hrs <= 24) greet = "Good Evening,";
  document.getElementById("greet").innerHTML = greet;
}

/**
 * Image preview for article form creation
 */
function PreviewImage(event) {
  var cover = document.getElementById("load-cover");
  var wrapper_cover = document.getElementById("show-cover");
  var label_cover = document.getElementById("cover-label");
  var article_body = document.getElementById("article-body");

  // Do somethin with this
  cover.removeAttribute("style");
  wrapper_cover.classList.remove("border");

  label_cover.innerHTML = "Change Cover Image";
  label_cover.classList.remove("p-12");
  label_cover.classList.add("p-3");

  article_body.classList.remove("my-16");
  article_body.classList.add("my-8");
  // Done

  cover.src = URL.createObjectURL(event.target.files[0]);
}
