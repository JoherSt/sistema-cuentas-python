<?php
require_once '../../models/usuario.php';

class UsersController
{

    public static function index()
    {
        $usuarioModel = new Usuario();
        $usuarios = $usuarioModel->getAll();
        return $usuarios; 
    }

    public static function show()
    {
        $id = $_GET['id']; 
        $usuarioModel = new Usuario();
        $usuario = $usuarioModel->getUserById($id); 
        return $usuario;
    }

    public static function store()
    {
        $nombre = $_POST['nombre'];
        $email = $_POST['email'];

        $usuarioModel = new Usuario();
        $result = $usuarioModel->store($nombre, $email, $_POST['password']); 
       
        if($result){
            header('location:index.php');
        }else{
           echo 'Hubo un error en la sentencia o algo mal escrito';
        }
    }

    public static function update()
    {
        $nombre = $_POST['nombre'];
        $email = $_POST['email'];
        $id = $_POST['id'];
        $usuarioModel = new Usuario();
        $result = $usuarioModel->update($id, $nombre, $email); 
        if($result){
            header('location:index.php');
        }else{
            echo "error en la sentencia o el usuario no existe para actualizar";
        }
    }

    public static function auth()
    {
        $email = $_POST['email'];
        $password = $_POST['password'];
        $usuarioModel = new Usuario();
        $result = $usuarioModel->autenticar($email, $password);
        $user = $result->fetch_assoc();
        if ($result->num_rows == 1 && password_verify($password, $user['password']))
        {
            $_SESSION['id'] = $user['id'];
            $_SESSION['name'] = $user['name'];
            $_SESSION['email'] = $user['email'];
            header('location:../usuarios/');
        }
        else
        {
            $_SESSION['message'] = "Correo o Clave incorrecta";
            header('location:index.php');
        }
    }
    
    public static function destroy()
    {
        $id = $_GET['id'];
        $usuarioModel = new Usuario(); 
        $result = $usuarioModel->destroy($id);
        if($result){
            header('location:index.php');
        }else{
            echo "error en la sentencia eliminar o no existe el usuario que quiere eliminar";
        }
    }

}

