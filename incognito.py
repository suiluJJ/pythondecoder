#importataan tkinter GUI:a varten ja base64 encodausta/decodausta varten
import tkinter as tk
import base64

class Incognito:
    def __init__(self):
        #määritetään ohjelman juuri
        self.root = tk.Tk()

        #määritetään ikkunan koko ja ohjelman nimi
        self.root.geometry("600x700")
        self.root.title("Incognito")

        #annetaan otsikko
        self.label = tk.Label(self.root, text="Incognito", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        #luodaan input boksi
        self.input = tk.Text(self.root, height=15, font=("Arial", 12))
        self.input.pack(padx=10, pady=10)

        #lisätään näppäimille ikkuna
        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)

        #määritetään ohjelman näppäimet
        button1 = tk.Button(buttonframe, text="b64 enc", font=('Arial', 10), command=self.b64_enc)
        button1.grid(row=0, column=0, sticky=tk.W+tk.E)

        button2 = tk.Button(buttonframe, text="hex enc", font=('Arial', 10), command=self.hex_enc)
        button2.grid(row=0, column=1, sticky=tk.W+tk.E)

        button3 = tk.Button(buttonframe, text="b64 dec", font=('Arial', 10), command=self.b64_dec)
        button3.grid(row=1, column=0, sticky=tk.W+tk.E)

        button4 = tk.Button(buttonframe, text="hex dec", font=('Arial', 10), command=self.hex_dec)
        button4.grid(row=1, column=1, sticky=tk.W+tk.E)
        #venytetään näppäinten tausta koko ikkunan leveydelle
        buttonframe.pack(fill='x')

        #luodaan output laatikko
        self.output = tk.Text(self.root, height=15, font=('Arial', 12), state="disabled")
        self.output.pack(padx=10, pady=10)
        self.root.mainloop()

    #luodaan funktiot encodausta/decodausta varten
    def b64_enc(self):
        viesti = self.input.get("1.0", tk.END).rstrip()
        viesti = viesti.encode()
        viesti_b64 = base64.b64encode(viesti)
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("end", viesti_b64)
        self.output.config(state="disabled")

    def hex_enc(self):
        viesti = self.input.get("1.0", tk.END).rstrip()
        viesti = viesti.encode()
        viesti_hex = base64.b16encode(viesti)
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("end", viesti_hex)
        self.output.config(state="disabled")

    def b64_dec(self):
        viesti = self.input.get("1.0", tk.END).rstrip()
        viesti = viesti.encode()
        viesti_b64 = base64.b64decode(viesti)
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("end", viesti_b64)
        self.output.config(state="disabled")
        
    def hex_dec(self):
        viesti = self.input.get("1.0", tk.END).rstrip()
        viesti = viesti.encode()
        viesti_hex = base64.b16decode(viesti)
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("end", viesti_hex)
        self.output.config(state="disabled")


Incognito()