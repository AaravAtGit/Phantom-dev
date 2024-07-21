import os
from dotenv import load_dotenv
import requests
import openai
import pyautogui
import cv2
import numpy as np
import time
import pyperclip
import json
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from playsound import playsound
import pyttsx3

# Using elevenLabs for fast response



class Phantom:
    def __init__(self, endpoint, voice_apikey, api_key=None):
        self.endpoint = endpoint
        self.voice_apikey = voice_apikey
        self.api_key = api_key
        self.engine = pyttsx3.init()

        self.client = ElevenLabs(api_key=voice_apikey)


    def copy_code(self):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        template = cv2.imread("images/Line-4.png", 0)
        result = cv2.matchTemplate(cv2.cvtColor(
            screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        pyautogui.moveTo(max_loc[0] + 40, max_loc[1])
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        pyautogui.click(max_loc[0] + 40, max_loc[1])
        global code
        code = pyperclip.paste()
        return code


    def Phantom_dev_Interact(self, current_line, next_line):
        jumps = next_line - current_line

        if jumps > 0:
            for i in range(jumps):
                pyautogui.press("down")
                time.sleep(np.random.uniform(0.05, 0.15))

        elif jumps < 0:
            for i in range(abs(jumps)):
                pyautogui.press("up")
                time.sleep(np.random.uniform(0.05, 0.15))

        time.sleep(np.random.uniform(0.5, 1.5))


    def add_numbers_to_code(self, code):
        lines = code.split('\n')
        numbered_lines = []
        for i, line in enumerate(lines, start=1):
            numbered_lines.append(f"{i:2d} {line}")
        numbered_string = '\n'.join(numbered_lines)
        print(numbered_string)
        return numbered_string


    def Explain_code(self, code, file="script.json"):
        client = openai.Client(base_url=self.endpoint,
            api_key=self.api_key
        )
        code = self.add_numbers_to_code(code)
        response = client.chat.completions.create(messages=[
            {"role": "system", "content": 'You are an api of a smart developer.The user will input code. and your output should be in json with explanation of the code per line. example: {"line 1": "explaination of line 1", "line 4": "explaination of line 4"}. Only give a brief description of the important lines. the speech should be as human sounding as possible Incorporate natural pauses, "um"s and "ah"s in speech'},
            {"role": "user", "content": code},
            ], model="mistral-large-2402")

        script = response.choices[0].message.content

        with open(file, "w") as f:
            f.write(script)



    def play_code(self, file="script.json"):
        with open(file) as f:
            data = json.load(f)

        current_line = 4
        for line in data:
            audio = self.client.generate(text=data[line], voice="Nicole", model="eleven_monolingual_v1")
            save(audio, f"sounds/{line}.mp3")

        for line in data:
            next_line = int(line.split('-')[0])
            self.Phantom_dev_Interact(current_line, next_line)
            playsound(f"sounds/{line}.mp3")

            current_line = next_line
        print(data)

    
    def play_code_fast(self, file="script.json"):
        with open(file) as f:
            data = json.load(f)

        current_line = 4
        for line in data:
            og_line = line
            line = line.replace("line", "").strip()
            next_line = int(line.split('-')[0])
            self.Phantom_dev_Interact(current_line, next_line)
            self.engine.say(data[og_line])
            self.engine.runAndWait()
            

            current_line = next_line
        print(data)






