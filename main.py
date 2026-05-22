import os
import time
from google import genai
from google.genai import types
import config

def generate_response(prompt,temperature=0.5):
    try:
        client = genai.Client(api_key ='AIzaSyBTM5aD8Ngvhg_j0YonkJACURE8Hdb3iWY')

        content =[
            types.Content(
                role = 'user',
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]

        generate_content_config = types.GenerateContentConfig(temperature=temperature,response_mime_type='text/plain',)

        response = client.models.generate_content(model='gemini-2.0-flash',contents=content,config = generate_content_config,)

        return response.text
    except Exception as e:
        return f"Error generating response :{str(e)}"


def temperature_prompt_activity():
    print('='*80)
    print("ADVANCED PROMPT ENG. : TEMP AND INSTRUCTION BASED PROMPTS")
    print('='*80)
    print('\nIn this Activity, we will explore')
    print('1. How temo affects AI creativity')
    print('2. How instruction based prompts can control AI outputs')

    print('\n','-'*40)
    print('Part I : Temperature Exploration')
    print('-'*40)

    base_prompt = input('\n Enter a creative prompt(e.g. Write a short story about a robot learning to paint):')

    print('\n Generating responses with different temperature setting..')
    print('\n Low Temp(0.1)-More Determnistic')
    low_temp_response = generate_response(base_prompt,temperature=0.1)
    print(low_temp_response)
    time.sleep(1)
    
    print('\n Med Temp(0.5)-Balanced')
    med_temp_response = generate_response(base_prompt,temperature=0.5)
    print(med_temp_response)
    time.sleep(1)

    print('\n High Temp(0.1)-More Random/Creative')
    high_temp_response = generate_response(base_prompt,temperature=0.9)
    print(high_temp_response)
    
    print('\n','-'*40)
    print('Part II Instruction based prompts')
    print('-'*40)

    print('\n Now , Lets explore how specific instructions change outputs')

    topic = input("\nChoose a topic(eg climate change):")

    instructions =[
        f'Summarize the key facts about {topic} in 3-4 sentences',
        f"Exlain {topic} as if I am 10 yrs",
        f"Write a pro con list about {topic}",
        f"Create a fictional  news headline from the year 2050 about {topic}"

    ] 

    for i,instructions in enumerate(instructions,1):
        print(f"\n --- Instruction{i}:{instructions}---")
        response = generate_response(instructions,temperature=0.7)
        print(response)
        time.sleep(1)


    print("\n"+'-'*40)
    print('Part III Creating own Instruction based prompts')
    print('-'*40)

    print("\n Now it is your turn , Create an instruction based prompt")

    custom_instruction= input("Enter your instruction based prompt:")
    try:
        custom_temp = float(input("Select a temperature:"))
        if custom_temp<0.1 or custom_temp>1.0 :
            print('Invalid Temperature, default 0.7')
            custom_temp = 0.7
    except ValueError:
        print('Invalid Inp..')
        custom_temp=0.7

    print(f" Your custom prompt with temp as {custom_temp}")
    custom_response = generate_response(custom_instruction,temperature=custom_temp) 
    print(custom_response)

    # Reflecion Ques
    print('\n'+'-'*40)
    print('REFLECTION QUESTIONS')
    print('\n'+'-'*40) 

    print('1. How did chnaging the temperature affect the creativity and variety in the AIs responses?') 
    print('2. Which instruction based prompt produced the most useful or intresting result?')
    print('3. How might you combine specific instructions and temperature settings in real applications?') 
    print('4. What patterns did you notice in how the AI responds to different types of instructions?')

    # Challenge Activity
    print('\n'+'-'*40)
    print('CHALLENGE ACTIVITY')
    print('\n'+'-'*40)      

    print('Try creating a chain of prompts where:') 
    print('1. First, ask the AI to generate content about a topic')
    print('2. The use an instruction based prompt to modify or build upon that content')
    print('3. Experiment with different temperature settings at each step ')
    print('\nFor Example : Generate a story -- Instruct AI to rewrite it in a specific style -- Ask AI to create a sequel')

def generate_streaming_response(prompt,temperature=0.5):
    try:
        client = genai.Client(api_key =config.Gemini_api_key)

        content =[
            types.Content(
                role = 'user',
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]

        generate_content_config = types.GenerateContentConfig(temperature=temperature,response_mime_type='text/plain',)
        print('\n Streaming response (press Ctrl+C to stop):')
        for chunk in client.model.generate_content_stream(model='gemini-2.0-flash',contents=content,config=generate_content_config,):
            print(chunk.text,end='')
        print('\n')
    except Exception as e :
        print(f'\n Error Generating Streaming response: {str(e)}')

    

if __name__=='__main__':

    temperature_prompt_activity()

print('\n'+'-'*40)
print('BONUS: Streaming Response')
print('\n'+'-'*40) 

print('Would you like to see a streaming response? (y/n)')
choice = input('>').lower().strip()
if choice=='y':
    prompt = input('\nEnter a prompt for streaming response:')
    generate_streaming_response(prompt,temperature=0.7)
