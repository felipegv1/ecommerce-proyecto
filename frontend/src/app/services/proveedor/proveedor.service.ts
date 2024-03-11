import { Injectable } from '@angular/core';
import { Proveedor } from 'src/app/models/proveedor';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProveedorService {
  proveedor: Proveedor[] = [];

  constructor(private http: HttpClient) { }

  public obtenerProveedores(): Observable<Proveedor[]> {
    return this.http.get<Proveedor[]>('http://localhost:8000/proveedores/');
  }

}
