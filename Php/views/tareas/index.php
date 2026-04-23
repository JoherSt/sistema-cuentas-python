<?php 
require_once "../../controllers/TareaController.php";
$List_tareas = TareaController::getAll();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Listado de Tareas</h1>
    <table border="1">
        <thead>
        <a href="form-crearTarea.php">Crear tarea</a><br>
            <th>Estado</th>
            <th>fecha_creacion</th>
            <th>Fecha_vencimiento</th>
            <th>Actualizar</th>
            <th>Eliminar</th>
            <th>Ver</th>
        </thead>
        <tbody>
            <?php foreach($List_tareas as $tarea): ?>
            <tr>
                <td><?=$tarea['estado'];?></td><br>
                <td><?=$tarea['fecha_creacion'];?></td>
                <td><?=$tarea['fecha_vencimiento'];?></td>
                <td><a href="editarTareas.php?id=<?=$tarea['id']?>">Editar</a></td>
                <td><a href="delete.php?id=<?=$tarea['id']?>">eliminar</a></td>
                <td><a href="show.php?id=<?=$tarea['id']?>">Ver</a></td>
            </tr>
            <?php endforeach;?>
        </tbody>
    </table>
    
</body>
</html>