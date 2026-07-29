# ==============================================================================
# ALEXANDER - AUTOMOTIVE ENGINEERING - GERMAN B2B COMPLIANCE
# REPOSITORY: Alexander-Automotive-Data-Engineering-Enterprise-Suite
# TAG_01: PYTHON AUTOMOTIVE AUTOMATION | MOTOR: fault_shield_loop.py
# ==============================================================================

def fault_shield_loop():
    # #1. Allocation: Raw payload stream with structured B2B automotive lines
    rawPayloadBatch = "BMW*MUNICH*98420-SECURE|AUDI*INGOLSTADT*E_FAIL|BMW*LEIPZIG*45210-SECURE"
    
    # #2. Lesson 1 (Split): Breaking the heavy batch into a clean workable list
    cargoUnitsList = rawPayloadBatch.split("|")
    
    # #3. Lesson 5 (Stream): continuous processing via while loop container
    loopCounter = 0
    totalItems = len(cargoUnitsList)
    
    print("\n--- BMW GERMAN FAULT SHIELD & INBOUND LOOP MONITOR ---", sep="-")
    
    while loopCounter < totalItems:
        # #6. Lesson 6 (Shield): Defensive execution block using try/except structure
        try:
            currentCargo = cargoUnitsList[loopCounter]
            
            # Parsing the internal components of the specific chassi
            chassiParts = currentCargo.split("*")
            brandToken = chassiParts[0]
            factoryToken = chassiParts[1]
            statusToken = chassiParts[2]
            
            # #4. Lesson 3 & 4 (Condition & Registry): If/Elif/And business logic
            # Checking if the cargo belongs to BMW AND contains a secure contract code
            if brandToken == "BMW" and "SECURE" in statusToken:
                # #2. Lesson 2 (Join): Re-linking route tags into clean industrial arrows
                purifiedRoute = " -> ".join([brandToken, factoryToken, "APPROVED"])
                print("[SHIELD - LOG]", "Cargo processed successfully:", purifiedRoute, sep=" -> ")
                
            elif brandToken == "AUDI" or "E_FAIL" in statusToken:
                # #5. Lesson 5 (Disjuntor Break): Force-stopping the loop if corruption is detected
                print("[SHIELD - WARNING]", "CRITICAL CORRUPTION DETECTED IN STATUS:", statusToken, sep=" -> ")
                print("[SHIELD - SECURITY]", "Activating break disjuntor to isolate memory.", sep=" -> ")
                break
                
        except IndexError as systemError:
            # Shield trigger to prevent system crash if layout index fails
            print("[SHIELD - ERROR]", "Payload breakdown failure:", str(systemError), sep=" -> ")
            break
            
        loopCounter += 1

    print("========================================", "PROCESS_COMPLETE", sep=" | ", end="\n")

# Activating the compliance fault shield loop for Wednesday sprint closure
fault_shield_loop()

# ==============================================================================
# Process exited - Return Code: 0 (The King Lion Provedor Master Lacre)
# ==============================================================================
