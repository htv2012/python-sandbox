import jsonpath

import banner
import data

banner.banner("query unit price < 100")
matches = jsonpath.query("$.products[?@.unit_price < 100]", data.inventory).select(
    "unit_price", "name"
)
print("Unit Price  Name")
print("----------  ----")
for obj in matches:
    print(f"{obj['unit_price']:>10}  {obj['name']}")
