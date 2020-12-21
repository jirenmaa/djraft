window.addEventListener(
  'DOMContentLoaded',
  function () {
    const articleForm = document.getElementById('article-form');

    function sentDataArticle() {
      const xhr = new XMLHttpRequest();
      var formData = new FormData();

      xhr.open("POST", "new-story", true);

      //: get csrf token
      formData.append(
        'csrfmiddlewaretoken',
        document.getElementsByName('csrfmiddlewaretoken')[0].value
      );

      //: get text content from element
      formData.append('title', document.getElementById('id_title').innerText);
      formData.append(
        'description',
        document.getElementById('id_description').innerText
      );
      formData.append('cover', document.getElementById('id_cover').files[0]);
      formData.append('body', document.getElementById('id_body').innerText);
      //: end of get text content from element

      xhr.send(formData);

      xhr.onreadystatechange = function(){
        if (xhr.status == 200){
          window.location.replace(`/@${username}`);
        }
      }
    }

    articleForm.addEventListener('submit', (e) => {
      e.preventDefault();
      console.log(document.getElementById('id_body').innerText)
      sentDataArticle();
    });
  },
  true
);
