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

  ngOnInit(): void {
    this.obtenerProveedores();
  }

  obtenerProveedores(): void {
    this.productoService.obtenerProveedores().subscribe(
      (data: Producto[]) => {
        this.productos = data;
      }
    );
  }

}
