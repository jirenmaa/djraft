window.addEventListener("DOMContentLoaded", function () {
  const storyForm = document.getElementById("story-form");
  const settingForm = document.getElementById("settings-form");

  /**
   * Function Story Creation and Edit
   */
  function storyProcessForm() {
    const url = window.location.pathname;
    const uname = document.getElementById("user-username").innerText;
    let _formContents = new FormData();
    let redirect = document.location.protocol + "//" + document.location.host;

    let lastSegment = url.split("/").pop() || url.split("/").pop();
    if (lastSegment.toString() == "edit") {
      redirect += "/me/stories";
    } else {
      redirect += "/@" + uname;
    }

    _formContents.append(
      "csrfmiddlewaretoken",
      document.getElementsByName("csrfmiddlewaretoken")[0].value
    );
    _formContents.append(
      "title",
      document.getElementById("id_title").innerText
    );
    _formContents.append(
      "description",
      document.getElementById("id_description").innerText
    );
    _formContents.append("cover", document.getElementById("id_cover").files[0]);
    _formContents.append("body", document.getElementById("id_body").innerText);

    fetch(url, {
      method: "POST",
      body: _formContents,
    }).then((response) => (window.location = redirect));
  }

  /**
   * Function User Edit Settings
   */
  function editUserSettings() {
    const url = window.location.pathname;
    var _formContents = new FormData();
    var newUserHrefDt = document.getElementById("user_href_detail");
    let redirect =
      document.location.protocol + "//" + document.location.host + "/@";

    _formContents.append(
      "csrfmiddlewaretoken",
      document.getElementsByName("csrfmiddlewaretoken")[0].value
    );
    _formContents.append(
      "username",
      document.getElementById("id_username").innerText
    );
    _formContents.append("bio", document.getElementById("id_bio").innerText);
    _formContents.append(
      "avatar",
      document.getElementById("id_avatar").files[0]
    );

    fetch(url, {
      method: "POST",
      body: _formContents,
    });
  }

  if (storyForm) {
    storyForm.addEventListener("submit", (e) => {
      e.preventDefault();
      storyProcessForm();
    });
  }

  if (settingForm) {
    settingForm.addEventListener("submit", (e) => {
      e.preventDefault();
      editUserSettings();
    });
  }
});
