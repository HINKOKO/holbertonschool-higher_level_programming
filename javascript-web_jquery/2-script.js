#!/usr/bin/node
$('#red_header').bind('click', function () {
  $(this).css('color', '#FF0000');
});

// this one works too but longer
// $(function () {
// 	$('#red_header').click(function () {
// 	  $(this).css('color', '#FF0000');
// 	});
//   });
