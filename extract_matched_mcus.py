from rapidfuzz import process, fuzz
import json

# Sample database of microcontroller numbers
mcu_database = [
    "STM32F103C8T6",
    "ATmega328P",
    "ESP32-WROOM-32",
    "PIC16F877A",
    "MSP430G2553",
    "STM32F407VGT6",
    "Arduino Uno R3",
    "Raspberry Pi Pico",
    "nRF52832",
    "TM4C123GH6PM"
]

# Sample text to search through
sample_text = """
I'm working on a project using the STM32F407VGT6 microcontroller. 
It's more powerful than the STM32F103C8T6 I used in my last project. 
I'm also considering using an ESP32-WROOM-32 for WiFi capabilities. 
My friend suggested I look into the MSP430G2553 for low power applications.
"""
#Get the sub selection of the microcontroller data 
reconstruct_subselect = {} 
def extract_mcu_mentions(text, mcu_list, threshold=70):
    # Split the text into words
    words = text.split()
    
    # Function to check if a word contains any MCU number
    def contains_mcu(word):
        matches = process.extract(word, mcu_list, scorer=fuzz.partial_ratio, limit=len(mcu_list))
        #print(matches)
        return [match for match in matches if match[1] >= threshold]
       
    # Extract words that contain MCU numbers
    mcu_mentions = []
    
    for word in words:
        matches = contains_mcu(word)
        if matches:
            mcu_mentions.append({
               word: matches
            })
    
    return mcu_mentions

# Extract MCU mentions
results = extract_mcu_mentions(sample_text, mcu_database)
#peint(results)
# Print results
mcus_maxrange = json.dumps(results, indent=2)
#print(json.dumps(results, indent=2))
mcusmaxdat = json.loads(mcus_maxrange)
#print(mcusmaxdat) 
for g in mcusmaxdat:
          #print(g)
          for ct in list(g):
                  #print(g[ct])  
                  sub_list =g[ct] # Get sub list 
                  for stx in sub_list:
                          print(stx) 
                          reconstruct_subselect[stx[0]] = stx[1]
print("Reconstruct sub select mcus: ",reconstruct_subselect)
