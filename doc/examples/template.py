
from htmltmpl import TemplateManager, TemplateProcessor

# Compile or load already precompiled template.
template = TemplateManager().prepare("template.tmpl")
tproc = TemplateProcessor()

# Set the title.
tproc.set("title", "Our customers")

# Create the 'Customers' loop.
customers = []

# First customer.
customer = {}
customer["name"] = "Joe Sixpack"
customer["city"] = "Los Angeles"
customer["new"] = 0
customers.append(customer)

# Second customer.
customer = {}
customer["name"] = "Paul Newman"
customer["city"] = "New York"
customer["new"] = 1
customers.append(customer)

tproc.set("Customers", customers)

# Print the processed template.
print(tproc.process(template))
