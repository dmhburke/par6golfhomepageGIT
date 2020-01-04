$(document).ready(function() {

  $(function () {
  	var tourDay = new Date();
  	tourDay = new Date(tourDay.getFullYear() + 0, 3 - 1, 20); //NOTE: year(target + x to current year), month (starting from zero, so minus 1), day
  	$('#defaultCountdown').countdown({until: tourDay});
  });

  $('.detailsButton').click(function() {
    $(this).toggleClass('rotateimg180');
    $(this).parent().toggleClass('expanded');
    });

  // $('#detailsButton').css('background-color', 'red');

});
