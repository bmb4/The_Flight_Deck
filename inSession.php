<?php

session_start();

if (isset($_POST['current_user'])) {
    $_SESSION['current_user'] = $_POST['current_user'];
}
if (!isset($_SESSION['current_user'])) {
    $_SESSION['current_user'] = 'Megan';
}
// echo $_SESSION['current_user'];
print 'hello';

?>