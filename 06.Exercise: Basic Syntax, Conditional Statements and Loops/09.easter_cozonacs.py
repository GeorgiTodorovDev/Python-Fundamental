budget = float(input())
price_1kg_flour = float(input())

egg_pack_price = price_1kg_flour * 0.75
milk_1l_price = price_1kg_flour + (price_1kg_flour * 0.25)
milk_025ml_price = milk_1l_price / 4
ttl_price_cozonac = price_1kg_flour + egg_pack_price + milk_025ml_price
cozonac_counter = 0
egg = 0
while budget >= ttl_price_cozonac:
    budget -= ttl_price_cozonac
    cozonac_counter += 1
    egg += 3
    if cozonac_counter % 3 == 0:
        egg_lose = cozonac_counter - 2
        egg -= egg_lose
print(f"You made {cozonac_counter:.0f} cozonacs! Now you have {egg:.0f} eggs and {budget:.2f}BGN left.")