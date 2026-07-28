def aduana_sanitization_index():
    
    rawCargoPayload = "   BMW-MUNICH-2026-ALEXANDER-98420-SECURE   "
    rawQuantityText = "250"
    rawSerialLetters = "BMW"
    
    
    cleanPayload = rawCargoPayload.strip()
    
    
    
    firstHyphenPos = cleanPayload.find("-")     
    
    
    munichWordIndex = cleanPayload.index("MUNICH") 
    
    
    isQuantityValid = rawQuantityText.isdigit()  
    isSerialValid = rawSerialLetters.isalpha()   
    
    
    print("\n--- BMW GERMAN ADUANA INTERNATION_AL REPOSITORY ---", sep="-")
    print("[PAYLOAD]", "Purified Cargo Chassi:", cleanPayload, sep=" -> ")
    print("[LOCATOR]", "First divisor '-' position index:", firstHyphenPos, sep=" -> ")
    print("[PRECISION]", "Real starting index of MUNICH:", munichWordIndex, sep=" -> ")
    print("[DIGITS]", "Does the cargo quantity contain digits only? (bool):", isQuantityValid, sep=" -> ")
    print("[SERIAL]", "Does the cargo serial contain letters only? (bool):", isSerialValid, sep=" -> ")
    print("========================================", "PROCESS_COMPLETE", sep=" | ", end="\n")


aduana_sanitization_index()



