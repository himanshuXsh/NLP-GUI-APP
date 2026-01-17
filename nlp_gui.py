import tkinter as tk
import nlpcloud

API_KEY = "b9c1898fa374db67af21d7a45f3a77424aebe68a"   # 🔴 apni key yahan daalo

database = {}

root = tk.Tk()
root.title("NLP GUI APP")
root.geometry("520x520")

# ---------------- CLEAR SCREEN ----------------
def clear():
    for w in root.winfo_children():
        w.destroy()

# ---------------- DASHBOARD ----------------
def dashboard():
    clear()
    tk.Label(root,text="NLP Dashboard",font=("Arial",18)).pack(pady=20)

    tk.Button(root,text="NER",width=25,command=ner_screen).pack(pady=5)
    tk.Button(root,text="Language Detection",width=25,command=lang_screen).pack(pady=5)
    tk.Button(root,text="Sentiment Analysis",width=25,command=sentiment_screen).pack(pady=5)
    tk.Button(root,text="Logout",width=25,command=login_screen).pack(pady=15)

# ---------------- REGISTER ----------------
def register():
    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if email in database:
        status.config(text="Email already exists",fg="red")
    else:
        database[email] = [name,password]
        status.config(text="Registered Successfully",fg="green")

# ---------------- LOGIN ----------------
def login():
    email = email_entry.get()
    password = pass_entry.get()

    if email in database and password == database[email][1]:
        dashboard()
    else:
        status.config(text="Invalid Login",fg="red")

# ---------------- LOGIN SCREEN ----------------
def login_screen():
    clear()

    tk.Label(root,text="Login / Register",font=("Arial",18)).pack(pady=10)

    tk.Label(root,text="Name").pack()
    global name_entry
    name_entry = tk.Entry(root,width=30)
    name_entry.pack()

    tk.Label(root,text="Email").pack()
    global email_entry
    email_entry = tk.Entry(root,width=30)
    email_entry.pack()

    tk.Label(root,text="Password").pack()
    global pass_entry
    pass_entry = tk.Entry(root,width=30,show="*")
    pass_entry.pack()

    tk.Button(root,text="Register",width=20,command=register).pack(pady=5)
    tk.Button(root,text="Login",width=20,command=login).pack(pady=5)

    global status
    status = tk.Label(root,text="")
    status.pack(pady=10)

# ---------------- NER SCREEN ----------------
def ner_screen():
    clear()
    tk.Label(root,text="NER",font=("Arial",18)).pack()

    para = tk.Entry(root,width=60)
    para.pack(pady=5)
    para.insert(0,"Enter paragraph")

    term = tk.Entry(root,width=60)
    term.pack(pady=5)
    term.insert(0,"Enter entity")

    result = tk.Label(root,text="",wraplength=480)
    result.pack(pady=10)

    def run():
        client = nlpcloud.Client("gpt-oss-120b",API_KEY,gpu=True)
        res = client.entities(para.get(),searched_entity=term.get())
        result.config(text=str(res))

    tk.Button(root,text="Submit",command=run).pack()
    tk.Button(root,text="Back",command=dashboard).pack(pady=10)

# ---------------- LANGUAGE DETECTION ----------------
def lang_screen():
    clear()
    tk.Label(root,text="Language Detection",font=("Arial",18)).pack()

    text = tk.Entry(root,width=60)
    text.pack(pady=5)

    result = tk.Label(root,text="")
    result.pack(pady=10)

    def run():
        client = nlpcloud.Client("python-langdetect",API_KEY,gpu=False)
        res = client.langdetection(text.get())
        result.config(text=str(res))

    tk.Button(root,text="Submit",command=run).pack()
    tk.Button(root,text="Back",command=dashboard).pack(pady=10)

# ---------------- SENTIMENT ----------------
def sentiment_screen():
    clear()
    tk.Label(root,text="Sentiment Analysis",font=("Arial",18)).pack()

    text = tk.Entry(root,width=60)
    text.pack(pady=5)

    result = tk.Label(root,text="")
    result.pack(pady=10)

    def run():
        client = nlpcloud.Client("distilbert-base-uncased-emotion",API_KEY,gpu=False)
        res = client.sentiment(text.get())
        result.config(text=str(res))

    tk.Button(root,text="Submit",command=run).pack()
    tk.Button(root,text="Back",command=dashboard).pack(pady=10)

# ---------------- START ----------------
login_screen()
root.mainloop()
