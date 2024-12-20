<?php 
include("config.php"); 
if (isset($_POST['edit'])):
    $id = $_POST['id']; 
    $NIM = $_POST['NIM']; 
    $namaMhs = $_POST['namaMhs']; 
    $angkatan = $_POST['angkatan']; 
    $kode_prodi = $_POST['kode_prodi']; 
      
    $sql = "UPDATE mhs SET NIM = '$NIM', namaMhs='$namaMhs', angkatan='$angkatan', kode_prodi='$kode_prodi' WHERE id=$id"; 
    $query = mysqli_query($conn, $sql); 

    if ($query) { 
      header('location: admin.php?hal=dataMhs');
    } else { 
      die("gagal menyimpan"); 
    } else : 
    die("akses halaman ini melalui admin"); 

    endif;
?>