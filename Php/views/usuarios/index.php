<?php
session_start();
require_once "../../controllers/UsersController.php";
$ListUsers =UsuarioController::index();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Bienvenid@ <?=$_SESSION['name'];?></h1>
    <h3>Listado de Usuarios</h3>
    <table border="1">
        <thead>
        <button><a href="form-crearUser.php">Crear Usuario</a></button>
            <th>Nombre</th>
            <th>Email</th>
            <th>Actualizar</th>
            <th>Eliminar</th>
            <th>Ver</th>
        </thead>
        <tbody>
            <?php foreach($ListUsers as $user):?>
                <tr>
                    <td><?=$user['name'];?></td>
                    <td><?=$user['email'];?></td>
                    <td><a href="editarUser.php?id=<?=$user['id']?>">Editar</a></td>
                    <td><a href="deleteUser.php?id=<?=$user['id']?>">eliminar</a></td>
                    <td><a href="show.php?id=<?=$user['id']?>">Ver</a></td>
                </tr>
                <?php endforeach;?>
        </tbody>
    </table>
 
</body>
</html>