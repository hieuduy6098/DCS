<?php
  require_once("connectSql.php");
  $sql = "SELECT * FROM datamay";
  $result = mysqli_query($connect, $sql);
  //var_dump($result);
  $flag = false;
  $filename = "sampledata.xls"; // File Name

  // Download file
  header("Content-Disposition: attachment; filename=\"$filename\"");
  header("Content-Type: application/vnd.ms-excel");
  while($row = mysqli_fetch_assoc($result)) {
    if(!$flag) {
    // viet ten cot giong ten truong trong bang
      echo implode("\t", array_keys($row)) . "\r\n";
      $flag = true;
    }
    echo implode("\t", array_values($row)) . "\r\n";
  }