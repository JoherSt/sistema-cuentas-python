<?php
require_once '../../Config/config.php';
class Tarea extends Conexion
{
    function getAll()
    {
        $sql = "SELECT * FROM tareas";  
        $result = $this->conexion->query($sql); 
        return $result->fetch_all(MYSQLI_ASSOC); 
    }

    function store($descripccion,$id_user,$fecha_vencimiento,$estado,$id_categoria)
    {
        $sql = "INSERT INTO tareas values(null,$id_user,'$descripccion',null,'$fecha_vencimiento','$estado',$id_categoria) ";
        return $this->conexion->query($sql); 
    }

    function destroy($id)
    {
        $sql = "DELETE FROM tareas WHERE id = $id";
        return $this->conexion->query($sql); 
    }


    function show($id)
    {
        $sql = "SELECT * FROM tareas WHERE id = $id";
        $result = $this->conexion->query($sql);
        return $result->fetch_assoc();
    }

    function update($id,$descripccion,$id_user,$id_categoria,$fecha_vencimiento,$estado)
    {
        $sql = "UPDATE tareas SET description = '$descripccion',id_usuario = $id_user,id_categoria = $id_categoria,fecha_vencimiento = $fecha_vencimiento,estado = '$estado' WHERE id = $id ";
        return $this->conexion->query($sql); 
    }
}

