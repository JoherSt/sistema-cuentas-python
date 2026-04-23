<?php
require_once '../../models/categoria.php';
class CategoriaController 
{
    public static function getAll(){
        $categoriaModel = new Categoria();
        $categorias = $categoriaModel->getAll();
        return $categorias; 
    }
    public static function show(){
        $id = $_GET['id']; 
        $categoriaModel = new Categoria();
        $categorias = $categoriaModel->show($id); 
        return $categorias;
    }

    public static function store(){
       
        $name = $_POST['name'];
        $descripccion = $_POST['description'];
        $categoriaModel = new Categoria();
        $result = $categoriaModel->store($name,$descripccion); 
       
        if($result){
            header('location:index.php');
        }else{
          
           echo 'Hubo un error en la sentencia o algo mal escrito';
        }
    }

    public static function update(){
        $name = $_POST['name'];
        $descripccion =$_POST['description'];
        $id = $_POST['id'];
        $categoriaModel = new Categoria();
        $result = $categoriaModel->update($name,$descripccion,$id); 
        if($result){
            header('location:index.php');
        }else{
         
            echo "error en la sentencia o la categoria no existe la categoria para acrualizar";
        }
    }
    
    public static function destroy(){
        $id = $_GET['id'];
        $categoriaModel = new Categoria();
        $result = $categoriaModel->destroy($id);
        if($result){
            header('location:index.php');
        }else{
            echo "error en la sentencia eliminar o no existe la categoria que quiere eliminar";
        }
    }
}