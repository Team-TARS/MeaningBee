$(document).ready(function() { 
		
		$('#login-form').on('submit', function(event){
		    event.preventDefault(); //to prevent it from getting refreshed
		    console.log("form submitted!");  // check whether its coming in.
		    create_post();
		});
		
		
	function create_post() { //to send post

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

		var csrftoken = getCookie('csrftoken'); // to get the csrf token - django 1.7 doc

		var usernameValue = $('#username').val(); //user name value
		var passwordValue = $('#password').val();

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
		            $('#post-text').val(''); // remove the value from the input
		            console.log(json); // log the returned json to the console
		            console.log("success"); // another sanity check
		            if(json['result']==='success') {
		            	alert("user authenticated");
		            } else {
		            	alert("authentication failure");
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