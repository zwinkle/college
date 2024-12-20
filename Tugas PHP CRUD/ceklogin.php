<?php 
session_start();
include "config.php";

$username = $_POST['username'];
$password = $_POST['password'];

$query = mysqli_query($conn, "SELECT * FROM user WHERE username = '$username'");
$data = mysqli_fetch_assoc($query); 
$hasil = mysqli_num_rows($query);

if ($hasil > 0) {
    if (password_verify($password, $data['password'])) { 
        $_SESSION['nama'] = $data['nama']; 
        $_SESSION['username'] = $data['username']; 
        header("location:admin.php"); 
    } else {
?> 
        <h1 align="center">Login Gagal,Password salah</h1>
        <meta http-equiv="refresh" content="1; url=login.php"/>
<?php
    } 
    } else { 
?>
        <h1 align="center">Login Gagal, Username dan Password tidak diketemukan</h1>
        <meta http-equiv="refresh" content="1; url=login.php"/>
<?php
    }
?>