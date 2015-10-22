$(document).ready(function(){
	var curr_page;
	var page = getUrlParameter('page') !== undefined ? getUrlParameter('page') : "";
			  
	if (page == "")	page = 1;
	curr_page = parseInt(page)
	
	$(document).scroll(function(){		
		if (isScrolledIntoView($('#footer'))){
			curr_page += 1;
			var order_by = getUrlParameter('order_by') !== undefined ? getUrlParameter('order_by') : "";
			var reverse = getUrlParameter('reverse') !== undefined ? getUrlParameter('reverse') : "";
			
			var url = $(location).attr('origin');
			var requested_url = url + '/?page=' + curr_page + '&order_by=' + order_by + '&reverse=' + reverse;
			
			$.ajax({
				url : requested_url,
				datatype: 'html',
				method: 'GET',
				success: function(html){	
					var parsed_html = "", tr_item = "";
					var parsed_html = $(html).find("tr");
					var $tbody = $("tbody");
					
					for (tr=1; tr <= parsed_html.length; tr++){						
						if (parsed_html[tr] !== undefined){
							var tr_item = parsed_html[tr].outerHTML;
							$tbody.append($(tr_item).hide().fadeIn(1000));
						}
						
					}
				},
				
				statusCode: {
					500: function(){
							//skip for now				
						}
				},			
			})
		}
		
	});	
	
	function getUrlParameter(sParam) {
	    var sURLVariables = $(location).attr('search').substring(1).split('&'),	         
	        sParameterName,
	        i;

	    for (i = 0; i < sURLVariables.length; i++) {
	        sParameterName = sURLVariables[i].split('=');

	        if (sParameterName[0] === sParam) {
	            return sParameterName[1] === undefined ? true : sParameterName[1];
	        }
	    }
	};
	
	function isScrolledIntoView(elem)
	{
	    var $elem = $(elem);
	    var $window = $(window);

	    var docViewTop = $window.scrollTop();
	    var docViewBottom = docViewTop + $window.height();

	    var elemTop = $elem.offset().top;
	    var elemBottom = elemTop + $elem.height();

	    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
	}
});