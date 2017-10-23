# *Sirviendo aplicaciones Php y Python*  

## Sitio web 1:    

     Tenemos que hacer una pagina con la URL ("http://php.alu5912.me") y que contenga una pagina en php

> Para ello tenemos que descargar la pagina  que se encuentra en el moodle como "demo_php.zip"

* Primero pasamos la pagina del moodle a la maquina de produccion y la descomprimimos :  

![imagen](./IMG/1.PNG)

* Luego creamos el virtual host al que llamaremos php   

![imagen](./IMG/2.PNG)
* Y Tambien su respectivo enlace simbolico  

![imagen](./IMG/3.PNG)  

![imagen](./IMG/4.PNG)
* Por ultimo reiniciamos NGINX  y cuando  accedemos a ("http://php.alu5912.me") ya nos saldria la pagina

![imagen](./IMG/5.PNG)

## Sitio web 2:    

    Tenemos que hacer una pagina con Python y que la podamos contralar con el supervisor , la pagina se hara con esta URL ("http://now.alu5912.me")

> ponemos el codigo de python que esta ya en el moodle  

* Primero creamos un entorno virtual con virtualenvs (sirve para instalar app en la misma maquina sin que estan interfieran con otros virtalenvs que instalemos) y lo activamos

![imagen](./IMG/2/1.python.PNG)

![imagen](./IMG/2/003.PNG)   

* Luego miramos si tenemos instalado el flask (un frameroot escrito en python para crear aplicaciones mas rapido)    

![imagen](./IMG/2/004.PNG)

* Ahora  creamos una carpeta en   ~$HOME que se llame "now" ,dentro creamos un  archivo llamado "main.py" y metemos el codigo de python que nos dejaron en el moodle

![imagen](./IMG/2/001.PNG)  


![imagen](./IMG/2/002.PNG)

* En este punto usamos el proceso uwsgi para que escuche peticiones en cierto puerto  ("http://alu5912.me:8080")


![imagen](./IMG/2/005.PNG)  

### *Configuración del sitio web*

* Primero ceramos un fichero de configuracion de uwsgi en la carpeta now para controlar este proceso

![imagen](./IMG/2/006.PNG)  


* Luego creamos un scrip que activara el entorno virtual de la aplicacion  y lanzar en proceso uwsgi.ini   

![imagen](./IMG/2/007.PNG)    

* Le damos permisos al scrip

![imagen](./IMG/2/008.PNG)   

![imagen](./IMG/2/009.PNG)    

* y lo ejecutamos:  

![imagen](./IMG/2/010.PNG)   

### *Parte de nginx*  

* Primero creamos el virtual host:    

![imagen](./IMG/2/011.PNG)   

* Y su respectivo enlace simbolico:    

![imagen](./IMG/2/012.PNG)    

![imagen](./IMG/2/013.PNG)    

* Reiniciamos nginx , ponemos (now.alu5912.me) y nos saldra lo siguiente porque el servicio no esta escuchando en el socket

![imagen](./IMG/2/014.PNG)  

* Para que funcione deberiamos lanzar el scrip ./run.sh  

![imagen](./IMG/2/010.PNG)  

* y ya nos saldria la pagina

![imagen](./IMG/2/016.PNG)   

### *Parte Supervisor*    

* En primero lugar, para que la aplicacion siempre funcione y poder contrlarla debemos instalar supervisor *sudo apt-get install supervisor*  

* Miramos a ver si funciona con "status":  

#### *Configuramos supervisor*  

* Para que funcione supervisor ,necesitamos crear un programa para ello en esta ruta:   

![imagen](./IMG/2/progarm.PNG)

* Ahora creamos un grupo para incluir los desarrollares de supervisor :  

![imagen](./IMG/2/019.PNG)   

* y modificamos el fichero de configuracion de supervisor de la siguiente manera:  

![imagen](./IMG/2/020.PNG)   

* y reiniciamos supervisor  con "reload" para que recargue y coja todos los cambios  


* hacemos un status:  

![imagen](./IMG/2/018.PNG)   

* y ahora si accedemos a ("http://now.alu5912.me") nos mostrara la pagina :   

![imagen](./IMG/2/016.PNG)

#### *Controlamos la aplicacion con supervisor*  

* la paramos :  

![imagen](./IMG/2/para1.PNG)   

![imagen](./IMG/2/parado1.PNG)   


* Y la encendemos :  


![imagen](./IMG/2/start1.PNG)    


![imagen](./IMG/2/016.PNG)   
