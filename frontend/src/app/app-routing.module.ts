import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProveedorComponent } from './components/proveedor/proveedor.component';
import { ProveedorDetalleComponent } from './components/proveedor/proveedorDetalle/proveedor-detalle/proveedor-detalle.component';
import { ProductoComponent } from './components/producto/producto.component';
import { ProductoDetalleComponent } from './components/producto/productoDetalle/producto-detalle/producto-detalle.component';

const routes: Routes = [
  { path: '', component: ProveedorComponent},
  { path: 'proveedores', component: ProveedorComponent },
  { path: 'proveedores/:nombre', component: ProveedorDetalleComponent },
  { path: 'productos', component: ProductoComponent},
  { path: 'producto/:nombre', component: ProductoDetalleComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
