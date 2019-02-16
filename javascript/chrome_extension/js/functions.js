
/*
* Send notification
*/
function notify() {
	var notification = webkitNotifications.createNotification(
	  'img/icon.png',  // icon url - can be relative
	  'Hello!',  // notification title
	  'Lorem ipsum...'  // notification body text
	);

	// Then show the notification.
	notification.show();
}
