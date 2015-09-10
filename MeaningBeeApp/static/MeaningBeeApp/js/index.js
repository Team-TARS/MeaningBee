$(document).ready(function() { 

$('#user_login_button').on('click' , function(event) {
		window.location.href = urlString + "/login/";
	});

$('#user_register_button').on('click' , function(event) {
		event.preventDefault(); //to prevent it from getting refreshed	
		window.location.href = urlString + "/registration/";
	});

});