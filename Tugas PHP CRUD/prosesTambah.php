<?php 
include("config.php"); 
if (isset($_POST['simpan'])) : 
    $NIM = $_POST['NIM']; 
    $namaMhs = $_POST['namaMhs']; 
    $angkatan = $_POST['angkatan']; 
    $kode_prodi = $_POST['kode_prodi']; 
    $sql = "INSERT INTO mhs (NIM, namaMhs, angkatan, kode_prodi) VALUES ('$NIM', '$namaMhs', '$angkatan', '$kode_prodi')"; 
    
    $query = mysqli_query($conn, $sql); 
    
    if ($query) { 
        header('location: admin.php?hal=dataMhs'); 
    } else { 
?> 
        <h1 align="center">Data gagal diinput</h1> 
        <meta http-equiv="refresh" content="1; url=admin.php?hal=tambahMhs" /> 
<?php 
    } else : 
    die("akses halaman ini melalui Admin"); 
endif;
?>