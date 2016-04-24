<?php

if ($_SERVER['REQUEST_METHOD'] == "POST") {
	$temperature = "";
	$humidity = "";
	if (isset($_REQUEST['temperature'])) {
	    $temperature = $_REQUEST['temperature'];
	}
	if (isset($_REQUEST['humidity'])) {
	    $humidity = $_REQUEST['humidity'];
	}
	if ($temperature != "" || $humidity != "") {
	    $output = time().",".$temperature.",".$humidity."\n";
	    print $output;
	    file_put_contents("log.csv", $output, FILE_APPEND);
	}
} else {
	print file_get_contents("log.csv");
}
