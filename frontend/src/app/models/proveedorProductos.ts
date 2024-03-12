import { Proveedor } from './proveedor';
import { Producto } from './producto';

export interface ProveedorConProductos extends Proveedor {
  productos?: Producto[];
}
