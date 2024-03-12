import { Component } from '@angular/core';
import { Producto } from 'src/app/models/producto';
import { ProductoService } from 'src/app/services/producto/producto.service';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})
export class ProductoComponent {
  constructor(
    private productoService: ProductoService,
  ) {}

  productos: Producto[] = [];
  categorias: string[] = [];

  ngOnInit(): void {
    this.obtenerProductos();


  }

  obtenerProductos(): void {
    this.productoService.obtenerProductos().subscribe(
      (data: Producto[]) => {
        this.productos = data;
        const categoriasMap = this.productos.map(producto => producto.categoria);
        this.categorias = [...new Set(categoriasMap)];
      }
    );
  }

}
