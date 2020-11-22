/* Project specific Javascript goes here. */
var d = new Date();
var greet;
var ch = d.getHours();


if (ch >= 5) { greet = "Good Morning,";}
else if (ch >= 12) { greet = "Good Afternoon,";}
else if (ch >= 17) { greet = "Good Evening,";}
document.getElementById("greet").innerHTML = greet;


function AutoGrowTextArea(textField) {
  if (textField.clientHeight < textField.scrollHeight) {
    textField.style.height = textField.scrollHeight + "px";
    if (textField.clientHeight < textField.scrollHeight) {
      textField.style.height =
        textField.scrollHeight * 2 - textField.clientHeight + "px";
    }
  } else {
    textField.style.height = textField.scrollHeight + "px";
  }
}
