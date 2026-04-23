<?php
require_once "../../controllers/ComentarioController.php";
$comentario = ComentarioController::show();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>informacion del comentario:</h1>
    <h1>El id de la tarea es :</h1>
    <h1><?=$comentario['id_tarea'];?></h1>
    <h1>El id del usuario es :</h1>
    <h1><?=$comentario['id_usuario'];?></h1>
    <h1>el comentario es :</h1>
    <h1><?=$comentario['description'];?></h1>
    <h1>La fecha de creacion del comentario es :</h1>
    <h1><?=$comentario['fecha_Creacion'];?></h1>
    <button><a href="index.php">regresar</a></button>
</body>
</html>