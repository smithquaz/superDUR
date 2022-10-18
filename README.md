# superDUR
IEEE SSCI Hackathon 2022 Champions

## Members
1. Toh Yue Zhen
2. Laiu Yan Kang, Asher
3. Tan Kai Xuan
4. Natalie Claire Ng Shu-En

## Flow of Application

### User Interface (undecided)
* Command Line? 
* csv? 
* GUI? 

### Initial KB Feed
1. Define an empty KB (blank sentence object)
2. Drugs: 
    * Define it as a SYMBOL object
    * Join all these symbols together using the AND object
    * Add these AND object into the empty KB
3. Medical Conditions / Allergies: 
    * Define an sql table that is pre-loaded with diseases and the relevant drugs that they cannot take
    * SQL query search database for drugs that cannot be taken for this condition 
    * Define these drugs using the NOT object and add them into the KB defined in 2.2