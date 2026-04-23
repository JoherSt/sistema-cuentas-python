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
    <h1>Formulario para Registrar  usuario</h1>
    <form action="crear.php" method="post">
        <label for="">ingresa el nombre</label>
        <input type="text" name="nombre">
        <label for="">ingresa el correo</label>
        <input type="email" name="email">
        <label for="">ingresa la password</label>
        <input type="password" name="password">
        <button type="submit">Guardar</button>
    </form>
    <button><a href="index.php">regresar</a></button>
</body>
</html>