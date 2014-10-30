
import MySQLdb
import MySQLdb.cursors
from htmltmpl import TemplateManager, TemplateProcessor

# Define some constants.
DB = "test"
USER = ""
PASSWD = ""
TABLE = """

    CREATE TABLE IF NOT EXISTS Products (
        id            INTEGER        NOT NULL AUTO_INCREMENT,
        name          VARCHAR(255)   NOT NULL,
        CONSTRAINT pkey_id
            PRIMARY KEY(id)
    )
    
"""

template = TemplateManager().prepare("products.tmpl")
tproc = TemplateProcessor()
                
# Assign a string to template variable named "title".
tproc.set("title", "Our products")
        
# Connect the database. Create the table.
db = MySQLdb.connect(db = DB, user = USER, passwd = PASSWD,
                     cursorclass = MySQLdb.cursors.DictCursor)
create_cur = db.cursor()
create_cur.execute(TABLE)
create_cur.close()

# Insert some data.
insert_cur = db.cursor()
insert_cur.executemany("""

    INSERT INTO Products (name) VALUES (%(name)s)

""", [
    {"name": "Seagate"},
    {"name": "Conner"},
    {"name": "Maxtor"}
])
insert_cur.close()


# Select the products.
products_cur = db.cursor()
products_cur.execute("""

    SELECT id, name
    FROM Products
    
""")

# Append product data in form of mappings (dictionaries) to the
# products list.
products = []
for i in range(products_cur.rowcount):
    products.append(products_cur.fetchone())
products_cur.close()
db.close()

# Assign the products list to template loop identifier 'Products'.
# NOTE: htmltmpl automatically converts all the values
# to strings using str().
tproc.set("Products", products)
        
# Process the template and print the result.
print tproc.process(template)
