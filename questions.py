import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#inicio puntaje del jugador
puntaje = 0
# selecciono de forma aleatoria las tres preguntas a realizar
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question, answer_option, correct_answers in questions_to_ask:
  print(question)
  for i, answer in enumerate(answer_option):
    print(f"{i + 1}. {answer}")
  # El usuario tiene 2 intentos para responder correctamente
  for intento in range(2):
    user_answer = (input("Respuesta: "))
    #verifico si la respuesta es valida
    #verifico que sea un numero
    if user_answer.isdigit():
      user_answer = int(user_answer)-1
      #verifico que este en el rango
      if user_answer in range(4):
        # Se verifica si la respuesta es correcta y modifico el puntaje
        if user_answer == correct_answers:
          print("¡Correcto!")
          puntaje += 1
          break
        else:
          puntaje -= 0.5
      #si la respuesta no fue valida
      else:
        print("Respuesta no válida")
        exit(1)
    else:
      print("Respuesta no válida")
      exit(1)
  else:
     # Si el usuario no responde correctamente después de 2 intentos,
     # se muestra la respuesta correcta
     print("Incorrecto. La respuesta correcta es:")
     print(answer_option[correct_answers])
  # Se imprime un blanco al final de la pregunta
  print()
# imprimo el puntaje del jugador
print("fin del juego")
print("puntaje obtenido:", puntaje)
