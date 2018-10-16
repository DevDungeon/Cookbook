Philips Hue Programming
============


# Tutorial/Documentation

https://developers.meethue.com/documentation/getting-started


# Get the bridge IP

www.meethue.com/api/nupnp


# Debug

http://192.168.0.105/debug/clip.html


# Create a username

http://192.168.0.105/api/
POST
{"devicetype":"my_hue_app#test"}

[
	{
		"success": {
			"username": "XXXXXXXXXXX_API_KEY_XXXXXXXXXXXXXXXXXXXX"
		}
	}
]


# Get list of lights

http://192.168.0.105/api/XXXXXXXXXXX_API_KEY_XXXXXXXXXXXXXXXXXXXX/lights
GET


# Get specific light info

http://192.168.0.105/api/XXXXXXXXXXX_API_KEY_XXXXXXXXXXXXXXXXXXXX/lights/1


# Turn a light on/off

http://192.168.0.105/api/XXXXXXXXXXX_API_KEY_XXXXXXXXXXXXXXXXXXXX/lights/1/state
{"on":false}
{"on":true, "sat":254, "bri":254,"hue":10000}
{"on":true, "hue":46920, "effect":"colorloop", "alert":"select"}
PUT


# Control whole group

http://192.168.0.105/api/XXXXXXXXXXX_API_KEY_XXXXXXXXXXXXXXXXXXXX/groups/1/action
{"on":true, "hue":46920, "effect":"colorloop", "alert":"select"}
PUT


# Example light info. State values are changeable

{
	"state": {
		"on": false,
		"bri": 1,
		"hue": 10778,
		"sat": 251,
		"effect": "none",
		"xy": [
			0.5609,
			0.4042
		],
		"ct": 500,
		"alert": "none",
		"colormode": "xy",
		"reachable": true
	},
	"type": "Extended color light",
	"name": "Hue Lamp 1",
	"modelid": "LCT001",
	"manufacturername": "Philips",
	"uniqueid": "00:11:22:33:44:55:66:77-00",
	"swversion": "5.50.1.19000"
}


# Other URLs

/lights resource which contains all the light resources
/groups resource which contains all the groups
/config resource which contains all the configuration items
/schedules which contains all the schedules
/scenes which contains all the scenes
/sensors which contains all the sensors
/rules which contains all the rules