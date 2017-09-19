$('.tab').on('click focusin', function() {
  $(this).parent().addClass('active').siblings().removeClass('active');
});