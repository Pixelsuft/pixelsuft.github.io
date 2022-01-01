window.addEventListener('contextmenu', function(e) {
  return e.preventDefault();
});


function main() {
  const copyright = document.getElementById('copyright');
  const links = document.getElementsByClassName('link');

  for (var i = 0; i < links.length; i++) {
    const current_link = links[i];
    current_link.addEventListener('click', function() {
      location.href = current_link.getAttribute('href');
    });
  }

  copyright.textContent += ' ' + new Date().getFullYear();
}

window.onload = main;
