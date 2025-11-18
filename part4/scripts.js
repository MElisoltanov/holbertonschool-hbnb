/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    /* DO SOMETHING */
    fetch('header.html')
      .then(response => response.text())
      .then(html => {
      document.getElementById('header').innerHTML = html;
    });

    fetch('footer.html')
      .then(response => response.text())
      .then(html => {
        document.getElementById('footer').innerHTML = html;
      });
  });