$(document).ready(function() { 

	$('#playerReady').on('click',function(event) {
		fetchWord();
	});


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
		            	console.log(randomWord)
		            	$('#displayWord').html(randomWord);


		            	//Start the timer once the word is fetched

		            	//TODO - try to get this from the span itself
		            	$('#playerReady').hide();
		            	var sec = parseInt($('#timerSeconds span').html());
						var timer = setInterval(function() { 
						   $('#timerSeconds span').text(sec--);
						   if (sec == -1) {
						      $('#hideMsg').fadeOut('fast');
						      clearInterval(timer);
						      //TODO - change this url
						      window.location.href = urlString + "/loading/";
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
});