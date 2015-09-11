$(document).ready(function() { 

	$('#instructions').on('click',function(event) {
		window.location.href = urlString + "/instructions/";
	});

	$('#beginGame').on('click',function(event) {
		window.location.href = urlString + "/begin_game/";
	});

	$('#playerDashboard').on('click',function(event) {
		window.location.href = urlString + "/player_dashboard/";
	});
});