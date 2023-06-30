Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> import tkinter as tk
... import time
... 
... class AMRAP_Counter:
...     def __init__(self, master):
...         self.master = master
...         master.title("AMRAP Counter")
...         master.geometry("400x300")
... 
...         # Label para exibir o tempo
...         self.time_label = tk.Label(master, text="00:00", font=("Arial", 50))
...         self.time_label.pack(pady=50)
... 
...         # Lista de exercícios
...         self.exercises = ["Pull-ups", "Push-ups", "Squats"]
...         self.repetitions = [0, 0, 0]
... 
...         # Labels para os exercícios e repetições
...         self.exercise_labels = []
...         self.repetition_labels = []
...         for i in range(len(self.exercises)):
...             exercise_label = tk.Label(master, text=self.exercises[i], font=("Arial", 20))
...             repetition_label = tk.Label(master, text="Repetições: " + str(self.repetitions[i]), font=("Arial", 12))
...             exercise_label.pack()
...             repetition_label.pack()
...             self.exercise_labels.append(exercise_label)
...             self.repetition_labels.append(repetition_label)
... 
...         # Botão para iniciar o cronômetro
...         self.start_button = tk.Button(master, text="Iniciar", font=("Arial", 16), command=self.start_timer)
...         self.start_button.pack(pady=50)
... 
        # Variáveis para controlar o cronômetro
        self.start_time = 0
        self.running = False

    def start_timer(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.start_button.config(text="Parar", command=self.stop_timer)
            self.master.after(1000, self.update_timer)

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Iniciar", command=self.start_timer)

    def update_timer(self):
        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            self.time_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.master.after(1000, self.update_timer)

    def add_repetition(self, exercise_index):
        if self.running:
            self.repetitions[exercise_index] += 1
            self.repetition_labels[exercise_index].config(text="Repetições: " + str(self.repetitions[exercise_index]))

root = tk.Tk()
amrap_counter = AMRAP_Counter(root)
root.mainloop()
