seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# create boolean overstock_risk 
overstock_risk = (seasonal == True) and (current_stock > high_stock_threshold)

# create boolean discount_eligible
discount_eligible = not selling_well and not on_sale

# create boolean make_discount 
make_discount = (overstock_risk == True) or (discount_eligible == True)

print('Should the item be discounted?', make_discount)