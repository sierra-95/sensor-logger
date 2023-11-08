<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$username = $_POST["username"];
	$password = $_POST["password"];

	// Replace with your authentication logic
	if ($username === "your_username" && $password === "your_password") {
	    // Successful login
	    // Log the login attempt (you can customize the log format)
		$logMessage = "Successful login attempt: Username: $username, IP: " . $_SERVER[" REMOTE_ADDR"] . ", Date: " . date("Y-m-d H:i:s") . "\n";

		file_put_contents("login_attempts.log", $logMessage, FILE_APPEND);
	}
	else {
		// Failed login
		// Log the login attempt (you can customize the log format)
		$logMessage = "Failed login attempt: Username: $username, IP: " . $_SERVER["REMOTE_ADDR"] . ", Date: " . date("Y-m-d H:i:s") . "\n";
	    file_put_contents("login_attempts.log", $logMessage, FILE_APPEND);
	}
 }

// Redirect back to the dashboard
header("Location: dashboard.html");
?>
