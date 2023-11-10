<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$username = $_POST["username"];
	$password = $_POST["password"];

	if ($username === "your_username" && $password === "your_password") {
		// Successful login
		// Log the login attempt (you can customize the log format)
		$logMessage = "Successful login attempt: Username: $username, IP: " . $_SERVER["REMOTE_ADDR"] . ", Date: " . date("Y-m-d H:i:s") . "\n";
		file_put_contents("login_attempts.log", $logMessage, FILE_APPEND);
	
		// Redirect back to the dashboard only on successful login
		header("Location: dashboard.html");
		exit(); // Ensure that the script stops execution after the redirect
	}
	else {
        // Failed login
        // Log the login attempt (you can customize the log format)
        $logMessage = "Failed login attempt: Username: $username, IP: " . $_SERVER["REMOTE_ADDR"] . ", Date: " . date("Y-m-d H:i:s") . "\n";
        file_put_contents("login_attempts.log", $logMessage, FILE_APPEND);
        
        // You might want to include an error message or handle failed login differently
        echo "Login failed. Please try again."; // Adjust as needed
    }
}
?>
