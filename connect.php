<?php
$server_name="localhost";
$username="root";
$password="";
$database_name="jobtalks";

$conn=mysqli_connect($server_name,$username,$password,$database_name);
//now check the connection
if(!$conn)
{
	die("Connection Failed:" . mysqli_connect_error());

}

if(isset($_POST['save']))
{	
	 $name_jina = $_POST['name_jina'];
	 $job_experience = $_POST['job_experience'];


	 $sql_query = "INSERT INTO stories (name_jina,job_experience)
	 VALUES ('$name_jina','$job_experience')";

	 if (mysqli_query($conn, $sql_query)) 
	 {
		echo "New Details Entry inserted successfully !";
	 } 
	 else
     {
		echo "Error: " . $sql . "" . mysqli_error($conn);
	 }
	 mysqli_close($conn);
}
?>