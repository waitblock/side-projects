import tkinter as tk
import applescript
import sys

import re
import subprocess


def get_speaker_output_volume():
    """
    Get the current speaker output volume from 0 to 100.

    Note that the speakers can have a non-zero volume but be muted, in which
    case we return 0 for simplicity.

    Note: Only runs on macOS.
    """
    cmd = "osascript -e 'get volume settings'"
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')

    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()

    volume = int(volume)
    muted = (muted == 'true')

    return 0 if muted else volume

if sys.platform != "darwin":
    print("This bad volume control only works on the darwin kernel (macos)")
    sys.exit(1)

root = tk.Tk()

root.geometry("400x250")
root.title("'Text-Based' Volume Control")

T = tk.Text(root, height=5, width=52)

def change_volume():
    chars = T.get("1.0", 'end-1c')
    if len(chars) > 1000:
        applescript.AppleScript(f"set volume output volume 100").run()
        print(f"Debug: Textbox contained text: {chars}")
        print(f"Debug: Volume changed to: 100")
        return
    applescript.AppleScript(f"set volume output volume {len(chars) * 0.1}").run()
    print(f"Debug: Textbox contained text: {chars}")
    print(f"Debug: Volume changed to: {len(chars) * 0.1}")

def show_volume():
    T.delete('1.0', tk.END)
    T.insert(tk.END, "Current volume is: " + str(get_speaker_output_volume()))

l = tk.Label(root, text="Bad Volume Control UI Thingy")
l2 = tk.Label(root, text="Enter the amount of characters equal to the desired volume")
l3 = tk.Label(root, text="(one character equals 0.1% of the total volume)")

b1 = tk.Button(root, text="Change Volume", command=change_volume)

b2 = tk.Button(root, text="Check Volume", command=show_volume)

b3 = tk.Button(root, text="Quit",
            command=root.destroy)

l.pack()
l2.pack()
l3.pack()
T.pack()
b1.pack()
b2.pack()
b3.pack()

tk.mainloop()