window.addEventListener('contextmenu', function(e) {
  return e.preventDefault();
});


function main() {
  const topnav = document.getElementById('pixelTop');
  const tops = topnav.getElementsByClassName('link');
  for (var i = 0; i < tops.length; i++) {
    const current_top = tops[i];
    current_top.addEventListener('click', function() {
      location.href = current_top.getAttribute('href');
    });
  }
}

window.onload = main;
