$(document).ready(function() {

  $(function () {
  	var tourDay = new Date();
  	tourDay = new Date(tourDay.getFullYear() + 1, 3 - 1, 20); //NOTE: day(+1), month (starting from zero, so minus 1), year
  	$('#defaultCountdown').countdown({until: tourDay});
  });

  $('.detailsButton').click(function() {
    $(this).toggleClass('rotateimg180');
    $(this).parent().toggleClass('expanded');
    });

  // $('#detailsButton').css('background-color', 'red');

});
