var blockId=1;
$(document).ready(function() {
	$('#comment').keypress(function (e) {
	  if (e.which == 13) {
	    var text = $('#comment').val();
            $("#answer-container").append('<div id=blockDiv'+blockId+' class="block-dimension margin-padding-10">'
		    		+'<div class="row">'+'<div class="col-sm-10">'
		    		+ text +'</div>'+'<div class="col-sm-2">'
					+'<button type="button" class="btn btn-default">'
					+'<span class="icon-style glyphicon glyphicon-remove">'+'</span>'
					+'</button>'+'</div>'+'</div>'+'</div>')
            $('#comment').val(" ");
            blockId++;
	    return false;  
  	  }
	});
});
