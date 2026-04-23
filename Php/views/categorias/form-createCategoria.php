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
    <h1>Formulario para Crear Categoria</h1>
    <form action="crear.php" method="post">
        <label for="">Ingrese el nombre de la categoria:</label>
        <input type="text" name="name">
        <label for="">Ingrese la descripccion de la categoria</label>
        <input type="text" name="description">
        <button type="submit">Guardar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>