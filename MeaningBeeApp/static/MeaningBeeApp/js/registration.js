$(document).ready(function() { 

	$('#user_register_button').on('click' , function(event) {
		event.preventDefault(); //to prevent it from getting refreshed	
		window.location.href = urlString + "/registration/";
	});
	
	$('#registration-form').on('submit', function(event){
	    event.preventDefault(); //to prevent it from getting refreshed
	    console.log("registration form submitted!");  // check whether its coming in.
	    register_user_post();
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
	
	function register_user_post() {
		
		var csrftoken = getCookie('csrftoken');
		var firstnameValue = $('#firstname').val();
		var lastnameValue = $('#lastname').val();
		var dateofbirthValue = $('#dateofbirth').val();
		var usernameValue = $('#username').val();
		var passwordValue = $('#password').val();
		var ajaxData = {csrfmiddlewaretoken: csrftoken, 'firstname' : firstnameValue,
				'lastname' : lastnameValue, 'dateofbirth' : dateofbirthValue,
				'username' : usernameValue, 'password':passwordValue  };
		
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
	        url : "/register_action/", // the endpoint
	        headers: { 'Content-Type': 'application/json'},
	        type : "POST", // http method
	        dataType:"json",
	        data : JSON.stringify(ajaxData), // data sent with the post request
	
	        // handle a successful response
	        success : function(json) {
	            console.log(json); // log the returned json to the console
	            console.log("success"); // another sanity check
	            if(json['result']==='success') {
	            	alert("user registered!");
	            } else {
	            	alert("registration failure!");
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