
# def cliCommands():
#     while(True):
#         command = input()
        
#         if command == 'quit':
#             break

#         elif command == 'history':
#             print('show history') #TODO

#         else:
#             try:
#                 left_currency, right_currency = command.split() 
#                 print(left_currency + " " + str(len(right_currency)))
#             except:
#                 print("input should be in format:  val val")

#             if(len(left_currency) or len(right_currency)) != 3:
#                 print("input should be in format:  val val!")

        # elif (len(command) != 7) or (" " not in command) or (command[0] == " "):
        #     print("Wrong command, please write again!")
            
        # else:   
        #     left_currency, right_currency = command.split()

        #     if(len(left_currency) or len(right_currency)) != 3:
        #         print("Wrong command, please write again!")
        #     elif (" " in left_currency) or (" " in right_currency):
        #         print("Wrong command, please write again!")
        #     else:
        #         print(" " in right_currency)
        #         print("Asking request for: " + left_currency + " " + right_currency)