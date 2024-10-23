function validateRegister() {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
        alert("Password tidak sama");
    } else {
        alert("Password sesuai");
    }
}
