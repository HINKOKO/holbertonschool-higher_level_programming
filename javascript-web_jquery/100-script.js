// DOMContentLoaded event fires when the initial HTML document has been completely loaded
// and parsed without waiting for stylesheet, images, scripts to finish loading
// basically, it's the goal of this advanced task here, to make us deal with this event
// DOMContentLoaded may fire before the script has a chance to run, so wise to check before
// by adding here our addEventListener on DOMContentLoaded

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
