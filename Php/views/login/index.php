<?php
session_start();
session_destroy();
 ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<style>
    button, input{
        display: block;
        padding: 5px 10px;
    }
</style>
    <h1>Inicio de Seccion</h1>
    <form action="autenticar.php" method="post">
        <label for="">Ingrese el correo</label>
        <input type="email" name="email" >
        <label for="">Ingrese la password</label>
        <input type="password" name="password" >
        <button type="submit">iniciar sescion </button>
    </form>
    <?php 
    if(isset($_SESSION['mesage']))
    {
        echo $_SESSION['mesage'];
    }
    ?>
</body>
</html>