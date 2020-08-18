def main():
	# write code here
	recipet = []

	# Loop of user input (Reciepit is a list of item dictionary)
	while True:
		name = input("Item (enter \"done\" when finished): ")
		if name == "done":
			break
		price = float(input("Price: "))
		quantity = float(input("Quantity: "))
		item = {
			"name": name, 
			"price": price,
			"quantity": quantity
			}
		recipet.append(item)
	
	# Print receipt
	print ("\n------------------------- \nreceipt\n-------------------------")
	total = 0 
	for i in recipet:
		print ("%s  %s  %.3fKD" % (i["quantity"], i["name"], i["price"]*i["quantity"] ))
		
		total += i["price"]*i["quantity"]

	print ("------------------------- \nTotal price: %.3f" % (total))

if __name__ == '__main__':
	main()