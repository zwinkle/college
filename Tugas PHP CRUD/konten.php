<?php 
if (!defined("INDEX")) die(""); 
 
$halaman = array("dashboard","dataMhs","tambahMhs",
"editMhs","deleteMhs"); 
 
if (isset($_GET['hal'])) $hal = $_GET['hal']; 
else $hal = "dashboard";
foreach($halaman as $h){ 
    if ($hal == $h){ 
        include "$h.php"; 
    break; 
    } 
}