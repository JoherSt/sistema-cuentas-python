<?php
require_once "../../controllers/TareaController.php";
$tarea = TareaController::show();
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
    <h1>Formulario para Actualizar tarea</h1>
    <form action="update.php" method="post">
        <input type="hidden" name="id" value="<?=$tarea['id'];?>">

        <label for="">su usuario en id es :</label>
        <input type="num" name="id_usuario" value="<?=$tarea['id_usuario'];?>">

        <label for="">Su descripccion es :</label>
        <input type="text" name="description" value="<?=$tarea['description'];?>">

        <label for="">su fecha de vencimiento es :</label>
        <input type="date" name="fecha_vencimiento" value="<?=$tarea['fecha_vencimiento'];?>">

        <label for="">su categoria en id es :</label>
        <input type="num" name="id_categoria" value="<?=$tarea['id_categoria'];?>">

        <label for="">El estado en id de la tarea es :</label>
        <input type="text" name="estado" value="<?=$tarea['estado'];?>">

        <button type="submit">Guardar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>