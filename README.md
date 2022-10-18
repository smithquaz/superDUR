# superDUR
IEEE SSCI Hackathon 2022 Champions

## Flow of Application
1. User Interface (undecided)
    1.1 Command Line? 
    1.2 csv? 
    1.3 GUI? 

2. Initial KB Feed
    2.1 Define an empty KB (blank sentence object)
    2.2 Drugs: 
        2.2.1 Define it as a SYMBOL object
        2.2.2 Join all these symbols together using the AND object
        2.2.3 Add these AND object into the empty KB
    2.3 Medical Conditions / Allergies: 
        2.3.1 Define an sql table that is pre-loaded with diseases and the relevant drugs that they cannot take
        2.3.2 SQL query search database for drugs that cannot be taken for this condition 
        2.3.3 Define these drugs using the NOT object and add them into the KB defined in 2.2