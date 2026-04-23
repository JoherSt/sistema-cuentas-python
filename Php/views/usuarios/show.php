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
    <h1>El usuario es :</h1>
    <h1>Su nombre es </h1>
    <h1><?=$user['name'];?></h1>
    <h1>Su email</h1>
    <h1><?=$user['email'];?></h1>
    <h1>Su password</h1>
    <h1><?=$user['password'];?></h1>
    <button><a href="index.php">regresar</a></button>
</body>
</html>