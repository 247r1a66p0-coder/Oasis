import socket
import threading
import tkinter as tk

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(('127.0.0.1', 5555))

root = tk.Tk()
root.title("Chat Application")

chat_box = tk.Text(root)
chat_box.pack()

message_entry = tk.Entry(root, width=40)
message_entry.pack()

def receive():

    while True:

        try:
            message = client.recv(1024).decode()

            chat_box.insert(
                tk.END,
                message + "\n"
            )

        except:
            client.close()
            break

def send_message():

    message = message_entry.get()

    client.send(message.encode())

    message_entry.delete(0, tk.END)

send_button = tk.Button(
    root,
    text="Send",
    command=send_message
)

send_button.pack()

thread = threading.Thread(target=receive)
thread.start()

root.mainloop()