Cordova Notes
=============


Installing
----------

npm install -g cordova

Start a new project
-------------------

Example::

  cordova create cordova-gps-tool com.devdungeon.cordovagpstool GpsTool

Add platforms
-------------

Add multiple platforms::

  cordova platform add browser
  cordova platform add android

Running/Build
--------------

Examples::

  cordova run browser
  cordova run android
  cordova build android
  cordova build android --release

Finding & Adding plugins
------------------------

Examples::

  cordova plugin search geolocation
  cordova plugin add cordova-plugin-geolocation

Once you add a plugin with that command,
it adds it to your ``config.xml`` and you are
good to go. No further imports or work needed,
before starting to access the API in the JS file.

Adding event listeners
----------------------

Add event listeners inside the ``onDeviceReady`` function.
