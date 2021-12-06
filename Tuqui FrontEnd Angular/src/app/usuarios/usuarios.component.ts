import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

//OnInit => se trata de una interfaz de Angular que permite especificar las actividades iniciales cuando se accede a un componente.
//          se asemeja al constructor de una clase.

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.css']
})
export class UsuariosComponent implements OnInit {
  //Atributos de la clase AppComponent. Para acceder al atributo desde el método utilizamos el operador 'this'
  title = 'Tuqui';
  usuario = "Andrés";     
  lugar = "Bogotá";
  zip = "680001";

  categorias = [
    "Todos",
    "Automóvil",
    "Bebé",
    "Ropa"
  ];

  

  
  //Métodos
  constructor() {
    //Inicializa un objeto -> el desarrollo lo aplica una sola vez
    console.log("Aló");
  }

  ngOnInit():void {
    //Inicializar el entorno del componente cada vez que accede a él. Se aplica cada vez que accede al componente
    

    //Almacenar la información general en el navegador del usuario
    //Sólo podemos almacenar información como texto
    localStorage.setItem("usuario", this.usuario);
    localStorage.setItem("lugar", this.lugar);
    localStorage.setItem("categorias", JSON.stringify(this.categorias));
  }



}
