<?php 
if (isset($_GET['id'])) {
    $id = $_GET['id']; 
    $sql = "SELECT * FROM mhs WHERE id='$id'"; 
    $query = mysqli_query($conn, $sql); 
    $data = mysqli_fetch_assoc($query); 
    if (mysqli_num_rows($query) < 1) { 
        die("data tidak ditemukan"); 
    } else { 
?> 
    <h2 class="judul">Edit Data Mahasiswa</h2> 
    <form action="prosesEdit.php" method="POST"> 
        <fieldset> 
        <input type="hidden" name="id" value="<?php 
            echo $data['id'] ?>" /> 
        <p> 
            <label for="nim">NIM : </label> 
            <input type="text" name="NIM" placeholder="NIM" value="<?php echo $data['nim']; ?> "> 
       </p> 
       <p> 
            <label for="nama">Nama : </label> 
            <input type="text" name="namaMhs" placeholder="nama" value="<?php echo $data['namamhs']; ?> "> 
        </p> 
        <p> 
            <label for="angkatan">Angkatan : </label> 
            <input type="text" name="angkatan" placeholder="Angkatan" value="<?php echo $data['angkatan']; ?> "> 
        </p> 
        <p> 
            <label for="kode_prodi">Kode Prodi : </label>
            <input type="text" name="kode_prodi" placeholder="Kode Prodi" value="<?php echo $data['kode_prodi']; ?> "> 
        </p>   
        <p> 
          <input type="submit" value="Edit Data" name="edit"> 
        </p> 
        </fieldset> 
    </form> 
<?php 
    } 
} 
?>