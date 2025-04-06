<?php
    $cmd_line = system("id", $retVar);
    echo '[+] Cmd executed: ' . $retVar;
?>