$(document).ready(function(){
  $('a[rel=tooltip]').tooltip();
  $('#credits').popover({'placement': 'top', });
  $(".collapse").collapse();
  
  
  $('#target_pls').on('change', function(){
    $('#targeted').slideToggle();
  });
    
});