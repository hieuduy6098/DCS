<?php
    if(!empty($_POST)) {
        session_start();
        $username = $_POST["user"];
        $password = $_POST["pswd"];
        
        //connect database
        require_once("connectSql.php");

        if ($username == "" || $password =="") {
            echo "username hoặc password bạn không được để trống!";
        }else{
            $sql = "SELECT * FROM users WHERE username = '".$username."' and password = '".$password."'";
            $query = mysqli_query($connect, $sql);
            $num_rows = mysqli_num_rows($query);
            if ($num_rows==0) {
                echo "tên đăng nhập hoặc mật khẩu không đúng !";
            }else{
                // Lấy ra thông tin người dùng và lưu vào session
                while ( $data = mysqli_fetch_array($query) ) {
                    $_SESSION["id"] = $data["id"];
                    $_SESSION['username'] = $data["username"];
                    $_SESSION["permission"] = $data["permission"];
                }
                    // Thực thi hành động sau khi lưu thông tin vào session
                    // ở đây mình tiến hành chuyển hướng trang web tới một trang gọi là index.html
                //var_dump($_SESSION);
                switch ($username) {
                    case 'user1':
                        # code...
                        header('Location: line1.php');
                        break;
                    case 'user2':
                        # code...
                        header('Location: line2.php');
                        break;
                    case 'admin':
                        # code...
                        header('Location: admin.php');
                        break;
                }
                $connect->close();
            }
        }   
    }
    
 
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>

</head>
<body>
    <div class="container">
    <h2>Login</h2>
    <form method="post" action="login.php">  
        <div class="form-group">
        <label for="text">User:</label>
        <input type="text" class="form-control" id="user" placeholder="Enter user" name="user">
        </div>
        <div class="form-group">
        <label for="pwd">Password:</label>
        <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pswd">
        </div>
        <input type="submit" name="submit" value="Submit">  
    </form>
    </div>
</body>
</html>