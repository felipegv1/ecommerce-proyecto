import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProveedorComponent } from './components/proveedor/proveedor.component';
import { ProductoComponent } from './components/producto/producto.component';
import { FacturaComponent } from './components/factura/factura.component';
import { ClienteComponent } from './components/cliente/cliente.component';
import { ProveedorDetalleComponent } from './components/proveedor/proveedorDetalle/proveedor-detalle/proveedor-detalle.component';
import { HeaderComponent } from './components/header/header.component';
import { ProductoDetalleComponent } from './components/producto/productoDetalle/producto-detalle/producto-detalle.component';
import { CategoriaComponent } from './components/producto/categoria/categoria.component';
import { CrearProductoComponent } from './components/producto/crear-producto/crear-producto.component';
import { CategoriasComponent } from './components/categorias/categorias.component';

@NgModule({
  declarations: [
    AppComponent,
    ProveedorComponent,
    ProductoComponent,
    FacturaComponent,
    ClienteComponent,
    ProveedorDetalleComponent,
    HeaderComponent,
    ProductoDetalleComponent,
    CategoriaComponent,
    CrearProductoComponent,
    CategoriasComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
