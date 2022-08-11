CUSTOMER ={
    "NAME":'customers',
    "SHAPE":"""
        first_name text,
        last_name text,
        email text
    """,
    "CREATE":"insert into customers values (?,?,?)",
    "READ":"select * from customers"
}