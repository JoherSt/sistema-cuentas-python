<?php 
session_start();
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
    <h1>Formulario para crear Tarea</h1>
    <form action="crear.php" method="post">

        <label for="">Ingresa el id del usuario</label>
        <input type="hidden" name="id_usuario" value="<?=$_SESSION['id'];?>">

        <label for="">Ingresa la descripccion</label>
        <input type="text" name="description">

        <label for="">Ingresa la fecha de vencimiento</label>
        <input type="date" name="fecha_vencimiento">

        
        <label for="">Elige el Estado</label><br>
        <select name="estado" >
            <option value="Pendiente">Pendiente</option>
            <option value="En proceso">En proceso</option>
            <option value="Cpmpletado">completado</option>
        </select><br>

        <label for="">Elige la categoria</label><br>

        <select name="id_categoria" >
            <option value="1">Trabajo</option>
            <option value="2">Urgente</option>
            <option value="3">completado</option>
        </select><br>

        <label for="">Ingresa el id de la categoria para clasificar la tarea</label>
        <input type="number" name="id_categoria">

        <button type="submit">Guardar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>