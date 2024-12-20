<?php 
include "config.php";
if (isset($_POST['fullname']) && isset($_POST['username']) && isset($_POST['password'])) {
    $nama = $_POST['fullname']; 
    $username = $_POST['username']; 
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $sql = "INSERT INTO user (nama, username, password) VALUES ('$nama', '$username', '$password')";
    $query = mysqli_query($conn, $sql);
    if ($query) {
    ?>
        <p>User berhasil dibuat, silahkan <a href="login.php">login</a> </p>
    <?php
    } else {
        header("location: register.php");
    }
}
?>