import random

palabras = ["telefono", "automovil", "perico", "arco", "probabilidad"]

def palabra():
    return random.choice(palabras)

def juego():
    w = palabra()
    guessed = "-" * len(w)
    attempts = 6
    guessed_letters = set()  
    print("Bienvenido")
    print("La palabra tiene ", len(w), " letras.")
    print(guessed)

    while attempts > 0 and "-" in guessed:
        guess = input("Ingresa una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue

        if guess in guessed_letters:
            print("Ya has intentado esta letra. Intenta con otra.")
            continue

        guessed_letters.add(guess)  
        if guess in w:
            guessed = "".join([guess if w[i] == guess else guessed[i] for i in range(len(w))])
        else:
            attempts -= 1
            print(f"Letra incorrecta. Te quedan {attempts} intentos.")

        print(guessed)

    if "-" not in guessed:
        print("adivinaste la palabra que era:", w)
    else:
        print("perdiste La palabra era:", w)

if __name__ == "__main__":
    juego()
