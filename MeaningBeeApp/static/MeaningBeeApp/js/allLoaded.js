$(document).ready(function() { 

	$('#playerReady').on('click',function(event) {
		window.location.href = urlString + "/user_definitions/";
		fetchWord();
	});	
});