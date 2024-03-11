import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Producto } from 'src/app/models/producto';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  proveedor: Producto[] = [];

  constructor(private http: HttpClient) { }

  public obtenerProveedores(): Observable<Producto[]> {
    return this.http.get<Producto[]>('http://localhost:8000/productos/');
  }


  public obtenerProveedorPorId(nombre: string): Observable<Producto> {
    const url = `http://localhost:8000/productos/${nombre}`;
    return this.http.get<Producto>(url);
  }
}
