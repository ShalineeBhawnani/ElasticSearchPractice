
def userInputAmount(original_price):
    net_price = original_price + 24.7

    gst_amount = net_price - original_price
    gst_percent = (( gst_amount*100 )/original_price)
    print(round(gst_percent),end='') 
    print("%")

# userInputAmount(float(input("Input Original Price:")))

def fixedGST(original_price):
    gst_included_amount =  original_price * 118/100
    print(gst_included_amount)
    
    gst_amount = gst_included_amount - original_price
    print(gst_amount)
    gst_percent = (( gst_amount*100)/original_price)
    print(gst_percent)

fixedGST(float(input("Enter Amount:")))