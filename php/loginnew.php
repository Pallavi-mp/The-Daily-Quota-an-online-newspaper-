<?php

extract($_POST);
$host="localhost"; // Host name 
$username = "root";
$password = " ";
$db = "user-details";
$con=mysqli_connect("$host", "$username", "$password","$db")or die("cannot connect"); 
$tbl="userdetails";
echo"SUCCESSSS";
mysqli_close($con);
?>
