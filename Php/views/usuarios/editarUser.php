<?php 
require_once "../../controllers/UsersController.php";
$user = UsuarioController::show();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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
    <h1>Formulario para Actualizar los datos del usuario</h1>
    <form action="update.php" method="post">
        <input type="hidden" name="id" value="<?=$user['id'];?>">
        <label for="">Ingrese el nombre</label>
        <input type="text" name="nombre" value="<?=$user['name'];?>">
        <label for="">Ingrese el correo</label>
        <input type="email" name="email" value="<?=$user['email'];?>">
        <button type="submit">Actualizar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>