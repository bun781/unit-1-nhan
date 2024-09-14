# Criterion A: Planning
## Problem Definition
My client is an old local bike rental shop owner in Karuizawa. As he puts his bikes in front of his store, he needs a way to lock them to prevent possible theft. To do so, he simply uses a bike lock for each bike. Additionally, to prevent every bike lock being compromised at the same time, he uses a different passcode for every single bike. 

Lately, he has complained tthat he cannot remember all the passcodes anymore, as the number of bikes in his shops ranges into the hundreds, and he feels like he is getting old. He tried to write all the passcodes in a booklet, but soon become paranoid of employees seeing every passcode of every bike, which he believes to be the starting point for a bike heist. Then he tried to use a simple cypher on the passcodes and write them down, but it also posed a challenge for him: the cypher took too long to crack, sometimes he makes a mistake that makes him repeat the entire process again; all of these steps, he said, were too mentally taxing and streessful for him to repeat multiple times during the day.

## Proposed Solution
To make the process easier for my client, I propose a hidden system that allows my client to manage the passcodes for his bikes.

This system will be embedded and disguised as a simple software to search up the rental price of a bicycle through inputting the bike’s number. However, when the user inputs a secret code, the program will change mode and act as a password manager that allows my client to perform CRUD operations on the passcodes. 

## Success Criteria
1. The software checks and accepts the appropriate user inputs to perform the search operation.
2. The software can handle typical errors (e.g. entering a bike number that does not exist, entering a string instead of a number, entering floats instead of integers) and give appropriate feedback
3. If the user enters the secret code, determined by the user, the program will change modes and acts as a password manager.
4. If the user enters the secret code ("open123"), the program will change modes and act as a password manager.
5. In the password manager, the user would be able to perform:
   * CRUD operations (Create, Read, Update, Delete) on bike passcode
   * Change the secret code
6. In password manager mode, the user should be able to perform CRUD operations (Create, Replace, Update, Delete):
   * Add a password (for example, for a website).
   * View the stored passwords (only if they re-enter the secret code).
7. The passwords will be stored in a text file. They are also encrypted.


# Criterion B: Design
### System Diagram

### Flow diagrams for algorithms
![flow](https://github.com/user-attachments/assets/93f4a0fb-66b8-4993-9b3d-b0b47deaeb82)
**Fig. 1** This is the flow diagram for the algorithm used to search in the data file...

### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan

## Record of Tasks

| Task Number | Planned Action              | Planned Outcome                                                 | Time Estimated | Target Completion Date | Criterion |
|-------------|-----------------------------|-----------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st Meeting with the client | Obtained a problem definition, understand what the situation is | 10 min         | Sep 7                  | A         |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |
