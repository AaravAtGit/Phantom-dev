import os
from dotenv import load_dotenv
from phantom import Phantom



load_dotenv()
THETA_ENDPOINT = os.environ["theta_endpoint"]
THETA_API_KEY = os.environ["theta_key"]
ELEVENLABS_API_KEY = os.environ["elevenlabs_key"]


phantom = Phantom(THETA_ENDPOINT,ELEVENLABS_API_KEY, THETA_API_KEY)




code = phantom.copy_code()
phantom.Explain_code(code)
phantom.play_code()