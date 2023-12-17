## Documentation for exceptions

### **1.** NoApiKeyProvidedException - API key not passed
### **2.** BadApiKeyProvidedException - Invalid API key provided
### **3.** ForbiddenAccessException - User violated the access rules
##
### **4.** BadCountryIdException - Invalid country ID
### **5.** BadServiceIdException - Invalid service ID
### **6.** WrongOperatorCodeException - There is no operator with this code
### **7.** InternalErrorException - Server error
### **8.** NoNumbersException - No numbers
### **9.** BlockedUserException - User blocked
### **10.** InsufficientFundsException - No enough founds on the balance
### **11.** CannotBuyMailRuServicesException - User has not been verified for MailRU purchase
### **12.** NoNumbersWithMaxPriceException - A request to obtain numbers with a maximum price limitation cannot be fulfilled
### **13.** TooFastOperationException - Order status changes too often, need to wait for 1 second
### **14.** OrderStatusChangeException - If they try to cancel an order that has already received a code or has already been canceled/completed
### **15.** TooEarlyCancellationException - Canceling an order before a certain time has elapsed 
### **16.** OrderProcessingException - Error during finishing or canceling order
### **17.** UnsupportedOrderTypeException - The API currently covers all order types, but is left for the future if new order types become available
### **18.** TechnicalWorksException - Technical works
### **19.** RentTimeNotAvailableException - Not available with this rent_time
### **20.** InvalidServiceCountException -  Incorrect number of services

##

### **21** ValidationException - The data was transmitted in an incorrect format
### **22** OtherApiException - Made just in case