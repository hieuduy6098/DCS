<?php
    require_once("define.php");
    
    //connect database
    $connect = new mysqli(HOST, USERNAME, PASSWORD, DATABASE);
    //set utf8
    mysqli_set_charset($connect, "utf8");
    //check connect
    if($connect->connect_errno){
        var_dump($connect->connect_errno);
        die();
    }
