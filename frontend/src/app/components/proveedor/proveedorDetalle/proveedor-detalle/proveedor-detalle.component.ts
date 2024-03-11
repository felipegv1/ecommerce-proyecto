import { Component } from '@angular/core';
import { Proveedor } from 'src/app/models/proveedor';
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

  proveedor: Proveedor | null = null;
  nombre: string = "";

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const nombre = params['nombre'];
      if (nombre) {
        this.verProveedor(nombre);
      } else {
        // Manejar el caso de que no se haya proporcionado un ID o no sea válido
        console.log('ID de proveedor no proporcionado o no válido');
      }
    });
  }

  verProveedor(nombre: string): void {
    this.proveedorService.obtenerProveedorPorId(nombre).subscribe(
      (data: Proveedor) => {
        this.proveedor = data;
      }
    );
  }
}
