import time
class Gst:
    '''
    It is an application which takes input 
    for the product quality, unit, name, price
    and provide calculated final price including 
    the GST of the perticular product category.
    '''
    __final_price=0
    __slab_code=0  
    __gst_applicable = 0
    def __init__(self):
            self._x = "start"       
            self.__gst_slab = {'food-grains':[],
                                'furniture':[],
                                'electronics':[],
                                'cosmetics':[]
                                }
            #product commodity code to store product into that category
            self.__slab_codes = {701:'food-grains',
                                702:'furniture',
                                703:'electronics',
                                704: 'cosmetics'}
                     
    #Method to set list of product in the the its category. 
    def set_gst_attr(self):
                
        
        print("Enter Numeric Code for product category \
            \nas per this \nfood-grains-701\nfurniture-702 \
            \nelectronics-703\ncosmetics-704"
            )
        
        print("\nAfter entering detail \
            \nTo keep continue press enter 'n'\
            \nand\n To finish enter 'q'  "
            )
        time.sleep(8)
        while self._x!="q!":
            try:    
                self.__slab_code =int(input('\nproduct category code :-'))    
            
            except ValueError :
                    print("entered wrong value")
                    self.__slab_code =int(input("product category code :-"))

            #Conforming the code entered for product category is correct or not.
            print("\nHave you entered correct \"product category\" code ?",end=" ")

            if "y"!= input("enter [y/n] "):
                    self.__gst_slabs = int(input("Enter code correctly \nfood-grains-701 \
                                                \nfurniture-702 \nelectronics-703 \
                                                \ncosmetics-704:-"))

            # how much item user want to enter for a product category.
            for _ in range(int(input(f"\nEnter number of item to be enter for \
                             \n{self.__slab_codes[self.__slab_code]}:- "))):

                if self.__slab_code==701:
                    slab_items =self.__set_gst_attri(0)
                    key = 'food-grains'
                elif self.__slab_code==702:
                    slab_items =self.__set_gst_attri(5)
                    key = 'furniture'
                elif self.__slab_code==703:
                    slab_items =self.__set_gst_attri(18)
                    key = 'electronics'
                else:
                    slab_items =self.__set_gst_attri(28)
                    key = 'cosmetics'
                
                
                self.__gst_slab[key].append(slab_items)
            
                
            self._x = "q!" if input("q/n to procced :-") == ("q" or "q!" ) else self._x

    # Method to store the the attribute of product in list.
    def __set_gst_attri(self,gst_percent):
                slab_items = []
                
                if not slab_items:    
                    try:    
                        slab_items.append(int(input("\nEnter product unit :- ")))
                    except ValueError :
                        print("entered wrong value")
                        slab_items.append(int(input("Enter product unit :- ")))
                    try:
                        slab_items.append(input("Enter product name :- "))
                    except ValueError:
                        print("entered wrong value")
                        slab_items.append(input("Enter product name :- "))
                    try:    
                        slab_items.append(float(input("Enter product price :- ")))
                    except ValueError :
                        print("entered wrong value")
                        slab_items.append(float(input("Enter product price :- ")))
                    slab_items.append(gst_percent)
                return slab_items
                
                
    # To output the calculated result of all the product with respective input.
    def get_gst_price(self):
            print("{0:5s} {1:15s} {2:20s} {3:28s} {4:15s}".format("Unit","Commodity","Initial Unit Price","Applicable GST","Final Price"))   
            for key in self.__gst_slab:
                if not (self.__gst_slab[key]):
                    continue
                else:
                
                    for final_price,i in self.gst_total_price(key):
                    
                        print("%2d %8s %20.2f %23d %26.2f"%(self.__gst_slab[key][i][0],
                            self.__gst_slab[key][i][1],
                            self.__gst_slab[key][i][2],
                            self.__gst_slab[key][i][3],
                            final_price))    

    # Method for calculating final price
    def gst_total_price(self,key):
        for i in range(len(self.__gst_slab[key])):
            final_value =  self.__gst_slab[key][i][0] * self.__gst_slab[key][i][2] + \
                    self.__gst_slab[key][i][0] * self.__gst_slab[key][i][2] * \
                    self.__gst_slab[key][i][3]/100

            yield final_value,i

            

if __name__ == '__main__':
    gst = Gst()
    gst.set_gst_attr()
    gst.get_gst_price()