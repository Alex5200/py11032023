import time

correct_password = "password"

def ask_password(cor_password):
    # cor_password == correct_password
    couner_error = 0
    while couner_error != 3:
        input_pass = input()
        if input_pass == cor_password:
            print("Пароль принят")
            couner_error = 3
        else:
            couner_error = couner_error + 1
            if couner_error == 3:
                print("В доступе отказано")



ask_password("123")
for i in range(1, 4, 1):
    print("sec pause",i)
    time.sleep(1)

ask_password("asda")


