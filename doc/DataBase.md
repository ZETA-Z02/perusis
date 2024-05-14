# BASE DE DATOS ASISTENTE DE VENTAS -> CHATBOT
## ENTIDADES - TABLAS
### categorias
- idcategoria **(PK): INT AUTO INCREMENT UNIQUE**
- categoria **VARCHAR(50)**

### marcas
- idmarca **(PK): INT AUTO INCREMENT UNIQUE**
- marca **VARCHAR(50)**

### productos
- id **(PK): INT AUTO INCREMENT UNIQUE**
- idcategoria **INT NOT NULL**
- idmarca **INT NOT NULL**
- modelo **TEXT**
- tipoventa **VARCHAR(20)**
- stock **INT**
- precio **DOUBLE**


## RELACIONES

1. La tabla *productos* tiene una relacion de uno a muchos **(1:M)** con la tabla *categorias*, ya que una categoría puede tener muchos productos, pero un producto pertenece solo a una categoría.
2. La tabla *productos* tiene una relacion de uno a muchos **(1:M)** con la tabla *marcas* ya que una marca puede tener muchos productos, pero un producto pertenece solo a una marca.