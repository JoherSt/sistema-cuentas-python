<?php
require_once "../../controllers/ComentarioController.php";
$Listcomentario = ComentarioController::getAll();
 ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Listado de comentarios</h1>
    <table border="1">
        <thead>
        <a href="form-crearComentario.php">Crear Comentario</a>
            <th>Id de la tarea</th>
            <th>Id de el usuario </th>
            <th>la fecha de creacion </th>
            <th>Actualizar</th>
            <th>Eliminar</th>
            <th>Ver</th>
        </thead>
        <tbody>
            <?php foreach($Listcomentario as $comentario):?>
            <tr>
            <td><?=$comentario['id_tarea'];?></td>
            <td><?=$comentario['id_usuario'];?></td>
            <td><?=$comentario['fecha_Creacion'];?></td>
            <td><button><a href="editarComentario.php?id=<?=$comentario['id']?>">Editar</a></button></td>
            <td><button><a href="delete.php?id=<?=$comentario['id']?>">Eliminar</a></button></td>
            <td><button><a href="show.php?id=<?=$comentario['id']?>">Ver</a></button></td>
            </tr>
            <?php endforeach;?>
        </tbody>
    </table>
    
</body>
</html>