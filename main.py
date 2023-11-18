import threading
import random
import time

# Criar um semáforo com valor inicial 1
semaforo_mesa = threading.Semaphore(1)

# Objeto compartilhado
start = random.randint(1, 3)

if start == 1:
    mesa = {"fumo": 0, "papel": 1, "fosforo": 1}
    
elif start == 2:
    mesa = {"fumo": 1, "papel": 0, "fosforo": 1}
    
elif start == 3:
    mesa = {"fumo": 1, "papel": 1, "fosforo": 0}

def funcao_que_acessa_mesa(tipo):
    while True:
        # Adquirir o semáforo, bloqueando o acesso para outras threads
        semaforo_mesa.acquire()

        try:
            # Código que acessa/modifica a mesa
            if tipo == "a":
                if mesa["papel"] >= 1 and mesa["fosforo"] >= 1:
                    mesa["fumo"] += 1
                    mesa["papel"] -= 1
                    mesa["fosforo"] -= 1
                    print("Fumante A conseguiu fumar...")
                    randomize()

                else:
                    print("Fumante A não conseguiu fumar...")

            elif tipo == "b":
                if mesa["fumo"] >= 1 and mesa["fosforo"] >= 1:
                    mesa["fumo"] -= 1
                    mesa["papel"] += 1
                    mesa["fosforo"] -= 1
                    print("Fumante B conseguiu fumar...")
                    randomize()

                else:
                    print("Fumante B não conseguiu fumar...")

            elif tipo == "c":
                if mesa["fumo"] >= 1 and mesa["papel"] >= 1:
                    mesa["fumo"] -= 1
                    mesa["papel"] -= 1
                    mesa["fosforo"] += 1
                    print("Fumante C conseguiu fumar...")
                    randomize()
                else:
                    print("Fumante C não conseguiu fumar...")

        finally:
            # Liberar o semáforo, permitindo que outras threads acessem
            semaforo_mesa.release()

        # Aguardar um pouco antes da próxima iteração
        time.sleep(3)

def randomize():
    number_n = random.randint(1, 3)

    if number_n == 1:
        mesa["papel"] += 1
        mesa["fumo"] += 1
        #print("O vendedor repõe na mesa, após fumante A fumar...")

    elif number_n == 2:
        mesa["papel"] += 1
        mesa["fosforo"] += 1
        #print("O vendedor repõe na mesa, após fumante B fumar...")

    elif number_n == 3:
        mesa["fumo"] += 1
        mesa["fosforo"] += 1
        #print("O vendedor repõe na mesa, após fumante C fumar...")

# Criar threads que executam a função
fumante1 = threading.Thread(target=funcao_que_acessa_mesa, args=('a'))
fumante2 = threading.Thread(target=funcao_que_acessa_mesa, args=('b'))
fumante3 = threading.Thread(target=funcao_que_acessa_mesa, args=('c'))

# Iniciar as threads
fumante1.start()
fumante2.start()
fumante3.start()

# Aguardar até que todas as threads terminem
fumante1.join()
fumante2.join()
fumante3.join()
