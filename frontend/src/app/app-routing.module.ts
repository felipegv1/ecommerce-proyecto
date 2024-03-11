import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProveedorComponent } from './components/proveedor/proveedor.component';


const routes: Routes = [
  { path: '', component: ProveedorComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
