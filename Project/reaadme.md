# Criterion A: Planning
## Problem Definition
My client is an old local bike rental shop owner in Karuizawa. As he puts his bikes in front of his store, he needs a way to lock them to prevent possible theft. To do so, he simply uses a bike lock for each bike. Additionally, to prevent every bike lock being compromised at the same time, he uses a different passcode for every single bike. 

Lately, he has complained that he cannot remember all the passcodes anymore, as the number of bikes in his shops ranges into the hundreds, and he feels like he is getting old. He tried to write all the passcodes in a booklet, but soon become paranoid of employees seeing every passcode of every bike, which he believes to be the starting point for a bike heist. Then he tried to use a simple cypher on the passcodes and write them down, but it also posed a challenge for him: the cypher took too long to crack, sometimes he makes a mistake that makes him repeat the entire process again; all of these steps, he said, were too mentally taxing and streessful for him to repeat multiple times during the day.

## Proposed Solution
To make the process easier for my client, I propose a hidden system that allows my client to manage the passcodes for his bikes.

This system will be embedded and disguised as a simple software to search up the rental price of a bicycle through inputting the bike’s number. However, when the user inputs the right Access Code, the program will change mode and act as a passcode manager that allows my client to perform CRUD (Create, Read, Update, and Delete) operations on the passcodes. Such systems ensure that any access to the passcode manager needs to be deliberate, as any other input aside from number usually returns an error.

Furthermore, in compliance with the client's request, the passcode for the bikes would be encrypted. As my client is old, once inside the passcode manager, the method should allow the user to enter typo of the passcode and still be able to decrypt the bike's passcode. This feature is further justified by the fact that the user needs to already enter the correct Access Code to enter the program. Nevertheless, there should be an additional security feature to offset the slight security decrease, such as having wrong keys returning plausible but wrong results (to combat brute force attacks).

Additionally, it would also have a function to change the Access Code itself, as there exists a possibility that my client accidentally compromises his passcode (e.g. due to him writing it). This would allow him to swiftly change the access to the Passcode Manager as well as the encryption of the bike passcode data, preventing further possible bike passcode compromise.

## Success Criteria
Default Program:

1. The software can receive an input for a bike number and displays that bike's rental rate
2. Find available bike information
3. Clear console
4. The software can output the number of available bike rental price information
5. The software can handle typical errors (e.g. entering a bike number that does not exist, entering a string instead of a number, entering floats instead of integers) and give appropriate feedback
6. If the user enters the secret access code, determined by the user, the program will change modes and acts as a password manager.
   
Password Manager: 

6. View bike's passcode:
      * User can input the number of one or multiple bikes to check each bike's passcode
      * The user must enter the access code (or words that are potential typos of the access code) to view the bike passcode
7. Update a bike's passcode
8. Create a new bike's passcode
9. Delete a preexising bike's passcode
10. Change the access code while also making the passcode data viewable with the new access code
11. Return back to Default Program or Terminate the Program
12. The bike passcodes and Passcode Manager access code will be stored in a text file. They are also encrypted, and can be encrypted with a key and the typo of the key.

# Criterion B: Design
### System Diagram
![System Diagram](https://github.com/user-attachments/assets/6a3c4598-6e75-4f09-9566-f68c507c992c)
**Fig. 1** Image of System Diagram.

### Flow diagrams for algorithms
![Overall Program View](https://github.com/user-attachments/assets/c114c8f2-c139-4db9-a735-f8e9cf298f1d)
**Fig. B1** Flowchart gives an overview of the flow of the program. Anything related to the passcode only ran after access code entered.
<br>
<br>
![Default Program](https://github.com/user-attachments/assets/ee99ed83-6814-49ec-8454-ce9e62497c65)
**Fig. B2** Code and Explanation flow chart for the "Default Program" mentioned in Figure 1
<br>
<br>
![Encryption Algorithm](https://github.com/user-attachments/assets/ff92ce91-e51a-4c71-b85d-566cf79640c4)
**Fig. B3** Code and Explanation flow chart for the encryption algorithm. Decryption can be achieved by reverseing the encryption algorithm with the right key


### Data storage
The bike rental rate data is stored as an unencrypted .csv file named bike_price.csv

The bike's passcode data is stored as an encrypted .csv file named watermelon_juice.csv. This name is to detract potential unauthorized users from accessing this file in the first place.

The Passcode Manager access code is not stored, but rather its hash generated by the SHA256 algorithm is stored in a .txt file instead. This is to ensure that unauthorized users has no way of accessing the passcode. This means that even when they are able to access the passcode manager, they cannot decrypt the bike's passcode data, as they are encrypted using the access code.

### Sketches of the application (wireframe diagrams)
![image](https://github.com/user-attachments/assets/1bdaa107-3402-4f84-b9c1-61eaf0a67071)


### Test plan
All tests are in chronological order, tests that can be tested at the same time are listed as the same number.

Due by September 17:

1. Encryption Method. Test both encryption and decryption.
2. Test key generation from input string (Test by inputting key into encryption and decryption algorithm)
3. Testing applying the encryption to an entire database file with multiple keys
4. Loading bike data, encrypted passcode, and hashed Access Code into memory
5. Test Default Program Function (check for handling invalid input)
6. Test Default Program Access Passcode function

Due by September 20:

5, Test passcode input function (Return inaccurate if user enter wrong access code

5, Test function that views passcodes (handle invalid bike number, handle multiple bikes data)

5, Test function that creates passcode (handle invalid bike number, database update after program exit, updating data in memory)

5, Test function that deleted passcode (handle invalid bike number, database update after program exit, updating data in memory)

5, Test function that updates passcode (handle invalid bike number, database update after program exit, updating data in memory)

6. Test updating passcode manager (Only proceed if entered the current Access Code, confirm new Access Code twice, Access Code change correctly reflected in bike passcode database, new Access Code can be use to access Passcode Manager, while the previous cannot., new Access Code's hash is correctly updated in text file.
7. Test exit functions (Exit functions exit the according function/code)

## Record of Tasks

| Task Number |                                                      Planned Action                                                     |                                                Planned Outcome                                               | Time Estimated | Target Completion Date | Criterion |
|:-----------:|:-----------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------:|:--------------:|:----------------------:|:---------:|
|           1 | Meet with client and finish problem defintion                                                                           | Have a clear problem definition                                                                              | 20 minutes     |                 Sep 11 | A         |
|           2 | Create a detailed proposed solution and success criteria                                                                | Provide the client with an idea of a solution to their problem                                               | 1 hour         |                 Sep 12 | A         |
|           3 | Modify the Success Criteria and proposed solution based on the client's feedback                                        | Have a proposed solution and success criteria that the client agrees with                                    | 30 minutes     |                 Sep 13 | A         |
|           4 | Create an overview flowchart of the program                                                                             | Have an outline of what functions I would need to create and the variables and database which I need to keep | 1 hour         |                 Sep 13 | B         |
|           5 | Create wireframe diagrams for the software's screens and features                                                       | Determine a clear user interfact for the software                                                            | 2 hours        |                 Sep 13 | B         |
|           6 | Create a test plan                                                                                                      | Have a clear view on what I need to test in order to fulfill the Success Criteria                            | 20 minutes     |                 Sep 14 | A         |
|           7 | Create an encryption method with the client and problem in mind                                                         | Have an encryption method that is secure enough, but does not provide a frustrating experience for my client | 4 hours        |                 Sep 14 | C         |
|           8 | Create functions to print out both the Default Program and Passcode Manager screen                                      | Verify that my idea of the user interface is possible in the terminal                                        | 1 hour         |                 Sep 14 | C         |
|           9 | Set up the necessary database file and write code to load their data into program's memory                              | Ensure that my data is saved even after exitting the program                                                 | 1 hour         |                 Sep 15 | C         |
|          10 | Create function that returns rental rate                                                                                | Feature of the Default Program                                                                               | 1 hour         |                 Sep 16 | C         |
|          11 | Create a view bike code function                                                                                        | Feature for the Passcode Manager and Success Criteria                                                        | 30 minutes     |                 Sep 16 | C         |
|          12 | Create function for update, create, and delete passcode (functions that modifies the database)                          | Feature for the Passcode Manager and Success Criteria                                                        | 5 hours        |                 Sep 16 | C         |
|          13 | Create function to change Access Code and modify the encrypted database accordingly                                     | Feature for the Passcode Manager and Success Criteria                                                        | 1.5 hours      |                 Sep 16 | C         |
|          14 | Verify with computer science expert, Dr. Ruben Pinzon, that my encryption method is valid                               | Ensure that my encryption method has a sufficient level of reliability                                       | 5 minutes      |                 Sep 16 | A         |
|          15 | Create a print all available bike function (Dr. Pinzon's Feedback) and a clear console function                         | Improve the user experience                                                                                  | 45 minutes     |                 Sep 17 | C         |
|          16 | Create function to ask user to enter access code again to either decrypt/encrypt passcode                               | Ensure that the access code is never stored in memory if not needed                                          | 15 minutes     |                 Sep 20 | B         |
|          17 | Get feedback from my peers                                                                                              | Ensure that my program has no fatal errors and add more accessibility features                               | 70 minutes     |                 Sep 25 | A, B      |
|          18 | Implement the feed back from my peer                                                                                    | Make my product more user friendly                                                                           | 3 hours        |                 Sep 25 | C         |
|          19 | Create finalized flow chart for the entire program, encryption method, and detailed Default Mode (Access Code checker)  | Explicitly show how my product works                                                                         | 2 hours        |                 Sep 26 | B         |
|          20 | Create exit functions                                                                                                   | Feature for the Passcode Manager                                                                             | 10 minutes     |                 Sep 26 | C         |
|          21 | Create a demonstration video for my final product                                                                       | Verify that my product works in its entirety                                                                 | 45 minutes     |                 Sep 26 | B, C      |
|          22 | Add additional comments to my source code                                                                               | For ease of possible future modifications                                                                    | 20 minutes     |                 Sep 27 | C         |
|          23 | Upload all files and documentation onto GitHub                                                                          | Show that my project is finished                                                                             | 10 minutes     |                 Sep 27 | B         |

# Show that the product works
[Please click here for the 3 minute demonstration video](https://youtu.be/nyCSnCaLIq8)
[Please click here for the fully voice overed product walkthrough](https://youtu.be/M2uInO910Hs)
