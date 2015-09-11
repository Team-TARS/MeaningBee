$(document).ready(function() {
	
	$('#login-form').on('submit', function(event){
	    event.preventDefault(); //to prevent it from getting refreshed
	    console.log("login form submitted!");  // check whether its coming in.
	    create_post();
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
	
	function validateUserCredentials(usernameValue,passwordValue) {
		console.log("Inside validation");
		if(usernameValue == null && passwordValue == null || usernameValue == "" && passwordValue == "") {
			document.getElementById('username_label').innerHTML = 'Enter valid username';
			document.getElementById('password_label').innerHTML = 'Enter valid password';
			return false;
		}
		else if(usernameValue == null || usernameValue == "") {
			document.getElementById('username_label').innerHTML = 'Enter valid username';
			return false;
		}
		else if(passwordValue == null || passwordValue == "") {
			document.getElementById('password_label').innerHTML = 'Enter valid password';
			return false;
		}
		else {
			return true;
		}
	}
	
	function create_post() { //to send post

		$('#login_label').html('');
		var csrftoken = getCookie('csrftoken'); // to get the csrf token - django 1.7 doc

		var usernameValue = $('#username').val(); //user name value
		var passwordValue = $('#password').val();
		
		var validationResult = validateUserCredentials(usernameValue,passwordValue);
		
		if(validationResult == true) {
			var formdata = $('#login-form').serialize();
			var ajaxData = {csrfmiddlewaretoken: csrftoken, 'username' : usernameValue, 'password':passwordValue  };

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
		        url : "/login_action/", // the endpoint
		        headers: { 'Content-Type': 'application/json'},
		        type : "POST", // http method
		        dataType:"json",
		        data : JSON.stringify(ajaxData), // data sent with the post request
		        //data:formdata,
		
		        // handle a successful response
		        success : function(json) {
		            console.log(json); // log the returned json to the console
		            console.log("success"); // another sanity check
		            if(json['result']==='success') {
		            	//alert("user authenticated");
		            	window.location.href = urlString + "/choice_screen/";
		            } else {
		            	//alert("authentication failure");
		            	$('#login_label').html('Username/password do not match!');
		            } 
		        }, 
		
		        // handle a non-successful response
		        error : function(xhr,errmsg,err) {
		            console.log("Error.");
		            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		        }
		    });	
		}
		else {
			console.log("Username or password missing.");
		}

		
	}
});