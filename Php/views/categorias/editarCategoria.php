<?php
require_once "../../controllers/Categoriacontroller.php";
$categoria = Categoriacontroller::show();
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
    <h1>Formulario para Actualizar categoria</h1>
    <form action="update.php" method="post">
        <input type="hidden" name="id" value="<?=$categoria['id']?>">
        <label for="">Ingrese el name</label>
       <input type="text" name="name" value="<?=$categoria['name']?>">
       <label for="">Ingrese la descriccion</label>
       <input type="text" name="description" value="<?=$categoria['description']?>">
       <button type="submit">Actualizar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>