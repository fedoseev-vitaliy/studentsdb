$(document).ready(function(){
	$('#load_more').click(function(){
		$.ajax({
			url : 'http://localhost:8000/?page=1&order_by=last_name&reverse=',
			datatype: 'html',
			method: 'GET',
			success: function(html){				
				var parsed_html = $(html).find("tr");
				var $tbody = $("tbody");
				for (tr=1; tr <= parsed_html.length; tr++){
					var tr_item = parsed_html[tr].outerHTML
					$tbody.append(tr_item);					
				}			
			},
			fail: function(){
				
			}
		})
	});	
});