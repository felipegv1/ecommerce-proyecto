import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Producto } from 'src/app/models/producto';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  private url = 'http://localhost:8000/'

  proveedor: Producto[] = [];

  constructor(private http: HttpClient) { }

  public obtenerProductos(): Observable<Producto[]> {
    return this.http.get<Producto[]>(`${this.url}productos/`);
  }


  public obtenerProductosPorNombre(nombre: string): Observable<Producto> {
    const url = `${this.url}productos/${nombre}`;
    return this.http.get<Producto>(url);
  }

  obtenerProductosPorCategoria(categoria: string): Observable<Producto[]> {
    const url = `${this.url}categoria/${categoria}`;
    return this.http.get<Producto[]>(url);
  }

  crearProducto(producto: Producto): Observable<Producto> {
    return this.http.post<Producto>(`${this.url}productos/crearProducto/`, producto);
  }
}
