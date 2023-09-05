import speech_recognition as sr
import os
import pyttsx3
import psutil
import webbrowser
import pywhatkit
import pygame
import requests
import wikipedia
import pyjokes
import platform
import datetime
from PIL import ImageGrab
import datetime
from qrgen import makeQRCode
from tabulate import tabulate
from sketchpy import library as lib

# ini buat qr code, jadwal, sama main musik
ig_username = 'zalz_ummar18'
favourite_song_link = ''
qr_code_link = 'https://instagram.com/zalz_ummar19'
playlist_link = ''
schedule = {}


class PersonalBot:
    # ini befungsi untuk set langsung voice mode ketika program baru dijalankan
    def __init__(self):
        # saat awal dijalankan, sistemnya menerima inputan teks, kalo mau nerima inputan suara ganti aja jadi voice
        self.command_mode = 'text'
        self.reminders = []

    def Listen(self):
        """
        The function listens for voice commands if the command mode is set to 'voice', otherwise it
        prompts the user to enter a command through text.
        :return: the user's command/query. If the command mode is set to 'voice', it uses speech
        recognition to listen to the user's voice and convert it into text. If the command mode is set
        to 'text', it prompts the user to enter a command/query manually.
        """
        if self.command_mode == 'voice':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening for orders..')
                r.pause_threshold = 0.7
                audio = r.listen(source)

                try:
                    print("Recognizing orders..")
                    Query = r.recognize_google(audio, language='en-in')
                    return Query

                except Exception as e:
                    print(e)
                    jarvis.Speak("Can you please say your orders again?")
                    print("Can you please say your orders again?")
                    return "None"
        elif self.command_mode == 'text':
            query = input('Enter command: ')
            return query

    def TakeScreenshot(self):
        """
        The function `TakeScreenshot` captures the current screen and saves it as a PNG image file with
        a timestamp in the filename.
        """
        screenshot = ImageGrab.grab()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"./assets/img/screenshot/screenshot_{current_time}.png"
        screenshot.save(file_name)
        print(f"Screenshot saved as {file_name}")
        self.Speak(f"Screenshot saved")

    # ini untuk pindah mode ke teks mode, buat pindah ke voice mode lagi masih dikembangkan

    def SwitchCommandMode(self):
        self.Speak("Do you want to switch to text mode? Say 'yes' or 'no'.")
        response = self.Listen()

        if 'yes' in response.lower():
            self.command_mode = 'text'
            self.Speak('Switched to text mode. Please enter commands.')
        else:
            self.Speak('Switching to voice mode. Please give voice commands.')

    # fitur untuk mengetahui spek laptop
    def GetSystemSpecs(self):
        system_info = f"System Specifications:\n"
        system_info += f"Operating System: Windows {platform.release()}\n"
        system_info += f"Processor: {platform.processor()}\n"
        system_info += f"Architecture: {platform.machine()}\n"
        system_info += f"RAM: {self.GetRAMInfo()}\n"
        print(system_info)
        return system_info

    def GetRAMInfo(self):
        ram = psutil.virtual_memory()
        total_ram_gb = round(ram.total / (1024 ** 3), 2)
        available_ram_gb = round(ram.available / (1024 ** 3), 2)
        return f"{available_ram_gb} GB out of {total_ram_gb} GB available"

    # fitur baru

    # ini untuk mengatur suara jarvis
    def Speak(self, audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        engine.say(audio)
        engine.runAndWait()

    # ini buat efek suara wibu
    def PlayAudio(self, audio_file):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    # ini juga mata wibu
    def rinne_sharingan(self):
        """
        The function `rinne_sharingan` runs a Python script called `rinnegan.py` using the `os.system`
        function.
        """
        os.system("python assets/py/rinnegan.py")

    def ClearScreen(self):
        os_name = platform.system().lower()
        if 'windows' in os_name:
            os.system("cls")

    # Fitur untuk mencari informasi di Wikipedia
    def SearchWikipedia(self, query):
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            self.Speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            print("There are multiple options available. Please specify the exact topic.")
            self.Speak(
                "There are multiple options available. Please specify the exact topic.")
        except wikipedia.exceptions.PageError as e:
            print("The requested page does not exist on Wikipedia.")
            self.Speak("The requested page does not exist on Wikipedia.")
        except Exception as e:
            print("An error occurred while fetching information from Wikipedia.")
            self.Speak(
                "An error occurred while fetching information from Wikipedia.")

    # fitur untuk menampilkan mata wibu
    def sharingan(self):
        os.system("python assets/py/sharingan.py")

    # daftar fitur yang tersedia
    def GetCapabilities(self):
        capabilities = [
            "1. Opening applications like Chrome, Notepad, and Visual Studio Code",
            "2. Providing CPU and battery information",
            "3. Fetching weather information",
            "4. Generating QR code",
            "5. Opening Instagram and searching for users",
            "6. Playing games like Slither.io, Mini Royale, and Krunker",
            "7. Opening Microsoft Word, PowerPoint, and Excel",
            "8. Managing and displaying schedule",
            "9. Showing current date and time",
            "10. Playing song from youtube",
            "11. Opening my own website",
            "12. Drawing an amazing eyes",
            "13. Switch to text mode, and vice versa",
            "14. See the specifications of your device",
            "15. Take the screenshot",
            "16. Detect the jutsu",
            "17. Converting from docx to pdf file and vice versa",
            "18. Download the data of Corona's victims"
        ]

        capabilities_text = "This is the features that can you ask to me:\n"
        capabilities_text += "\n".join(capabilities)

        print(capabilities_text)
        jarvis.Speak(capabilities_text)
        print("For features number 5, 3, and 10, I suggest you instruct me to switch to text mode.")
        jarvis.Speak(
            "For features number 5, 3, and 10, I suggest you instruct me to switch to text mode.")
        print("To enable the text mode, just say 'text mode'")
        jarvis.Speak("To enable the text mode, just say 'text mode'")

    # kalo ga tau cara pakai nya ada di dalam fungsi ini
    def Help(self):
        help_text = """
        Available Commands:
        - Say, "Open Chrome": To Opens a new browser window in Google Chrome.
        - Say, "Open Notepad": to Opens Notepad application.
        - Say, "Open Visual Studio Code": to Opens Microsoft Visual Studio Code.
        - Say, "Open Word": to Opens Microsoft Word.
        - Say, "Open PowerPoint": to Opens Microsoft PowerPoint.
        - Say, "Open Excel": to Opens Microsoft Excel.
        - Say, "Open YouTube": to Opens YouTube in your default browser.
        - Say, "Play Song": to Plays a song on YouTube (Switch to text mode to use this feature).
        - Say, "Search for Instagram [username]": to Opens the Instagram profile of the specified username (Switch to text mode to use this feature).
        - Say, "Open My Instagram": to Opens your Instagram profile.
        - Say, "Play the Worm Game": to Opens the game "Slither.io" in your default browser.
        - Say, "Play Battle Royale Game": to Opens the game "Mini Royale" in your default browser.
        - Say, "Play the Shooting Game": to Opens the game "Krunker" in your default browser.
        - Say, "Make QR Code": to Generates a QR code with a link to your Instagram profile.
        - Say, "Weather": to Fetches the weather information for a specified city (Switch to text mode to enter the city name).
        - Say, "Get System": to Displays the system specifications of your device.
        - Say, "CPU Info": to Displays the current CPU usage.
        - Say, "Battery Info": to Displays the current battery status and level.
        - Say, "Set Schedule": Sets a schedule for a specific day and activity.
        - Say, "What Time Is It": Displays the current day, time, and scheduled activity (if any).
        - Say, "Sharingan": Activates the Sharingan animation.
        - Say, "Rinnegan": Activates the Rinnegan animation.
        - Say, "Open My Website": Opens your website.
        - Say, "Close Chrome": Closes all instances of Google Chrome.
        - Say, "Close Notepad": Closes all instances of Notepad.
        - Say, "Close Word": Closes all instances of Microsoft Word.
        - Say, "Close PowerPoint": Closes all instances of Microsoft PowerPoint.
        - Say, "Close Excel": Closes all instances of Microsoft Excel.
        - Say, "Close Edge": Closes all instances of Microsoft Edge.
        - Say, "Close All": Closes all instances of supported applications.
        - Say, "Go to Sleep Jarvis": Shuts down the assistant.
        - Say, "Who Are You": Provides information about Jarvis.
        - Say, "Thank You Jarvis": Shows appreciation to the assistant.
        - Say, "Text Mode": Switches to text mode for entering commands via text.
        - say, "Screenshot": To take the screenshot.
        - Say, "Voice Mode": (Not implemented yet) Switches back to voice mode for voice commands. (this feature is still on development)
        """
        print(help_text)
        jarvis.Speak(
            "Here are the available commands. Please say the command you want to use.")
        jarvis.Speak(help_text)

    # fitur informasi kondisi cpu saat ini
    def GetCpuInfo(self):
        cpu_percent = psutil.cpu_percent()
        cpu_info = f"Current CPU usage: {cpu_percent}%"
        print(cpu_info)
        return cpu_info

    # Fitur untuk memberikan joke
    def TellJoke(self):
        joke = pyjokes.get_joke()
        print(joke)
        self.Speak(joke)

    # fitur untuk informasi baterai saat ini
    def GetBatteryInfo(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        if plugged:
            status = "Plugged In"
        else:
            status = "Not Plugged In"
        battery_info = f"Battery status: {status}, {percent}%"
        print(battery_info)
        return battery_info

    # fitur informasi cuaca berdasarkan kota yang disebut
    def GetWeatherInfo(self):
        """
        The function `GetWeatherInfo` retrieves and displays the current weather information and a
        one-week forecast for a specified city using the OpenWeatherMap API.
        """
        jarvis.Speak(
            "Which city's weather information would you like to know?")
        city = jarvis.Listen()

        api_key = "983afcd78906be97b74610e31ac0dfaf"  # Ganti dengan API key Anda
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

        # Mengirim permintaan GET ke API cuaca
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  # Menggunakan satuan Celsius
        }

        response = requests.get(base_url, params=params)
        forecast_response = requests.get(forecast_url, params=params)

        weather_data = response.json()
        forecast_data = forecast_response.json()

        if weather_data["cod"] == 200 and forecast_data["cod"] == "200":
            # Menampilkan informasi cuaca saat ini
            current_weather = f"Current Weather in {city}:\n"
            current_weather += f"Weather Description: {weather_data['weather'][0]['description']}\n"
            current_weather += f"Temperature: {weather_data['main']['temp']}°C\n"
            current_weather += f"Humidity: {weather_data['main']['humidity']}%\n"
            current_weather += f"Wind Speed: {weather_data['wind']['speed']} m/s\n"

            print(current_weather)
            jarvis.Speak(current_weather)

            # Mendapatkan perkiraan cuaca satu minggu ke depan
            forecasts = forecast_data["list"]

            # Menyiapkan data untuk tabel
            table_data = []
            for forecast in forecasts:
                date = forecast["dt_txt"]
                temperature = forecast["main"]["temp"]
                weather_description = forecast["weather"][0]["description"]
                table_data.append(
                    [date, f"{temperature}°C", weather_description])

            # Menampilkan tabel informasi cuaca
            headers = ["Date", "Temperature", "Weather"]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

        else:
            error_message = "Unable to fetch weather information."
            print(error_message)
            jarvis.Speak(error_message)

    # Fitur set jadwal
    def SetSchedule(self):
        jarvis.Speak("Please provide the details for the schedule.")
        jarvis.Speak("What day is the schedule for?")
        day = jarvis.Listen()
        jarvis.Speak("What time is the schedule?")
        time = jarvis.Listen()
        jarvis.Speak("What is the schedule?")
        activity = jarvis.Listen()

        schedule[day.lower()] = {"time": time, "activity": activity}
        print(schedule[day.lower()])

        jarvis.Speak("Schedule has been set successfully.")

    # fitur untuk menanyakan waktu hari ini serta mengecek apakah hari ini ada jadwal atau tidak
    def GetSchedule(self):
        current_day = datetime.datetime.now().strftime("%A").lower()
        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_day in schedule:
            activity = schedule[current_day]["activity"]
            scheduled_time = schedule[current_day]["time"]

            print(f"Today is {current_day.capitalize()}.")
            print(f"The current time is {current_time}.")
            print(f"You have a scheduled activity at {scheduled_time}.")
            print(f"The activity is {activity}.")

            jarvis.Speak(f"Today is {current_day.capitalize()}.")
            jarvis.Speak(f"The time is {current_time}.")
            jarvis.Speak(f"You have a scheduled activity at {scheduled_time}.")
            jarvis.Speak(f"The activity is {activity}.")
        else:
            jarvis.Speak(f"Today is {current_day.capitalize()}.")
            jarvis.Speak(f"The current time is {current_time}.")
            jarvis.Speak("You don't have any scheduled activity for today.")
            print(f"Today is {current_day.capitalize()}.")
            print(f"The current time is {current_time}.")
            print("You don't have any scheduled activity for today.")


# The above code is creating an instance of a class called "PersonalBot" named "jarvis". It then
# prints a message and calls a method called "Speak" on the "jarvis" object to speak a message.
if __name__ == '__main__':
    jarvis = PersonalBot()
    print("Good day sir, I\'m Jarvis. say 'Specifications' to see what can i do for you")
    jarvis.Speak(
        'Good day sir, I\'m Jarvis. say "Specifications" to see what can i do for you')

    while True:
        if jarvis.command_mode == 'voice':
            result = jarvis.Listen()
        elif jarvis.command_mode == 'text':
            result = input('Enter command: ')
        # result = jarvis.Listen()
        print("Your order is", result)
        # jarvis.ClearScreen()

        # Basic Commands
        if 'jarvis' in result.lower():
            jarvis.Speak('Yes, sir?')
            jarvis.ClearScreen()

        if 'take a screenshot' in result.lower() or 'screenshot' in result.lower() or 'ss' in result.lower():
            jarvis.TakeScreenshot()

        # perintah menampilkan mata wibu
        if 'rinnegan' in result.lower():
            # jarvis.Speak('Drawing Rinne Sharingan')
            jarvis.rinne_sharingan()

        # liat spesifikasi laptop kamu
        if 'get system' in result.lower():
            system_specs = jarvis.GetSystemSpecs()
            jarvis.Speak(system_specs)

        # lu juga harus tau terimakasih, udah dibantuin juga
        if 'thank you jarvis' in result.lower():
            jarvis.Speak('No problem, sir')

        # perintah pengenalan diri
        if 'who are you' in result.lower():
            print(
                "I am Jarvis, version 1.0. I am an AI assistant developed by Zalzdarkent on July 31, 2023")
            jarvis.Speak(
                'I am Jarvis, version 1.0. I am an AI assistant developed by Zalzdarkent on July 31, 2023')

        # buat buka browser, kalo kalian pakai duck duck go atau yang lain bisa diganti
        if 'open chrome' in result.lower():
            jarvis.Speak('Opening a new browser')
            os.system("start chrome")

        # fitur baru

        # perintah informasi cuaca
        if 'weather' in result.lower():
            jarvis.GetWeatherInfo()

        if 'clear' in result.lower() or 'cls' in result.lower():
            jarvis.ClearScreen()

        # ini buat ganti ke perintah teks
        if 'text mode' in result.lower():
            jarvis.SwitchCommandMode()

        # nah ini buata ngegambar si RDJ
        if 'iron man' in result.lower():
            obj = lib.rdj()
            obj.draw()

        # buat buka notepad
        if 'open notepad' in result.lower():
            os.system("start notepad")

        # buat liat daftar fitur
        if 'specifications' in result.lower():
            jarvis.GetCapabilities()

        # if jarvis.command_mode == 'text':
        #     jarvis.SwitchVoiceMode()

        if 'search on wikipedia' in result.lower() or 'wikipedia' in result.lower():
            jarvis.Speak('What do you want to search for on Wikipedia?')
            search_query = jarvis.Listen()
            jarvis.SearchWikipedia(search_query)

        if 'tell a joke' in result.lower():
            jarvis.TellJoke()

        # buat  buka vs code
        if 'open visual studio code' in result.lower():
            jarvis.Speak("Opening Visual Studio Code")
            os.system("start code")

        # nah ini kalo kalian punya website sendiri bisa diganti aja file location nya
        if 'open my website' in result.lower():
            jarvis.Speak('Opening your website')
            website_path = 'file:///C:/xampp/htdocs/aruna/index.html'
            webbrowser.open(website_path, new=1)

        # ini juga mata wibu
        if 'sharingan' in result.lower():
            os.system("start assets/web/index.html")
            jarvis.PlayAudio("./assets/audio/Sharingan.mp3")

        if 'convert word to pdf' in result.lower():
            os.system("py assets/py/doc2pdf.py")

        if 'convert pdf to word' in result.lower():
            os.system("py assets/py/pdf2word.py")

        if 'covid victims' in result.lower():
            os.system("py assets/py/data_covid.py")

        if 'jutsu' in result.lower() or 'ninjutsu' in result.lower() or 'hand sign' in result.lower():
            os.system("py NINJUTSU/Ninjutsu_demo.py")

        # Help command
        if 'help' in result.lower():
            jarvis.Help()

        # info cpu
        if 'cpu info' in result.lower():
            cpu_info = jarvis.GetCpuInfo()
            jarvis.Speak(cpu_info)

        # info baterai
        if 'battery info' in result.lower():
            battery_info = jarvis.GetBatteryInfo()
            jarvis.Speak(battery_info)

        # kalo mau udahan, bilang aja jangan ngilang apalagi selingkuh
        if 'go to sleep jarvis' in result.lower():
            jarvis.Speak('Shutting down')
            break

        # generate qr code
        if 'make qr code' in result.lower():
            jarvis.Speak('Making your QR code')
            makeQRCode(qr_code_link)

        # buat buka yt
        if 'open youtube' in result.lower():
            jarvis.Speak('Opening YouTube')
            webbrowser.open("http://youtube.com", new=1)

        # buat dengerin lagu di yt
        if 'play song' in result.lower():
            jarvis.Speak('What song would you like me to play?')
            song = jarvis.Listen()
            jarvis.Speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        # Khusus Instagram methods
        # Untuk mencari Instagram, katakan "search for Instagram username" (pengenalan suara bisa sulit, jadi disarankan pindah ke mode teks)
        if 'search for instagram' in result.lower():
            result = result.replace(" ", "")
            username = result[18:]
            insta_link = "http://instagram.com/{}".format(username)
            webbrowser.open(insta_link, new=1)
            jarvis.Speak(f"Searching for {username}")

        if 'open my instagram' in result.lower():
            jarvis.Speak('Opening your Instagram')
            insta_link = "http://instagram.com/{}".format(ig_username)
            webbrowser.open(insta_link, new=1)

        # Play random games (disarankan untuk spek laptop di atas ryzen 3, dan intel I3 gen 11)
        if 'play the worm game' in result.lower():
            jarvis.Speak('Opening Slither.io')
            webbrowser.open("http://slither.io", new=1)

        if 'play battle royale game' in result.lower():
            jarvis.Speak('Opening Mini Royale')
            webbrowser.open("http://miniroyale2.io", new=1)

        if 'play the shooting game' in result.lower():
            webbrowser.open("http://krunker.io", new=1)

        # Open Microsoft stuff
        if 'open word' in result.lower():
            jarvis.Speak('Opening Microsoft Word')
            os.system("start word")

        if 'open powerpoint' in result.lower():
            jarvis.Speak('Opening Microsoft PowerPoint')
            os.system("start powerpnt")

        if 'open excel' in result.lower():
            jarvis.Speak('Opening Microsoft Excel')
            os.system("start excel")

        # menutup chrome
        if 'close chrome' in result.lower():
            if 'chrome.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the browser')
                os.system("taskkill /im chrome.exe /f")
            else:
                jarvis.Speak('Chrome is not currently open')

        # menutup notepad
        if 'close notepad' in result.lower():
            if 'notepad.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the notepad')
                os.system("taskkill /im notepad.exe /f")
            else:
                jarvis.Speak('notepad is not currently open')

        # menutup ms word
        if 'close word' in result.lower():
            if 'winword.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the microsoft word')
                os.system("taskkill /im winword.exe /f")
            else:
                jarvis.Speak('microsoft word is not currently open')

        # menutup ppt
        if 'close powerpoint' in result.lower():
            if 'powerpnt.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the microsoft power point')
                os.system("taskkill /im powerpnt.exe /f")
            else:
                jarvis.Speak('microsoft power point is not currently open')

        # menutup excel
        if 'close excel' in result.lower():
            if 'excel.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the microsoft excel')
                os.system("taskkill /im excel.exe /f")
            else:
                jarvis.Speak('microsoft excel is not currently open')

        # menutup vs code
        if 'close visual studio code' in result.lower():
            if 'code.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the visual studio code')
                os.system("taskkill /im code.exe /f")
            else:
                jarvis.Speak('visual studio code is not currently open')

        # menu tutup ms edge
        if 'close edge' in result.lower():
            if 'msedge.exe' in (p.name() for p in psutil.process_iter()):
                jarvis.Speak('Closing the microsoft edge')
                os.system("taskkill /im msedge.exe /f")
            else:
                jarvis.Speak('microsoft edge is not currently open')

        # menutup semua aplikasi
        if 'close all' in result.lower():
            closed_apps = []
            if 'chrome.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im chrome.exe /f")
                closed_apps.append('Chrome')
            # Add similar checks and close commands for other applications...
            if 'notepad.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im notepad.exe /f")
                closed_apps.append('notepad')
            if 'winword.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im winword.exe /f")
                closed_apps.append('winword')
            if 'powerpnt.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im powerpnt.exe /f")
                closed_apps.append('powerpoint')
            if 'excel.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im excel.exe /f")
                closed_apps.append('excel')
            if 'msedge.exe' in (p.name() for p in psutil.process_iter()):
                os.system("taskkill /im msedge.exe /f")
                closed_apps.append('edge')

            if closed_apps:
                jarvis.Speak(f"Closing {', '.join(closed_apps)}")
            else:
                jarvis.Speak('No applications were open')

        # buat atur jadwal (sebenernya belum beres)
        if 'set schedule' in result.lower():
            jarvis.SetSchedule()

        # buat menanyakan waktu hari ini
        if 'what time is it' in result.lower():
            jarvis.GetSchedule()
