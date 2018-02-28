<html>
<head>
<meta charset="utf-8">
<title>Formulario</title>
</head>
<body>
 <form action="ejercicio2.php" method="post">
    <div class="row">
        <label for="nombre">Tu nombre:</label><br />
        <input id="nombre" class="input" name="nombre" type="text" value="" size="30" /><br />
    </div>
    <div class="row">
        <label for="apellido">Tu apellido:</label><br />
        <input id="apellido" class="input" name="apellido" type="text" value="" size="30" /><br />
    </div>
    <div class="row">
        <label for="salario">Tu salario:</label><br />
        <input id="salario" class="input" name="salario" type="text" value="" size="30" /><br />
    </div>
    <div class="row">
        <label for="edad">Tu edad:</label><br />
        <input id="edad" class="input" name="edad" type="text" value="" size="30" /><br />
    </div>
    <input id="submit_button" type="submit" value="Enviar!"/>
</form>     
<?php
$salario = (float)$_POST["salario"];
$Edad = (int)$_POST["edad"];
$nombre = $_POST["nombre"];
$apellido = $_POST["apellido"];

if ( $salario <= 2000  and $salario >= 1000 ) {
    if ($Edad > 45){
       $salario =$salario +( $salario * 0.03);
                  }
    }
    else{
        $salario = $salario + ($salario * 0.1);
        }

elseif ($salario < 1000){
        if ($Edad < 30){ 
            $salario = 1100;  
        }
        elseif ( $Edad <= 45 and $Edad => 30){
                $salario =$salario + ($salario * 0.03);
            }
        
        else{
            $salario = $salario + ($salario * 0.15);
    }   
}
echo("<p>El nuevo salario de $nombre $apellido con $Edad años será $salario</p>");

?>
</body>
</html>
