# Import necessary libraries
import speech_recognition as aa  # For recognizing speech
import pyttsx3  # For text-to-speech conversion
import pywhatkit  # For automating tasks like playing YouTube videos
import datetime  # For getting the current date and time
import wikipedia  # For fetching information from Wikipedia
import time  # For handling time-related functions

# Create a speech recognizer instance
listener = aa.Recognizer()
# Initialize the text-to-speech engine
machine = pyttsx3.init()

# Function to convert text to speech
def talk(text):
    machine.say(text)  # Queue the text to be spoken
    machine.runAndWait()  # Ensure the speech is processed
    
# Function to listen for user input
def input_instruction():
    instruction = ""  # Initialize instruction to an empty string
    
    try:
        # Use the microphone to listen for speech
        with aa.Microphone() as origin:
            print("Listening...")  # Indicate that the assistant is listening
            speech = listener.listen(origin)  # Capture the audio from the microphone
            # Recognize the speech using Google's speech recognition
            instruction = listener.recognize_google(speech)  
            instruction = instruction.lower()  # Convert the recognized text to lowercase
            # Check if the assistant's name is mentioned in the instruction
            if "jarvis" in instruction:
                print(instruction)  # Print the recognized instruction
                
    except Exception as e:
        print("Error:", e)  # Print any errors for debugging
    return instruction  # Return the recognized instruction

# Function to handle commands and interactions
def play_Jarvis():
    last_input_time = time.time()  # Track the last time valid input was received
    timeout_duration = 10  # Set timeout duration in seconds
    
    while True:  # Loop to keep the assistant running
        instruction = input_instruction()  # Get user input
        # Check if the instruction is empty (indicating no response)
        if not instruction:
            # If no input is received and the timeout duration has passed
            if time.time() - last_input_time > timeout_duration:
                talk('I think you are busy. See you later!.')  # Say bye
                talk('Have a great day')
                break  # Exit the loop to stop the assistant
            else:
                continue  # Wait for the next input
        last_input_time = time.time()  # Update the last input time
        print(instruction)  # Print the recognized instruction
        
        # Check if the instruction contains the word "play"
        if "play" in instruction:
            # Clean the instruction to get the song name
            instruction = instruction.replace('jarvis', "").replace('play', "").strip()
            talk("Playing " + instruction)  # Inform the user that the song is being played
            pywhatkit.playonyt(instruction)  # Play the song on YouTube
            
        # Check if the instruction asks for the current time
        elif 'time' in instruction:
            time_now = datetime.datetime.now().strftime('%I:%M %p')  # Get the current time
            talk('Current time is ' + time_now)  # Speak the current time
            
        # Check if the instruction asks for the current date
        elif 'date' in instruction:
            date_now = datetime.datetime.now().strftime('%d/%m/%Y')  # Get the current date
            talk("Today's date is " + date_now)  # Speak the current date
            
        # Check if the user asks how the assistant is doing
        elif 'how are you' in instruction:
            talk('I am fine, how about you?')  # Respond to the user
            
        # Check if the user asks for the assistant's name
        elif 'what is your name' in instruction:
            talk('I am Jarvis, what can I do for you?')  # Introduce the assistant
            
        # Check if the user asks about a person
        elif 'who is' in instruction:
            human = instruction.replace('who is', "").strip()  # Extract the name from the instruction
            info = wikipedia.summary(human, 1)  # Get a summary from Wikipedia
            print(info)  # Print the information
            talk(info)  # Speak the information
        
        # Check if the user says "stop"
        elif 'stop' in instruction:
            talk('byee! Have a great day!')  # Say bye
            talk('see you next time')
            break  # Exit the loop to stop the assistant
        
        # If the instruction does not match any known commands
        else:
            talk('Please can you repeat that?')  # Ask the user to repeat
# Start the assistant
play_Jarvis()