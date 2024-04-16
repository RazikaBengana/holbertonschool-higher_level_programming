import $ from 'jquery';

const $listElement = $('UL.my_list');
const $addItemElement = $('div#add_item');

$addItemElement.on('click', () => {
  $listElement.append('<li>Item</li>');
});
