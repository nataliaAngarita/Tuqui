import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppComponent } from '../app.component';
import { ComunicacionbackendService } from '../comunicacionbackend.service';

@Component({
  selector: 'app-dinero-efectivo',
  templateUrl: './dinero-efectivo.component.html',
  styleUrls: ['./dinero-efectivo.component.css']
})
export class DineroEfectivoComponent implements OnInit {

  constructor(private router:Router, private app:AppComponent, private comunicacion:ComunicacionbackendService) { }

  ngOnInit(): void {
  }

}
