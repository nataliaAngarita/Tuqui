import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {HttpClient} from '@angular/common/http';

const dominio ="localhost:8000/"

@Injectable({
  providedIn: 'root'
})
export class ComunicacionbackendService {

  constructor(private http:HttpClient) { }
  getDineroEfectivo():Observable<any>{
    return this.http.get(dominio+"cuenta/api/CarteraAhorro/");
  }
}
