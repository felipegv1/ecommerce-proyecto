import { Component } from '@angular/core';
import { Proveedor } from 'src/app/models/proveedor';
import { ProveedorService } from 'src/app/services/proveedor/proveedor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-proveedor',
  templateUrl: './proveedor.component.html',
  styleUrls: ['./proveedor.component.css']
})
export class ProveedorComponent {
  constructor(
    private proveedorService: ProveedorService,
    private router:Router
  ) {}

  proveedores: Proveedor[] = [];

  ngOnInit(): void {
    this.obtenerProveedores();
  }

  obtenerProveedores(): void {
    this.proveedorService.obtenerProveedores().subscribe(
      (data: Proveedor[]) => {
        this.proveedores = data;
      },
      error => {
        console.error('Ocurrió un error al obtener los proveedores', error);
      }
    );
  }




}
