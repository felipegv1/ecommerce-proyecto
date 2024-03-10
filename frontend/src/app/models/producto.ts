export interface Producto {
  id?: number;
  nombre: string;
  descripcion: string;
  precio: number;
  categoria: string;
  stock: number;
  // imagen: string; // Suponiendo que guardas la URL de la imagen
  idProveedor: number;
}
