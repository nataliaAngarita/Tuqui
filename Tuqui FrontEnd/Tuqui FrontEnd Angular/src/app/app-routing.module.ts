import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './principal/principal.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { TableroprincipalComponent } from './tableroprincipal/tableroprincipal.component';
import { DineroEfectivoComponent } from './dinero-efectivo/dinero-efectivo.component';

const routes: Routes = [
  { path: 'usuarios', component: UsuariosComponent},
  { path: '', component: PrincipalComponent },
  { path: 'tableroprincipal', component: TableroprincipalComponent },
  { path: 'dinero_efectivo', component: DineroEfectivoComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
