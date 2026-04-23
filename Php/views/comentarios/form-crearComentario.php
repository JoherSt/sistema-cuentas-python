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
    <h1>Formulario para Registrar comentario</h1>
    <form action="crear.php" method="post">
        <label for="">Ingresa el Id de la tarea</label>
        <input type="text" name="id_tarea">
        <label for="">Ingresa el Id del usuario</label>
        <input type="text" name="id_usuario">
        <label for="">Ingresa el comentario</label>
        <input type="text" name="description">
        <button type="submit">registrar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>