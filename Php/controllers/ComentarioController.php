<?php
require_once '../../models/comentario.php';
class ComentarioController 
{
    public static function getAll()
    {
        $comentarioModel = new Comentario();// metodos post
        $comentarios = $comentarioModel->getAll();
        return $comentarios; 
    }
    public static function show()
    {
        $id = $_GET['id']; 
        $comentarioModel = new Comentario();
        $comentarios = $comentarioModel->show($id); 
        return $comentarios;
    }

    public static function store()
    {
        $id_tarea = $_POST['id_tarea'];
        $id_user = $_POST['id_usuario'];
        $descripccion = $_POST['description'];//id_tarea,id_usuario,description,fecha_creacion-null
        $comentarioModel = new Comentario();
        $result = $comentarioModel->store($id_tarea,$id_user,$descripccion); 
       
        if($result){
            header('location:index.php');
        }else{
          
           echo 'Hubo un error en la sentencia o algo mal escrito';
        }
    }

    public static function update()
    {
        $id = $_POST['id'];
        $id_tarea = $_POST['id_tarea'];
        $id_user = $_POST['id_usuario'];
        $descripccion =$_POST['description'];
        $comentarioModel = new Comentario();
        $result = $comentarioModel->update($id,$id_tarea,$id_user,$descripccion); 
        if($result){
            header('location:index.php');
        }else{
         
            echo "error en la sentencia o la categoria no existe la categoria para acrualizar";
        }
    }
    
    public static function destroy()
    {
        $id = $_GET['id'];
        $comentarioModel = new Comentario();
        $result = $comentarioModel->destroy($id);
        if($result){
            header('location:index.php');
        }else{
            echo "error en la sentencia eliminar o no existe la categoria que quiere eliminar";
        }
    }
}