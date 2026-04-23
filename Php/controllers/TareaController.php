<?php
require_once '../../models/tarea.php';
class TareaController 
{
    public static function getAll()
    {
        $tareaModel = new Tarea();
        $tareas = $tareaModel->getAll();
        return $tareas; 
    }

    public static function show()
    {
        $id = $_GET['id']; 
        $tareaModel = new Tarea();
        $tareas = $tareaModel->show($id); 
        return $tareas;
    }

    public static function store()
    {
      
        $descripccion = $_POST['description'];
        $id_user = $_POST['id_usuario'];
        $fecha_vencimiento = $_POST['fecha_vencimiento'];
        $estado = $_POST['estado'];
        $id_categoria = $_POST['id_categoria'];
        $tareaModel = new Tarea();
        $result = $tareaModel->store($descripccion,$id_user,$fecha_vencimiento,$estado,$id_categoria); 
       
        if($result){
            header('location:index.php');
        }else{
          
           echo 'Hubo un error en la sentencia o algo mal escrito';
        }
    }

    public static function update()
    {
        $id = $_POST['id'];
        $descripccion = $_POST['description'];
        $id_user = $_POST['id_usuario'];
        $id_categoria = $_POST['id_categoria'];
        $fecha_vencimiento = $_POST['fecha_vencimiento'];
        $estado = $_POST['estado'];
        $tareaModel = new Tarea();
        $result = $tareaModel->update($id,$descripccion,$id_user,$id_categoria,$fecha_vencimiento,$estado); 
        if($result){
            header('location:index.php');
        }else{
         
            echo "error en la sentencia o la categoria no existe la categoria para acrualizar";
        }
    }
    
    public static function destroy()
    {
        $id = $_GET['id'];
        $tareaModel = new Tarea();
        $result = $tareaModel->destroy($id);
        if($result){
            header('location:index.php');
        }else{
            echo "error en la sentencia eliminar o no existe la categoria que quiere eliminar";
        }
    }
}