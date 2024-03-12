import { Component } from '@angular/core';
import { Producto } from 'src/app/models/producto';
import { ProductoService } from 'src/app/services/producto/producto.service';

@Component({
  selector: 'app-crear-producto',
  templateUrl: './crear-producto.component.html',
  styleUrls: ['./crear-producto.component.css']
})
export class CrearProductoComponent {
  constructor(
    private productoService: ProductoService,
  ) {}

  categorias: string[] = ['Pantalla', 'Mouse', 'Teclado', 'Disco duro', 'Juguetes'];

  producto: Producto = {
    nombre: '',
    descripcion: '',
    precio: 0,
    categoria: '',
    stock: 1,
    idProveedor: 1,
  };

  crearProducto(): void {
    this.productoService.crearProducto(this.producto).subscribe({
      next: (productoCreado) => {
        console.log('Producto creado con éxito', productoCreado);
        // Aquí puedes, por ejemplo, redirigir al usuario o limpiar el formulario
      },
      error: (error) => console.error('Error al crear producto', error)
    });
  }


}
