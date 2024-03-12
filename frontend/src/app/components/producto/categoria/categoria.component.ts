import { Component } from '@angular/core';
import { Producto } from 'src/app/models/producto';
import { ProductoService } from 'src/app/services/producto/producto.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-categoria',
  templateUrl: './categoria.component.html',
  styleUrls: ['./categoria.component.css']
})
export class CategoriaComponent {
  constructor(
    private productoService: ProductoService,
    private route: ActivatedRoute,
  ) {}

  productos: Producto[] = [];
  categoria: string = ''

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.categoria = params['categoria'];
      if (this.categoria) {
        this.obtenerPorCategoria(this.categoria);
      }
    });
  }

  obtenerPorCategoria(categoria: string): void {
    this.productoService.obtenerProductosPorCategoria(categoria).subscribe(
      (data: Producto[]) => {
        this.productos = data;
      }
    )
  }

}
