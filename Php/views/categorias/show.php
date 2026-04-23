<?php 
require_once "../../controllers/CategoriaController.php";
$categoria = CategoriaController::show();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>La Categoria</h1>
    <h1>El nombre es :</h1>
    <h1><?=$categoria['name'];?></h1>
    <h1>Su descripcion es :</h1>
    <h1><?=$categoria['description'];?></h1>
    <button><a href="index.php">regresar</a></button>
</body>
</html>