from APIgroq import Agent
from APIgemini import Gemini

GroqAgent = Agent()

reponse = GroqAgent.ask("Bonjour, ca va ?")

print(reponse)



GeminiAgent = Gemini()

GeminiAgent.audio(reponse)