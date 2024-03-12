import { Component } from '@angular/core';
import { Producto } from 'src/app/models/producto';
import { ProductoService } from 'src/app/services/producto/producto.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-producto-detalle',
  templateUrl: './producto-detalle.component.html',
  styleUrls: ['./producto-detalle.component.css']
})
export class ProductoDetalleComponent {
  constructor(
    private productoService: ProductoService,
    private route: ActivatedRoute,
    private router:Router
  ) {}

  producto: Producto | null = null;

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const nombre = params['nombre'];
      if (nombre) {
        this.verProducto(nombre);
      }
    });
  }

  verProducto(nombre: string): void {
    this.productoService.obtenerProductosPorNombre(nombre).subscribe(
      (data: Producto) => {
        this.producto = data;
      }
    );
  }

}
