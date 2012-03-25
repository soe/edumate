$(document).ready(function(){
  $('a[rel=tooltip]').tooltip();
  $('#credits').popover({'placement': 'top', });
  
  
  $('#target_pls').on('change', function(){
    $('#targeted').slideToggle();
  });
    
});