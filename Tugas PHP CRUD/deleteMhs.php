<?php
include "config.php";
if (isset($_GET['id'])) : 
    $id = $_GET['id']; 
    $sql = "DELETE FROM mhs where id='$id'"; 
    $query = mysqli_query($conn, $sql); 
    if ($query) { 
        header('location: admin.php?hal=dataMhs');
    } else 
    die("akses halaman ini melalui Admin"); 
endif;
?>