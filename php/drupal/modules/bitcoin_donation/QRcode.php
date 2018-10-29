<?php
include_once("phpqrcode/qrlib.php");

ob_start("callback");
  $param = "bitcoin:" . $_GET['qr_text'];
  if (!empty($_GET['label'])) {
    $param .= '?label=' . $_GET['label'];
  }
ob_end_clean(); 

QRcode::png($param);


