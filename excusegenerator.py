#random module
#list[item/object list]
#string concatination +
#appendding.append()
#join .join()
#functions 
#for loop


import random


#list of components for excuses
excuse_starters =[
    "I'm sorry but",
    "unfortunately",
    "i regrete to inform you that",
    "due to unforseen circumstances"
    
    ]
excuse_reasons =[
    "my dog ate my home work",
    "my arlarm didn't go off",
    "there was heavy traffice on my way",
    "i had a sudden family emergency",
    "my computer crashed and i lost my work"
    ]
excuse_endings =[
    "so i couldn't complete the work on time",
    "which lead to my delay",
    "resulting to my inability to meet the deadline",
    "causing me to miss out on the important event"
    ]
    
def generate_excuse():
    excuse_parts = []
    excuse_parts.append(random.choice(excuse_starters))
    excuse_parts.append(random.choice(excuse_reasons))
    excuse_parts.append(random.choice(excuse_endings))
    return " ".join(excuse_parts)
   
    #Generate the random excuses
    #random_start = random.choice(excuse_starters)
    #randome_reason = random.choice(excuse_reasons)
    #randome_ending = random.choice(excuse_endings)

    #concatinate the parts the parts to print the final excuse_endings
    final_excuse = random_start + " " + randome_reason + " " + randome_ending
    return final_excuse

#print the excuses
#print("Generating Excuses: ")
#print(final_excuse)


#user input customization
num_excuses = int(input ("Enter the number of excuses to generate: "))

#Generate excuses in bulk
print("Generate Excuses: ")
for _ in range(num_excuses):
    excuse = generate_excuse(); 
    print(excuse)
    print("- " * 40)
    
    
    
    
    
    