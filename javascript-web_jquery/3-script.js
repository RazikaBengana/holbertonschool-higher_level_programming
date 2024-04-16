import $ from 'jquery';

const $headerElement = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $headerElement.addClass('red');
});
