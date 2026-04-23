<?php require_once "../../controllers/CategoriaController.php";
$Listcategorias = CategoriaController::getAll();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Listado de Categorias</h1>
    <table border="1">
        <thead>
        <a href="form-createCategoria.php">Crear Categoria</a><br>
            <th>nombre</th>
            <th>Ver</th>
            <th>Actualizar</th>
            <th>Eliminar</th>
        </thead>
        <tbody>
            <?php foreach ($Listcategorias as $categoria): ?>
            <tr> 
                <td><?=$categoria['name'];?></td><br>
                <td><a href="show.php?id=<?=$categoria['id']?>">Ver</a></td>
                <td><a href="editarCategoria.php?id=<?=$categoria['id']?>">Editar</a></td>
                <td><a href="delete.php?id=<?=$categoria['id']?>">Eliminar</a></td>
            </tr>
            <?php endforeach;?>
        </tbody>
    </table>
    
</body>
</html>