import os
import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tmb
import tkinter.ttk as ttk
import pafy
import subprocess
import threading

def download_button_fn (button,link_entry,progress_bar):

    def daemon_fn():

        def progess_bar_update_fn(total, recvd, ratio, rate, eta): 

            current_progress = (recvd/total)*100
            progress_bar.configure(value=current_progress)

            return(0)

        button.state(["disabled"])
        
        url = link_entry.get()
        if (url):

            savepath = tfd.askdirectory()
            if savepath:

                video = pafy.new(url)
                filename = video.title + '.webm'
                savename = video.title + '.mp3'


                audio_stream = video.getbestaudio()
                
                try:
                    audio_stream.download(filepath=savepath)
                    
                    subprocess.run(["ffmpeg","-i",filename,"-f", "mp3","-ab", "192000","-vn",savename])
                    os.remove(filename)
                except:
                    tmb.showerror(title="Download Error",message="Unable to download audio from link")
          
        else:
            tmb.showerror(title="Download Error", message="Please enter a URL first !")                                      
        button.state(["!disabled"])

        return()
    
    t1 = threading.Thread(target=daemon_fn,daemon=True)
    t1.start()

    return()

root = tk.Tk()
root.resizable(width=False,height=False)
root.title("YouTube mp3 Downloader")

link_label = ttk.Label(master=root,text="YouTube link:")
link_label.grid(row=0,column=0,sticky='nsew')

link_entry = ttk.Entry(master=root,width=100)
link_entry.grid(row=0,column=1,sticky='nsew')

download_button = ttk.Button(master=root,text="Download Audio as mp3")
download_button.grid(row=1,column=1,sticky='nsew')

progress_label = ttk.Label(master=root,text="Progress:")
progress_label.grid(row=2,column=0,sticky='nsew')

progress_bar = ttk.Progressbar(master=root)
progress_bar.grid(row=2,column=1,sticky='nsew')

download_button.configure(command=lambda:download_button_fn(download_button,link_entry,progress_bar))

root.mainloop()
