<?php 
session_start(); 
ob_start(); 
include "config.php"; 
if (empty($_SESSION["nama"])) { 
?>
<p>kalian harus login untuk mengakses halaman ini</p>
<meta http-equiv="refresh" content="1; url=login.php"/>
<?php 
} else { 
define("INDEX", true) 
?>
<!DOCTYPE html> 
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halaman Admin</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="grid-container">
        <!-- Navbar -->
        <div class="grid-navbar">
            <div class="navbarheader">Sistem Akademik</div>
            <div class="logout"><a href="#">Logout</a></div>
        </div>

        <!-- Sidebar -->
        <div class="grid-sidebar">
            <div class="profilepic">
                <img src="images/profile.png" alt="Profile Picture" class="imground">
                <p><?php echo $_SESSION["nama"]; ?></p>
            </div>
            <div class="navigation">
                <ul>
                    <li><a href="?hal=dashboard" class="active">Dashboard</a></li>
                    <li><a href="?hal=dataMhs">Data Mahasiswa</a></li>
                    <li><a href="?hal=tambahMhs">Tambah Mahasiswa</a></li>
                </ul>
            </div>
        </div>

        <!-- Header -->
        <div class="grid-head">
            <h2>Selamat Datang di Sistem Akademik</h2>
            <p>Sistem Informasi Akademik Campus Terintegrasi</p>
        </div>

        <!-- Content -->
        <div class="grid-content">
            <?php include "konten.php" ?>
        </div>
    </div>
</body>

</html>
<?php 
} 
?>