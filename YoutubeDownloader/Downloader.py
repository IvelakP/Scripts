import customtkinter as ctk
from tkinter import filedialog
from pytube import YouTube
import sys

class YoutubeDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.graphical_interface()
        self.mainloop()

    def graphical_interface(self):
        # Create a root window

        # Title of the window
        self.title("Youtube Downloader")

        # Set min and max dimension of the window
        self.geometry("720x480")
        self.minsize(720, 480)
        self.maxsize(1080, 720)

        # Create a frame
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Create a label and the entrybox for URL
        self.url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here: ")
        self.entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
        self.url_label.pack(pady=(10, 5))
        self.entry_url.pack(pady=(10, 5))

        # Create a download button
        self.download_button = ctk.CTkButton(content_frame, text="Download", command=self.download_video)
        self.download_button.pack(pady=(10, 5))

        # Create a label amd the progress bar  to display the downlaod progress
        self.progress_label = ctk.CTkLabel(content_frame, text="0%")
        self.progress_bar = ctk.CTkProgressBar(content_frame, width=400)
        self.progress_bar.set(0)


        # Create the status label
        self.status_label = ctk.CTkLabel(content_frame, text="", width=100)

        # Bind the closing event to the method

    def download_video(self):
        save_path = self.open_file_dialog()
        url = self.entry_url.get()

        self.status_label.pack(pady=(10, 5))
        self.progress_bar.pack(pady=(10, 5))
        self.progress_label.pack(pady=(10, 5))

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path=save_path)

            # Download the video into a specific directory

            self.status_label.configure(text=f"Downloaded", text_color="white", fg_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_completed = bytes_downloaded / total_size * 100

        self.progress_label.configure(text=str(int(percentage_completed)) + "%")
        self.progress_label.update()

        self.progress_bar.set(float(percentage_completed / 100))

    def open_file_dialog(self):
        folder = filedialog.askdirectory()
        if folder:
            print(f"Selected folder: {folder}")
            return folder
        else:
            sys.exit("Not valid folder")



if __name__ == "__main__":
    app = YoutubeDownloaderApp()

