import tkinter as tk
import time

class AMRAP_Counter:
    def __init__(self, master):
        self.master = master
        master.title("AMRAP Counter powered by DANIBOY")
        master.geometry("700x550")

        # Label para exibir o tempo
        self.time_label = tk.Label(master, text="00:00", font=("Roboto", 50))
        self.time_label.pack(pady=25)

        # Lista de exercícios
        self.exercises_list = ["Air Squat", "Back Squat", "Bench Press", "Box Jump", "Burpee", "Clean", "Deadlift", "Double Under", "Front Squat", "Handstand Push-up", "Kettlebell Swing", "Muscle Up", "Overhead Squat", "Pull-up", "Push Press", "Push-up", "Row", "Sit-up", "Snatch", "Squat Clean", "Thruster", "Toes-to-bar", "Wall Ball"]

        # Multipla escolha de exercícios
        self.exercises_selection = []
        self.exercises_selection_labels = []
        self.exercises_selection_frame = tk.Frame(master)
        self.exercises_selection_frame.pack(pady=10)

        for i in range(len(self.exercises_list)):
            var = tk.IntVar()
            checkbutton = tk.Checkbutton(self.exercises_selection_frame, text=self.exercises_list[i], variable=var, onvalue=1, offvalue=0)
            checkbutton.pack(side="left", padx=5, pady=5)
            self.exercises_selection.append(var)

            label = tk.Label(self.exercises_selection_frame, text="0", font=("PT Sans", 16))
            label.pack(side="left", padx=5, pady=5)
            self.exercises_selection_labels.append(label)

        # Botão para adicionar repetições
        self.add_repetition_button = tk.Button(master, text="Adicionar repetição", font=("PT Sans", 16), command=self.add_repetition)
        self.add_repetition_button.pack(pady=10)

        # Botão para iniciar o cronômetro
        self.start_button = tk.Button(master, text="Iniciar", font=("PT Sans", 16), command=self.start_timer)
        self.start_button.pack(pady=30)

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

    def add_repetition(self):
        for i in range(len(self.exercises_selection)):
            if self.exercises_selection[i].get() == 1:
                current_value = int(self.exercises_selection_labels[i].cget("text"))
                self.exercises_selection_labels[i].config(text=str(current_value + 1))

root = tk.Tk()
amrap_counter = AMRAP_Counter(root)
root.mainloop()
