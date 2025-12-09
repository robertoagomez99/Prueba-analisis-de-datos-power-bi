drop table if exists fact_ventas cascade;
drop table if exists  dim_producto cascade;
drop table if exists  dim_cliente cascade;
drop table if exists  dim_ubicacion cascade;
drop table if exists  dim_canal cascade;
drop table if exists  staging_ventas cascade; 

create table if not exists dim_producto (
    id_producto int primary key,
    sku varchar(50),
    nombre_producto varchar(255),
    categoria varchar(100)
);

create table if not exists dim_cliente (
    id_cliente int primary key,
    tipo_cliente varchar(100)
);

create table if not exists dim_ubicacion (
    id_ubicacion int primary key,
    ciudad varchar(100)
);

create table if not exists dim_canal (
    id_canal int primary key,
    tipo_venta varchar(50)
);

create table if not exists fact_ventas (
    id_venta int primary key,
    fecha date,
    id_producto int,
    id_cliente int,
    id_ubicacion int,
    id_canal int,
    cantidad int,
    precio_unitario decimal(10,2),
    descuento decimal(10,2),
    costo_envio decimal(10,2),
    venta_total decimal(15,2),
    constraint fk_prod foreign key (id_producto) references dim_producto(id_producto),
    constraint fk_cli foreign key (id_cliente) references dim_cliente(id_cliente),
    constraint fk_ubi foreign key (id_ubicacion) references dim_ubicacion(id_ubicacion),
    constraint fk_canal foreign key (id_canal) references dim_canal(id_canal)
);
