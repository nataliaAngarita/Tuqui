import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { PrincipalComponent } from './principal/principal.component';
import { TableroprincipalComponent } from './tableroprincipal/tableroprincipal.component';
import { DineroEfectivoComponent } from './dinero-efectivo/dinero-efectivo.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    UsuariosComponent,
    PrincipalComponent,
    TableroprincipalComponent,
    DineroEfectivoComponent,
    /*ProductosComponent,
    ComprasComponent*/
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
