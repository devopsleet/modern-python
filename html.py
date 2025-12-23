import tkinter as tk
from tkinter import scrolledtext, messagebox

def generate_html():
    item_details = item_details_entry.get("1.0", tk.END).strip()
    title = title_entry.get().strip()
    description = description_entry.get("1.0", tk.END).strip()
    historical_significance = historical_entry.get("1.0", tk.END).strip()
    provenance = provenance_entry.get("1.0", tk.END).strip()
    estimate = estimate_entry.get().strip()

    if not title:
        messagebox.showerror("Missing Field", "Please enter the Title.")
        return

    html_output = f"""
<div class="item-description">
    <h2>{title}</h2>
    <p><strong>Item Details:</strong> {item_details}</p>
    <p><strong>Description:</strong> {description}</p>
    <p><strong>Historical Significance:</strong> {historical_significance}</p>
    <p><strong>Provenance and Authentication:</strong> {provenance}</p>
    <p><strong>Estimate:</strong> {estimate}</p>
</div>
    """.strip()

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, html_output)

# Create main window
root = tk.Tk()
root.title("HTML Description Generator")
root.geometry("700x750")
root.resizable(False, False)

# --- Input Fields ---
tk.Label(root, text="Title:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
title_entry = tk.Entry(root, width=80)
title_entry.pack(padx=10, pady=5)

tk.Label(root, text="Item Details:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
item_details_entry = scrolledtext.ScrolledText(root, width=80, height=3)
item_details_entry.pack(padx=10, pady=5)

tk.Label(root, text="Description:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
description_entry = scrolledtext.ScrolledText(root, width=80, height=4)
description_entry.pack(padx=10, pady=5)

tk.Label(root, text="Historical Significance:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
historical_entry = scrolledtext.ScrolledText(root, width=80, height=3)
historical_entry.pack(padx=10, pady=5)

tk.Label(root, text="Provenance and Authentication:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
provenance_entry = scrolledtext.ScrolledText(root, width=80, height=3)
provenance_entry.pack(padx=10, pady=5)

tk.Label(root, text="Estimate:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
estimate_entry = tk.Entry(root, width=80)
estimate_entry.pack(padx=10, pady=5)

# Generate Button
tk.Button(root, text="Generate HTML", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_html).pack(pady=10)

# Output Box
tk.Label(root, text="Generated HTML:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
output_box = scrolledtext.ScrolledText(root, width=80, height=15, font=("Courier", 10))
output_box.pack(padx=10, pady=5)

# Start GUI
root.mainloop()
