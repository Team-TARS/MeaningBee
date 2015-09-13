var blockId = 1;
var finalUserDefinitions;

$(document).ready(function() {

	fetchWord();
	
	/*Creates a new block when user provides definitions and presses enter*/
	$('#comment').keypress(function (e) {
	  if (e.which == 13) {
	    var text = $('#comment').val();
            $("#answer-container").append('<div id='+blockId+' class="block-dimension margin-padding-10">'
		    		+'<div class="row">'+'<div class="col-sm-10 block-definition">'
		    		+ text +'</div>'+'<div class="col-sm-2">'
					+'<button type="button" class="btn btn-default" onClick="remove_definition($(this))">'
					+'<span class="icon-style glyphicon glyphicon-remove">'+'</span>'
					+'</button>'+'</div>'+'</div>'+'</div>')
            $('#comment').val(" ");
            blockId++;
	    return false;  
  	  }
	});
});

/*Removes the user-definition when close button is clicked*/
function remove_definition(clickedButtonReference) {
	clickedButtonReference.parent().parent().parent().remove();
}

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

function fetchWord() {
	console.log("Inside fetch word");
	var csrftoken = getCookie('csrftoken');
	//TODO - chcek if it is need to send csrftoken
	var ajaxData = {csrfmiddlewaretoken: csrftoken, 'sampleData' : 'sample'};
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	}); // to check if the csrf token is set - django 1.7 doc

	$.ajax({
	        url : "/fetch_word/", // the endpoint
	        headers: { 'Content-Type': 'application/json'},
	        type : "POST", // http method
	        dataType:"json",
	        data : JSON.stringify(ajaxData), // data sent with the post request
	
	        // handle a successful response
	        success : function(json) {
	            console.log(json); // log the returned json to the console
	            console.log("success"); // another sanity check
	            if(json['result']==='success') {
	            	var randomWord = json['word'];
	            	console.log(randomWord);

	            	$('#displayWord').html(randomWord);


	            	//Start the timer once the word is fetched
	            	var sec = parseInt($('#timerSeconds span').html());
					var timer = setInterval(function() { 
					   $('#timerSeconds span').text(sec--);
					   if (sec == -1) {
					   	  finalUserDefinitions = getUserDefinitions();
					   	  console.log(finalUserDefinitions);
					      //$('#hideMsg').fadeOut('fast');
					      $('#continue').fadeOut('fast');
					      clearInterval(timer);
					      //TODO - change this url
					      //window.location.href = urlString + "/loading/";
					   } 
					}, 1000);
	            }
	            else {
	            	//TODO - handle this error or keep polling
	            	alert("Oops, something went wrong");
	            }
	        },
	        // handle a non-successful response
	        error : function(xhr,errmsg,err) {
	            console.log("Error.");
	            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
	        }
	});			
}

function getUserDefinitions() {
	var myValue = $(".block-definition"); //returns array of dom elements
    var word = $.makeArray(myValue); //returns array of javascript objects
    var result = []; 
    var i = 0;
    $.each(word, function(index,value) {
    	result[i++] = $(value).html();
	});
	return result;
}


/*Collecting the final set of user definitions when user clicks continue*/
$("#continue").on("click", function(){
    finalUserDefinitions = getUserDefinitions();
    console.log(finalUserDefinitions);
});

