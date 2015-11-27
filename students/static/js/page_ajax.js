$(document).ready(function(){
	var curr_page;
	var page = getUrlParameter('page') !== undefined ? getUrlParameter('page') : "";
	var order_by = getUrlParameter('order_by') !== undefined ? getUrlParameter('order_by') : "";
	var reverse = getUrlParameter('reverse') !== undefined ? getUrlParameter('reverse') : "";
	
	if (page == "")	page = 1;
	curr_page = parseInt(page);			
	
	$(document).on('change', '.checkbox_delete_or_not', function(){		
		var value = $(this)[0].checked;
		var url = $(location).attr('href');		
		var id = $(this)[0].attributes['checkbox_id'].value;
		
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
		var csrftoken = getCookie('csrftoken');

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
		});
		
		$.post(url, {"checkbox_value": value, 
				     "checkbox_id": id,}
				);							
	});
	
	$(document).scroll(function(){		
		if (isScrolledIntoView($('#footer'))){
			curr_page += 1;			
			
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
							$tbody.append($(tr_item).hide().fadeIn(2000));
							$(document).trigger('ready');
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
	};
});