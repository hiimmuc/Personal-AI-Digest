// Reading progress bar
(function () {
  var bar = document.getElementById("progress");
  if (!bar) return;
  window.addEventListener("scroll", function () {
    var doc = document.documentElement;
    var scrolled = doc.scrollTop || document.body.scrollTop;
    var total = doc.scrollHeight - doc.clientHeight;
    bar.style.width = total > 0 ? (scrolled / total * 100) + "%" : "0%";
  });
})();
