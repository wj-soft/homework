$(document).ready(function () {
  // 메인 메뉴 제어를 위한 스크립트
  var main_menu = $('.menu > li');
  var sub_menu_last = $('.menu-detail li:last-child a');

  main_menu.hover(function () {
    $(this).find('.menu-detail').toggleClass('menu-detail-active');
  });
  main_menu.focusin(function () {
    $(this).find('.menu-detail').addClass('menu-detail-active');
  });
  sub_menu_last.focusout(function () {
    $(this).parents('.menu-detail').removeClass('menu-detail-active');
  });

  var tab = $('.tab');
  tab.on('click focusin', function () {
    $(this).parent().addClass('menu-detail-active')
      .siblings().removeClass('menu-detail-active');
  });
});