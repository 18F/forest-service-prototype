$(document).ready(function(){
  $('.add_another_permit_holder').click(function(e){
    e.preventDefault();
    $(".permit_hide").toggle();
    $(this).text($(this).text() == "Add Another Permit Holder" ? "Remove Second Permit Holder" : "Add Another Permit Holder");
  });

  const fieldMapping = {
    'id_organizer_address_1' : 'id_permit_holder_address_1',
    'id_organizer_address_2' : 'id_permit_holder_address_2',
    'id_city' : 'id_permit_holder_city',
    'id_state' : 'id_permit_holder_state',
    'id_zipcode' : 'id_permit_holder_zipcode',
  }

  function addEventListener(listener, outputfield){
    $('#'+listener).on('input', function() {
      if($('#permit-holder-same-address').val() == 'yes'){
          $('#'+outputfield).val($(this).val());
      }
    });

  }
  //Initialize to disabled
  for(key in fieldMapping){
    $('#'+fieldMapping[key]).prop('disabled', true);

    //Add listeners
    addEventListener(key, fieldMapping[key]);
  };

  $('#permit-holder-same-address').change(function(){
    if($(this).val() == "no"){
      $('.permit_holder_1_fieldset input').prop('disabled', false);
      $('.permit_holder_1_fieldset select').prop('disabled', false);
    } else {
      for(key in fieldMapping){
        $('#'+fieldMapping[key]).val($('#'+key).val()).prop('disabled', true);
      };
    }
  });

  $('button:submit').mousedown(function(){
    console.log("i fired");
    for(key in fieldMapping){
      $('#'+fieldMapping[key]).prop('disabled', false);
    }
  });


});
