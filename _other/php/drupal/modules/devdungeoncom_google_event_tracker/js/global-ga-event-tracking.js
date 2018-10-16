(function ($){
	$(document).ready(function($) {
		// trackEvent parameters: Category, Action, Label
		
		// Video - user clicks image to open lightbox
		$('.view-video img').click(function() {
			_gaq.push(['_trackEvent', 'Video', 'Play']);
		});
		
		// Newsletter signup form - Start - onclick into name field
		$('#webform-name #edit-submitted-name').click(function() {
			_gaq.push(['_trackEvent', 'Lead Gen', 'Start', 'Newsletter']);
		});
		
		// Blog comment - Click into textarea - Need to ensure users don't have wysiwyg
		$('.field-name-comment-body textarea').click(function() {
			_gaq.push(['_trackEvent', 'Blog', 'Start', 'Comment']);
		});

		// Generic event for webform submissions
		$('.node-webform #edit-submit').click(function() {
			var $pagetitle = $('#page-title').html();
			_gaq.push(['_trackEvent', 'Webform', 'Submitted', $pagetitle]);
		});
		
	});
} (jQuery));
