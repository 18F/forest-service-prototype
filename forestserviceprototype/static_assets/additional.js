$(document).ready(function(){

  // Field handling for Application form
  $('.permit_hide').hide();
  $('.add_another_permit_holder').click(function(e){
    e.preventDefault();
    $(this).text($(this).text() == "Add another permit holder" ? "Remove second permit holder" : "Add another permit holder");
    $(".permit_hide").toggle();
  });

  const fieldMapping = {
    'id_applicant_address_1' : 'id_permit_holder_address_1',
    'id_applicant_address_2' : 'id_permit_holder_address_2',
    'id_applicant_city' : 'id_permit_holder_city',
    'id_applicant_state' : 'id_permit_holder_state',
    'id_applicant_zipcode' : 'id_permit_holder_zipcode',
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
    for(key in fieldMapping){
      $('#'+fieldMapping[key]).prop('disabled', false);
    }
  });

//Form handling for application approval and rejection
$('#approve-form').on('submit', function(event){
    event.preventDefault();
    form_decision(this, '', 'Approved');
});

$('#deny-error-message').hide();
$('#deny-form').on('submit', function(event){
    event.preventDefault();
    reason = $('#input-type-textarea').val();
    if (reason.length > 0){
      $('#deny-error-message').hide().text("");
      form_decision(this, reason, 'Rejected');
    } else {
      $('#deny-error-message').show().text("Please enter an explanation for your denial");
    }
});
function form_decision(div, decision_explanation, new_status) {
    console.log($(div).prop("action")); // sanity check
    $.ajax({
        url : $(div).prop("action"), // the endpoint
        type : "POST", // http method
        data : { deny_reason :  decision_explanation}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            $('#permit-status').text(new_status);
            $('#application-review').hide();
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

//ADD CSRF Protection
// This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


});
