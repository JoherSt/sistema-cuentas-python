<?php
require_once '../../Config/config.php';
class Comentario extends Conexion
{
    function getAll()
    {
        $sql = "SELECT * FROM comentarios";    
        $result = $this->conexion->query($sql); 
        return $result->fetch_all(MYSQLI_ASSOC); 
    }

    function store($id_tarea,$id_user,$descripccion)
    {
        $sql = "INSERT INTO comentarios values(null,$id_tarea,$id_user,'$descripccion',null) ";
        return $this->conexion->query($sql); 
    }

    function destroy($id)
    {
        $sql = "DELETE FROM comentarios WHERE id = $id";
        return $this->conexion->query($sql); 
    }


    function show($id)
    {
        $sql = "SELECT * FROM comentarios WHERE id = $id";
        $result = $this->conexion->query($sql);
        return $result->fetch_assoc();
    }

    function update($id,$id_tarea,$id_user,$descripccion)
    {
        $sql = "UPDATE comentarios SET id_tarea = $id_tarea,id_usuario =$id_user,description = '$descripccion' WHERE id = $id ";
        return $this->conexion->query($sql); 
    }
}

