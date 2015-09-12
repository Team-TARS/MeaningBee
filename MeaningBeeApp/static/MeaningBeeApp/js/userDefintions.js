var blockId = 1;
$(document).ready(function() {
	
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


/*Collecting the final set of user definitions when user clicks continue*/
$("#continue").on("click", function(){
    var myValue = $(".block-definition"); //returns array of dom elements
    var word = $.makeArray(myValue); //returns array of javascript objects
    $.each(word, function(index,value) {
    	var finalUserDefinitions = $(value).html();
    	console.log(finalUserDefinitions);
	});
});

