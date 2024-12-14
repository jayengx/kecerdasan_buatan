# List =[]

# Dictionary = {key: value}

data_list = [ i + 1 for i in range(10)]
# print(data_list[4]) # 5
# print(data_list[7]) # 5

data_dict = {
    "nama": "Rudi",
    "nilai": 85,
    "Domisili": "Jakarta",
    "lulus": True
}

# print(data_dict["Domisili"])

trx = {
    "discount": 20,
    "percentage": True,
    "max_discount": 10000,
    "tax": 11,
    "items": [
        {
            "product": "Aqua 500ml",
            "price": 5500,
            "qty": 3
        },
        {
            "product": "Indomie goreng",
            "price": 3100,
            "qty": 10
        },
        {
            "product": "Kecap ABC 150ml",
            "price": 10500,
            "qty": 2
        }
    ]
}
# print(trx["items"][1]["price"])

# Subtotal
# subtotal = sum([item["price"] * item["qty"] for item in trx["items"]])
# print(f"Subtotal: Rp.{subtotal}")
# nominal discount
# discount = min(subtotal * trx["discount"]/100, trx["max_discount"]) if trx["percentage"] else trx["discount"]
# print(f"Discount: Rp.{discount}")
# nominal pajak
# tax = (subtotal - discount) * trx["tax"]/100
# print(f"Tax: Rp.{tax}")
# Grand total
# grand_total = subtotal - discount + tax
# print(f"GrandTotal: Rp.{grand_total}")

# BILL

print("======================================================")
print("             BILL                    ")
print("=====================================================")
print("items:")
subtotal = 0
for item in trx["items"]:
    product = item["product"]
    price = item["price"]
    qty = item["qty"]
    print(f"        {product}:   Rp.{price}")
    print(f"                              x{qty} = {price * qty}")
    print("------------------------------------------------------")
    subtotal += price * qty
print(f"                     Subtotal: Rp. {subtotal}")
discount = min(subtotal * trx["discount"]/100, trx["max_discount"]) if trx["percentage"] else trx["discount"]
tax = (subtotal - discount) * trx["tax"]/100
grand_total = subtotal - discount + tax
print(f"                    Discount: Rp. {discount} (-)")
print(f"                         Tax: Rp. {tax}")
print(f"                 Grand Total: Rp. {grand_total}")