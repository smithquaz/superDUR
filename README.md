# superDUR
IEEE SSCI Hackathon 2022 Champions

## Members
1. Toh Yue Zhen
2. Laiu Yan Kang, Asher
3. Tan Kai Xuan
4. Natalie Claire Ng Shu-En

## Relevant Skills to Learn
1. sql-alchemy 
    * load data from csv into this sql table (create + load)
    * we can then extract information from this table to feed into our AI
2. modus ponens inference engine 
    * rules that help simplify logical symbols
    * main AI
    * will need a lot of reading & githubbing :)
3. flask / any webapp framework, UI design
    * take user input, output the result to the user
    * look pretty and nice to use for the user

## Flow of Application

### Phase 1: Pre-Loading
1. Define and load sql table titled: Medical Conditions (table of all the drugs that cannot be prescribed based on medical conditions)
2. Define and load sql table titled: DDIs (table of all known drug-drug interactions - may have to split into 2)

### Phase 2a: User Input (account information)
1. User provides (1) current drugs, (2) medical conditions and (3) allergies to the system
2. Make a sql query to extract from table Medical Conditions: all the drugs that cannot be prescribed based on (2) medical conditions
3. (1) current drugs, result of extraction in 2 and (3) allergies are added directly into the KB (using AND object)
4. Flatten the values of the KB into a dictionary (just text words for easy matches)

### Phase 2b: User Input (all DDIs)
1. Make a sql query to extract from table DDIs: all known drug-drug interactions of this drug
2. Result of extraction is added into KB one by one for all matching statements (using AND object)

### Phase 3a: AI Resolution (number of matches) ; O(n) * O(m) * O(p + m)
1. Repeat for all DDIs extracted: O(n)
    * Repeat for number of items in KB: Check if there is a match between the KB item and the DDI 
    * Break when list finished traversing or all KB item is found
    * O(m) * O(p + m) - note: python 3.10 only
2. Remove all DDIs with 0 matches (not relevant)
3. Sort the DDIs in terms of number of matches (use Merge Sort) 

### Phase 3b: AI Resolution (inference engine)
1. Repeat for all DDIs, pass them one by one into the inference engine
2. If any contradiction is found, output false
3. If all managed to pass succesfully, output true

### Phase 4: Output Display
1. Output the result
2. Design the page
