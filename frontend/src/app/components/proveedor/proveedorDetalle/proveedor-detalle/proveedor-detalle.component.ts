import { Component } from '@angular/core';
import { ProveedorConProductos } from 'src/app/models/proveedorProductos';
import { ProveedorService, } from 'src/app/services/proveedor/proveedor.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-proveedor-detalle',
  templateUrl: './proveedor-detalle.component.html',
  styleUrls: ['./proveedor-detalle.component.css']
})
export class ProveedorDetalleComponent {
  constructor(
    private proveedorService: ProveedorService,
    private route: ActivatedRoute,
    private router:Router
  ) {}

  proveedorConProductos: ProveedorConProductos | null = null;

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const nombre = params['nombre'];
      if (nombre) {
        this.verProveedor(nombre);
      }
    });
  }

  verProveedor(nombre: string): void {
    this.proveedorService.obtenerProveedorPorId(nombre).subscribe(
      (data:ProveedorConProductos) => {
        this.proveedorConProductos = data;
      }
    );




  }
}
