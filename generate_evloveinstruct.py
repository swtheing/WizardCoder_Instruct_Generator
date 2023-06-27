import json
import time
from gpt4_azure import completion
prompt = "Please increase the difficulty of the given programming test question a bit. You can increase the difficulty using, but not limited to, the following methods: "
instructs = open("evole_instruct.txt", "r")
codes = json.load(open("code_alpaca_20k.json", "r"))
new_codes = []
for code in codes:
    cur_prompt = prompt
    for i, instruct in enumerate(instructs):
        cur_prompt += str(i+1) + ". " + instruct.strip() + "; "
    problem = code["instruction"] + " input: " +  code["input"] + ";"
    cur_prompt += " question: " + problem
    instruct = completion(cur_prompt)
    output = completion(instruct)
    new_codes.append({"instruct": instruct, "output": output})
    break

fp = open("new_code_demo.json", "w")
json.dump(new_codes, fp)        

    
    
