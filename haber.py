import feedparser
import tkinter as tk
from tkinter import scrolledtext

# RSS feed'in URL'si
url = "https://www.cnnturk.com/feed/rss/dunya/gallery"

# RSS feed'i parse et
news = feedparser.parse(url)

# Haberleri ayrı pencerelerde gösteren fonksiyon
def show_news(title, summary):
    news_window = tk.Toplevel(root)
    news_window.title(title)
    
    text_area = scrolledtext.ScrolledText(news_window, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.INSERT, summary)
    text_area.config(state=tk.DISABLED)

# Ana pencere oluştur
root = tk.Tk()
root.title("Haberler")

# Haberleri listele ve butonlarla göster
for information in news.entries:
    button = tk.Button(root, text=information.title, command=lambda info=information: show_news(info.title, info.summary))
    button.pack(padx=10, pady=5, fill=tk.X)

# Ana döngüyü başlat
root.mainloop()
