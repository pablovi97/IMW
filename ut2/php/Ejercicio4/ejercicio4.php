<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Formulario</title>
</head>
<body>
    <form action="ejercicio4.php" method="post">
        <label for="filas">Filas:</label>
        <input type="text" name="filas"/><br>

        <label for="columnas">Columnas:</label>
        <input type="text" name="columnas"/><br>

        <input type="submit" value="Enviar"/>
    </form>
<table border="1">
<?php
$col = 1;
$fil = 1;
$filas = (float)$_POST["filas"];
$columnas = (float)$_POST["columnas"];

if ($filas >= 1 and $columnas >= 1) {
        echo("<h3>Tabla:</h3>");
    while ($fil<=$filas) {
        $fil++;
        echo("<tr>");
        while ($col<=$columnas) {
            $col++;
            echo("<td>table</td>");
            }
        $col = 1;
        echo("</tr>");
        }
        }
    else{
    echo("Error en el valor");
}

?>
</table>
</body>
</html>
