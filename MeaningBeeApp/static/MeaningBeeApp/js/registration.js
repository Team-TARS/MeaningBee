$(document).ready(function() { 
	
	$('#registration-form').on('submit', function(event){
	    event.preventDefault(); //to prevent it from getting refreshed
	    clearValidationErrors();
	    register_user_post();
	});

	$('#login_redirect').on('click',function(event) {
		window.location.href = urlString + "/login/";
	});
	
	
	//$('#dateofbirth').datepick();
	var newMaxDate = new Date();
	newMaxDate.setFullYear(newMaxDate.getFullYear() - 8 );
	newMaxDate.setDate(1);
	newMaxDate.setMonth(0);
	

	var newMinDate = new Date();
	newMinDate.setFullYear(newMinDate.getFullYear() - 20 );
	newMinDate.setDate(1);
	newMinDate.setMonth(0);
	$("#dateofbirth").datepick({ maxDate: newMaxDate, minDate: newMinDate});
	
	function clearValidationErrors() {
		document.getElementById('firstname_label').innerHTML = '';
	    document.getElementById('lastname_label').innerHTML = '';
	    document.getElementById('dob_label').innerHTML = '';
	    document.getElementById('username_label').innerHTML = '';
	    document.getElementById('password_label').innerHTML = '';
	    document.getElementById('registration_label').innerHTML = '';
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
	
	function validateRegistrationCredentials(firstnameValue,lastnameValue,dateofbirthValue,usernameValue,passwordValue) {
		if(firstnameValue=="" || lastnameValue=="" || dateofbirthValue=="" || usernameValue=="" || passwordValue=="") {
			if(firstnameValue=="") {
				document.getElementById('firstname_label').innerHTML = 'Enter valid firstname';
			}
			if(lastnameValue=="") {
				document.getElementById('lastname_label').innerHTML = 'Enter valid lastname';
			}
			if(dateofbirthValue=="") {
				document.getElementById('dob_label').innerHTML = 'Enter valid date of birth';
			}
			if(usernameValue=="") {
				document.getElementById('username_label').innerHTML = 'Enter valid username';
			}
			if(passwordValue=="") {
				document.getElementById('password_label').innerHTML = 'Enter valid password';
			}
			return false;
		}
		else {
			return true;
		}
	}	
	
	function register_user_post() {
		
		var csrftoken = getCookie('csrftoken');
		var firstnameValue = $('#firstname').val();
		var lastnameValue = $('#lastname').val();
		var dateofbirthValue = $('#dateofbirth').val();
		var usernameValue = $('#username').val();
		var passwordValue = $('#password').val();
		
		var validationResult = validateRegistrationCredentials(firstnameValue,lastnameValue,dateofbirthValue,usernameValue,passwordValue);
		
		if(validationResult == true) {
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
		            	//alert("user registered!");
		            	$('#registration_success_label').html("User registered");
		            	$('#register').removeClass('showinline');
		            	$('#register').addClass('hidden');

		            	//$('#login_redirect').show();
		            	$('#login_redirect').removeClass('hidden');
		            	$('#login_redirect').addClass('showinline');
		            	//window.location.href = urlString + "/login/";
		            }
		            else if(json['result']==='user exists') {
		            	$('#username_label').html('Username already exists!');
		            }
		            else {
		            	alert("registration failure!");
		            	$('#registration_label').html("Registration failed. Provide different credentials or please try again later");
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
			console.log("Missing fields.");
		}
		
	}
		
		

});