<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halaman Register</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="container">
        <div class="loginbox">
            <h2>Halaman Register</h2>
            <form action="cekregister.php" method="POST">
                <input id="fullname" name="fullname" type="text" placeholder="Nama Lengkap" required>
                <input id="username" name="username" type="text" placeholder="Username" required>
                <input id="password" name="password" type="password" placeholder="Password" required>
                <input id="konfirm_password" name="konfirm_password" type="password" placeholder="Konfirmasi Password" required>
                <input type="submit" value="Register" name="register" onclick="return Validate()">
            </form>
        </div>
    </div>

    <script type="text/javascript">
        function Validate() {
            var password = document.getElementById("password").value;
            var konfirmPassword = document.getElementById("konfirm_password").value;

            if (password != konfirmPassword) {
                alert("Password tidak sesuai");
                return false;
            }
            return true;
        }
    </script>
</body>

</html>
