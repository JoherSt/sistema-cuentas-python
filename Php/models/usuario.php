<?php
require_once '../../CONFIG/config.php';
class Usuario extends Conexion
{

    public function getAll()
    {
        $sql = "SELECT * FROM usuarios";    
        $result = $this->conexion->query($sql); 
        return $result->fetch_all(MYSQLI_ASSOC); 
    }

    public function getUserById($id)
    { 
        $sql = "SELECT * FROM usuarios WHERE id = ?";
        $stmt = $this->conexion->prepare($sql);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result->fetch_assoc();          
    }

    public function store($nombre, $email, $password)
    { 
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO usuarios (name, email, password) VALUES (?, ?, ?)";
        $stmt = $this->conexion->prepare($sql);
        $stmt->bind_param("sss", $nombre, $email, $hashed_password);
        return $stmt->execute();
    }

    public function update($id, $nombre, $email)
    {
        $sql = "UPDATE usuarios SET name = ?, email = ? WHERE id = ?";
        $stmt = $this->conexion->prepare($sql);
        $stmt->bind_param("ssi", $nombre, $email, $id);
        return $stmt->execute();
    }
    
    public function autenticar($email, $password)
    {
        $sql = "SELECT * FROM usuarios WHERE email = ?";
        $stmt = $this->conexion->prepare($sql);
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result;
    }

    public function destroy($id)
    {
        $sql = "DELETE FROM usuarios WHERE id = ?";
        $stmt = $this->conexion->prepare($sql);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

