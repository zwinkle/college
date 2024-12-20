<?php 
$sql = "SELECT * FROM mhs"; 
$query = mysqli_query($conn, $sql); 
$i = 1; 
?> 
<h2 class="judul">Data Mahasiswa</h2> 
<table class="table"> 
    <thead> 
        <tr> 
            <th>No</th> 
            <th>NIM</th>
            <th>Nama</th>
            <th>Angkatan</th> 
            <th>Kode Prodi</th> 
            <th>Edit</th> 
        </tr> 
    </thead> 
    <tbody> 
<?php 
    while ($row = mysqli_fetch_assoc($query)) { ?> 
    <tr> 
        <td><?php echo $i 
?>
        </td> 
        <td><?php echo $row['nim']; ?></td> 
        <td><?php echo $row['namamhs']; ?></td> 
        <td><?php echo $row['angkatan']; ?></td> 
        <td><?php echo $row['kode_prodi']; ?></td> 
        <td>
            <a href="?hal=editMhs&id=<?php echo $row['id']; ?>" class="tombol edit">Edit</a>
            <a href="?hal=deleteMhs&id=<?php echo $row['id']; ?>" class="tombol hapus">Delete</a></td> 
    </tr> 
<?php 
            $i++; 
}
?> 
    </tbody> 
</table>