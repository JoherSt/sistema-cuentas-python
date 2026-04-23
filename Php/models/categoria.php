<?php
require_once '../../Config/config.php';
class Categoria extends Conexion
{
    function getAll()
    {
        $sql = "SELECT * FROM categorias";    
        $result = $this->conexion->query($sql); 
        return $result->fetch_all(MYSQLI_ASSOC); 
    }

    function store($name,$descripccion)
    {
        $sql = "INSERT INTO categorias values(null,'$name','$descripccion') ";
        return $this->conexion->query($sql); 
    }

    function destroy($id)
    {
        $sql = "DELETE FROM categorias WHERE id = $id";
        return $this->conexion->query($sql); 
    }


    function show($id)
    {
        $sql = "SELECT * FROM categorias WHERE id = $id";
        $result = $this->conexion->query($sql);
        return $result->fetch_assoc();
    }

    function update($name,$descripccion,$id)
    {
        $sql = "UPDATE categorias SET name = '$name',description = '$descripccion' WHERE id = $id ";
        return $this->conexion->query($sql); 
    }
}

