<?php

class PHPTail {
        
        
        /**
         * Location of the log file we're tailing
         * @var string
         */
        private $log = "";
        /**
         * The time between AJAX requests to the server. 
         * 
         * Setting this value too high with an extremly fast-filling log will cause your PHP application to hang.
         * @var integer
         */
        private $updateTime;
        /**
         * This variable holds the maximum amount of bytes this application can load into memory (in bytes).
         * @var string
         */
        private $maxSizeToLoad;
        /**
         * 
         * PHPTail constructor
         * @param string $log the location of the log file
         * @param integer $defaultUpdateTime The time between AJAX requests to the server. 
         * @param integer $maxSizeToLoad This variable holds the maximum amount of bytes this application can load into memory (in bytes). Default is 2 Megabyte = 2097152 byte
         */
        public function __construct($log, $defaultUpdateTime = 2000, $maxSizeToLoad = 2097152) {
                $this->log = $log;
                $this->updateTime = $defaultUpdateTime;
                $this->maxSizeToLoad = $maxSizeToLoad;
        }
        /**
         * This function is in charge of retrieving the latest lines from the log file
         * @param string $lastFetchedSize The size of the file when we lasted tailed it.  
         * @param string $grepKeyword The grep keyword. This will only return rows that contain this word
         * @return Returns the JSON representation of the latest file size and appended lines.
         */
        public function getNewLines($lastFetchedSize, $grepKeyword, $invert) {

                /**
                 * Clear the stat cache to get the latest results
                 */
                clearstatcache();
                /**
                 * Define how much we should load from the log file 
                 * @var 
                 */
                $fsize = filesize($this->log);
                $maxLength = ($fsize - $lastFetchedSize);
                /**
                 * Verify that we don't load more data then allowed.
                 */
                if($maxLength > $this->maxSizeToLoad) {
                        return json_encode(array("size" => $fsize, "data" => array("ERROR: PHPTail attempted to load more (".round(($maxLength / 1048576), 2)."MB) then the maximum size (".round(($this->maxSizeToLoad / 1048576), 2)."MB) of bytes into memory. You should lower the defaultUpdateTime to prevent this from happening. ")));  
                }
                /**
                 * Actually load the data
                 */
                $data = array();
                if($maxLength > 0) {
                        
                        $fp = fopen($this->log, 'r');
                        fseek($fp, -$maxLength , SEEK_END); 
                        $data = explode("\n", fread($fp, $maxLength));
                        
                }
                /**
                 * Run the grep function to return only the lines we're interested in.
                 */
                if($invert == 0) {
                        $data = preg_grep("/$grepKeyword/",$data);
                }
                else {
                        $data = preg_grep("/$grepKeyword/",$data, PREG_GREP_INVERT);
                }
                /**
                 * If the last entry in the array is an empty string lets remove it.
                 */
                if(end($data) == "") {
                        array_pop($data);
                }
                return json_encode(array("size" => $fsize, "data" => $data));   
        }
        /**
         * This function will print out the required HTML/CSS/JS
         */
        public function generateGUI() {
                ?>
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                        <head>
                                <title>PHPTail</title> 
                                <meta http-equiv="content-type" content="text/html;charset=utf-8" />

                                <link type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/themes/flick/jquery-ui.css" rel="stylesheet"></link>
                                <style type="text/css">
                                        #grepKeyword, #settings { 
                                                font-size: 80%; 
                                        }
                                        .float {
                                                background: white; 
                                                border-bottom: 1px solid black; 
                                                padding: 10px 0 10px 0; 
                                                margin: 0px;  
                                                height: 30px;
                                                width: 100%; 
                                                text-align: left;
                                        }
                                        .results {
                                                padding-bottom: 20px;
                                        }
                                </style>

                                <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
                                <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js"></script>
                                
                                <script type="text/javascript">
                                        /* <![CDATA[ */
                                        //Last know size of the file
                                        lastSize = <?php echo filesize($this->log); ?>;
                                        //Grep keyword
                                        grep = "";
                                        //Should the Grep be inverted?
                                        invert = 0;
                                        //Last known document height
                                        documentHeight = 0; 
                                        //Last known scroll position
                                        scrollPosition = 0; 
                                        //Should we scroll to the bottom?
                                        scroll = true;
                                        $(document).ready(function(){

                                                // Setup the settings dialog
                                                $( "#settings" ).dialog({
                                                        modal: true,
                                                        resizable: false,
                                                        draggable: false,
                                                        autoOpen: false,
                                                        width: 590,
                                                        height: 270,
                                                        buttons: {
                                                                Close: function() {
                                                                        $( this ).dialog( "close" );
                                                                }
                                                        },
                                                        close: function(event, ui) { 
                                                                grep = $("#grep").val();
                                                                invert = $('#invert input:radio:checked').val();
                                                                $("#grepspan").html("Grep keyword: \"" + grep + "\"");
                                                                $("#invertspan").html("Inverted: " + (invert == 1 ? 'true' : 'false'));
                                                        }
                                                });
                                                //Close the settings dialog after a user hits enter in the textarea
                                                $('#grep').keyup(function(e) {
                                                        if(e.keyCode == 13) {
                                                                $( "#settings" ).dialog('close');
                                                        }
                                                });             
                                                //Focus on the textarea                                 
                                                $("#grep").focus();
                                                //Settings button into a nice looking button with a theme
                                                $("#grepKeyword").button();
                                                //Settings button opens the settings dialog
                                                $("#grepKeyword").click(function(){
                                                        $( "#settings" ).dialog('open');
                                                        $("#grepKeyword").removeClass('ui-state-focus');
                                                });
                                                //Set up an interval for updating the log. Change updateTime in the PHPTail contstructor to change this
                                                setInterval ( "updateLog()", <?php echo $this->updateTime; ?> );
                                                //Some window scroll event to keep the menu at the top
                                                $(window).scroll(function(e) {
                                                    if ($(window).scrollTop() > 0) { 
                                                        $('.float').css({
                                                            position: 'fixed',
                                                            top: '0',
                                                            left: 'auto'
                                                        });
                                                    } else {
                                                        $('.float').css({
                                                            position: 'static'
                                                        });
                                                    }
                                                });
                                                //If window is resized should we scroll to the bottom?
                                                $(window).resize(function(){
                                                        if(scroll) {
                                                                scrollToBottom();
                                                        }
                                                });
                                                //Handle if the window should be scrolled down or not
                                                $(window).scroll(function(){
                                                        documentHeight = $(document).height(); 
                                                        scrollPosition = $(window).height() + $(window).scrollTop(); 
                                                        if(documentHeight <= scrollPosition) {
                                                                scroll = true;
                                                        }
                                                        else {
                                                                scroll = false; 
                                                        }
                                                });
                                                scrollToBottom();
                                                                                        
                                        });
                                        //This function scrolls to the bottom
                                        function scrollToBottom() {
                                                $('.ui-widget-overlay').width($(document).width());
                                            $('.ui-widget-overlay').height($(document).height());

                                                $("html, body").scrollTop($(document).height());
                                                if($( "#settings" ).dialog("isOpen")) {
                                                        $('.ui-widget-overlay').width($(document).width());
                                                    $('.ui-widget-overlay').height($(document).height());
                                                    $( "#settings" ).dialog("option", "position", "center");
                                                }
                                        }
                                        //This function queries the server for updates.
                                        function updateLog() {
                                                $.getJSON('Log.php?ajax=1&lastsize='+lastSize + '&grep='+grep + '&invert='+invert, function(data) {
                                                        lastSize = data.size;
                                                        $.each(data.data, function(key, value) { 
                                                                $("#results").append('' + value + '<br/>');
                                                        });
                                                        if(scroll) {
                                                                scrollToBottom();
                                                        }
                                                });
                                        }
                                        /* ]]> */
                                </script>
                        </head> 
                        <body>
                                <div id="settings" title="PHPTail settings">
                                        <p>Grep keyword (return results that contain this keyword)</p>
                                        <input id="grep" type="text" value=""/>
                                        <p>Should the grep keyword be inverted? (Return results that do NOT contain the keyword)</p>
                                        <div id="invert">
                                                <input type="radio" value="1" id="invert1" name="invert" /><label for="invert1">Yes</label>
                                                <input type="radio" value="0" id="invert2" name="invert" checked="checked" /><label for="invert2">No</label>
                                        </div>
                                </div>
                                <div class="float">
                                        <button id="grepKeyword">Settings</button>
                                        <span>Tailing file: <?php echo $this->log; ?></span> | <span id="grepspan">Grep keyword: ""</span> | <span id="invertspan">Inverted: false</span>
                                </div>
                                <div id="results">
                                </div>
                        </body> 
                </html> 
                <?php
        }
}