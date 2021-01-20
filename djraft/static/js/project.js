window.addEventListener("DOMContentLoaded", function () {
  /**
   * Remove all `domain.com/#id` from url
   */
  //Get all the hyperlink elements
  var links = document.getElementsByTagName("a");

  //Browse the previously created array
  Array.prototype.forEach.call(links, function (elem, index) {
    //Get the hyperlink target and if it refers to an id go inside condition
    var elemAttr = elem.getAttribute("href");
    if (elemAttr && elemAttr.includes("#")) {
      //Replace the regular action with a scrolling to target on click
      elem.addEventListener("click", function (ev) {
        ev.preventDefault();
        //Scroll to the target element using replace() and regex to find the href's target id
        document.getElementById(elemAttr.replace(/#/g, "")).scrollIntoView({
          block: "start",
          inline: "nearest",
        });
      });
    }
  });

  /**
   * User dropdown menus
   */
  var btnMenu = document.getElementById("btn-menu");
  var menus = document.getElementById("menus");
  btnMenu.addEventListener("click", () => {
      menus.classList.toggle("display-none");
  })

});
