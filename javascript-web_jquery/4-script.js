import $ from 'jquery';

const $headerElement = $('header');
const $divRedHeader = $('DIV#toggle_header');

$divRedHeader.on('click', () => {
  const currentClass = $headerElement.attr('class');

  if (currentClass === 'green') {
    $headerElement.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerElement.toggleClass(`${currentClass} green`);
  }
});
