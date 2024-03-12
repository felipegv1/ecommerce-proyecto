import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProveedorComponent } from './components/proveedor/proveedor.component';
import { ProveedorDetalleComponent } from './components/proveedor/proveedorDetalle/proveedor-detalle/proveedor-detalle.component';
import { ProductoComponent } from './components/producto/producto.component';
import { ProductoDetalleComponent } from './components/producto/productoDetalle/producto-detalle/producto-detalle.component';
import { CategoriaComponent } from './components/producto/categoria/categoria.component';
import { CrearProductoComponent } from './components/producto/crear-producto/crear-producto.component';

const routes: Routes = [
  { path: '', component: ProveedorComponent},
  { path: 'proveedores', component: ProveedorComponent },
  { path: 'proveedores/:nombre', component: ProveedorDetalleComponent },
  { path: 'productos', component: ProductoComponent},
  { path: 'productos/:nombre', component: ProductoDetalleComponent },
  { path: 'categoria/:categoria', component: CategoriaComponent },
  { path: 'crearProducto', component: CrearProductoComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
