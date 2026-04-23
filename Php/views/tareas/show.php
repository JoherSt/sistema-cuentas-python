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
    <h1>informacion de la tarea :</h1>
    <h1>Su estado:</h1>
    <h1><?=$tarea['estado'];?></h1>
    <h1>Su descripccion:</h1>
    <h1><?=$tarea['description'];?></h1>
    <h1>Su id de usuario es:</h1>
    <h1><?=$tarea['id_usuario'];?></h1>
    <h1>Su id categoria es:</h1>
    <h1><?=$tarea['id_categoria'];?></h1>
    <h1>Su fecha de creacion:</h1>
    <h1><?=$tarea['fecha_creacion'];?></h1>
    <h1>Su fecha de vencimiento:</h1>
    <h1><?=$tarea['fecha_vencimiento'];?></h1>
    <button><a href="index.php">regresar</a></button>
</body>
</html>