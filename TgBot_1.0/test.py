# from yoomoney import Authorize
# from yoomoney import Client, Quickpay

# if 10/100 < 1:
#     print()

# token = "4100115145345234.F19146ED415926B3660E18EAA4628475E4A45F3AA18B59F72FC8F6034F53C5C65D5672EE8CBB7B32E0EAF5ECD838219F8472BC61BD114980383EFB25C7D8553A69830C6A69F1438832BEF8451EBD9C404F92D1ED2C8C6769F7DF6D9724A5BA895AB12BDFDAC8BF50C11D545D08477532AB2D290148527EBFE4A03FA159F92408"
# client = Client(token)

# quickpay = Quickpay(
#     receiver="4100115145345234",
#     quickpay_form="shop",
#     targets="Sponsor this project",
#     paymentType="SB",
#     sum=10,
#     label="a1b2c3d4e5",
# )

# url = quickpay.redirected_url

# print(quickpay.base_url)
# print(quickpay.redirected_url)


# def check():
#     history = client.operation_history(label="a1b2c3d4e5")
#     print("List of operations:")
#     print("Next page starts with: ", history.next_record)
#     for operation in history.operations:
#         print()
#         print("Operation:", operation.operation_id)
#         print("\tStatus     -->", operation.status)
#         print("\tDatetime   -->", operation.datetime)
#         print("\tTitle      -->", operation.title)
#         print("\tPattern id -->", operation.pattern_id)
#         print("\tDirection  -->", operation.direction)
#         print("\tAmount     -->", operation.amount)
#         print("\tLabel      -->", operation.label)
#         print("\tType       -->", operation.type)


# a = input("Проверка платежа: ")
# if a != "":
#     check()


# user = client.account_info()
# print("Account number:", user.account)
# print("Account balance:", user.balance)
# print("Account currency code in ISO 4217 format:", user.currency)
# print("Account status:", user.account_status)
# print("Account type:", user.account_type)
# print("Extended balance information:")
# for pair in vars(user.balance_details):
# print("\t-->", pair, ":", vars(user.balance_details).get(pair))
# print("Information about linked bank cards:")
# cards = user.cards_linked
# if len(cards) != 0:
# for card in cards:
# print(card.pan_fragment, " - ", card.type)
# else:
# print("No card is linked to the account")


# async def check_pay(message, comment):
#     try:
#         history = client.operation_history(label=str(comment))
#         if history.operations == []:
#             print(f"⚜️Сожалеем но платеж не был обнаружен...")
#         else:
#             for operation in history.operations:
#                 if operation.status == 'success':
#                     print(f"success")

#     except Exception as e:
#         print(e)

# Authorize(
#     # client_id полученный при регистрации приложения (B7598786A657D9CB4F455468BE00C2BD1590A07453456784F85133098E0D9)
#     client_id="E8EAF8EF8178F7CEC7A03B45CD7EB9A4FEAB2CBEA891B19FB7654464CC8E60D6",
#     # 4100115145345234.F19146ED415926B3660E18EAA4628475E4A45F3AA18B59F72FC8F6034F53C5C65D5672EE8CBB7B32E0EAF5ECD838219F8472BC61BD114980383EFB25C7D8553A69830C6A69F1438832BEF8451EBD9C404F92D1ED2C8C6769F7DF6D9724A5BA895AB12BDFDAC8BF50C11D545D08477532AB2D290148527EBFE4A03FA159F92408
#     redirect_uri="https://t.me/DarkPro_bot",
#     scope=["account-info", "operation-history", "operation-details", "incoming-transfers", "payment-p2p", "payment-shop"])
