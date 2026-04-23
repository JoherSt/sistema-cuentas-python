<?php 
session_start();
require_once "../../controllers/UsersController.php";
UsersController::auth();
