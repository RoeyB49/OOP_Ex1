# OOP_Ex1
1. Sources:

   • https://www.irjet.net/archives/V3/i7/IRJET-V3I7181.pdf

   • https://www.kth.se/social/files/588617c2f276547fe1dbf8d2/AJanssonKUgglaLingvall_dkand15.pdf

    • https://github.com/00111000/Elevator-Scheduling-Simulator

2. Offline Algorithm:

    Our Algorithm based on preliminary information that were given us:
    
    • List of elevators calls
    
    •  Numbers of the elevators in the building
    
    • JSON files that contains detailed information about each building and about each elevator in it.

    The idea of our algorithm is simple because it's much easier and, in the end, more efficient to decide which elevator is the best to take is you have the list of calls upfront.
    We will the describe the algorithm by steps:
    
    • First, we want to read all the details we have to be able to work with it means we need to take the calls list and the building and elevators details into code(read JSON into object, read&edit csv file).

    • After we have the list of calls, we want to be able to allocate the best elevator possible to each call. To do so we got a formula(given to us) that calculate the expected time the elevator will travel from given floor to destination floor after we get the answer, we will want to take the lowest possible time we got and make it the "best" elevator possible.

    • To make it even more efficient we added function that calculate the distance between the call floor to the floor that the "best" elevator(from the formula) floor.

    • The output in the end will be the edited list of calls now with the allocation of the elevators.

3. Our functions:

    • def from_csv(self, file_name):

    read from csv file(in our case the csv file is the list of calls).

    • def from_json(self, file_name):

    read from JSON file and make it an object in python(in our case the JSON file contains the details of each building).

    • def assignElev(self, b, call):

    as we explained above this function will assign the "best" elevator by calculating with function below.

    • def calculateTime(self, lastFloor, elev, call):

    this function will calculate then expected time the elevator will travel from given floor to destination floor and include the distance between the call and the elevator current position("lastfloor").

    • def save_csv(self, assignedElevList, file_name):

    this function will save the edited list of calls to a new csv file.

4. UML Diagram:(links below)

    https://ibb.co/brJfdFz

    https://www.linkpicture.com/view.php?img=LPic61967c8955dfe556123132

5. UniTest explanation:

    • TestCalls:

    We are testing if the calls csv file is read correctly to our code.

    • Testbuilding:

    We are testing if the building JSON file is read correctly to our code. 

6. Cases check by tester:

    B1 , Calls A

    Code Owners,1,2,  Building_file,data/B1.json,  Calls,data/output.csv

    Total waiting time: 11292.0,  average waiting time per call: 112.92,  unCompleted calls,0,  certificate, -252680109

    B2 , Calls A

    Code Owners,1,2,  Building_file,data/B2.json,  Calls,data/output.csv

    Total waiting time: 6044.0,  average waiting time per call: 60.44,  unCompleted calls,0,  certificate, -341555593

    B3 calls A

    Code Owners,1,2,  Building_file,data/B3.json,  Calls,data/output.csv

    Total waiting time: 4372.0,  average waiting time per call: 43.72,  unCompleted calls,0,  certificate, -282850382

    B4 calls A

    Code Owners,1,2,  Building_file,data/B4.json,  Calls,data/output.csv

    Total waiting time: 2427.0,  average waiting time per call: 24.27,  unCompleted calls,0,  certificate, -485655093

    B5 calls A

    Code Owners,1,2,  Building_file,data/B5.json,  Calls,data/output.csv

    Total waiting time: 1652.0,  average waiting time per call: 16.52,  unCompleted calls,0,  certificate, -457785037

    B3 , Calls B

    Code Owners,1,2,  Building_file,data/B3.json,  Calls,data/output.csv

    Total waiting time: 633083.5880959925,  average waiting time per call: 633.0835880959925,  unCompleted calls,252,  certificate, -2615234438

    B4 , Calls B

    Code Owners,1,2,  Building_file,data/B4.json,  Calls,data/output.csv

    Total waiting time: 295403.0223360008,  average waiting time per call: 295.4030223360008,  unCompleted calls,132,  certificate, -612608119

    B5 , Calls B

    Code Owners,1,2,  Building_file,data/B5.json,  Calls,data/output.csv

    Total waiting time: 212254.11993599898,  average waiting time per call: 212.25411993599897,  unCompleted calls,82,  certificate, -866924593

    B3 , Calls C

    Code Owners,1,2,  Building_file,data/B3.json,  Calls,data/output.csv

    Total waiting time: 626588.012525009,  average waiting time per call: 626.5880125250089,  unCompleted calls,205,  certificate, -2550646558

    B4 , Calls C

    Code Owners,1,2,  Building_file,data/B4.json,  Calls,data/output.csv

    Total waiting time: 321245.97842999955,  average waiting time per call: 321.2459784299995,  unCompleted calls,126,  certificate, -1512116086

    B5 , Calls C

    Code Owners,1,2,  Building_file,data/B5.json,  Calls,data/output.csv

    Total waiting time: 196772.9479299999,  average waiting time per call: 196.7729479299999,  unCompleted calls,26,  certificate, -810912874

    B3 , Calls D

    Code Owners,1,2,  Building_file,data/B3.json,  Calls,data/output.csv

    Total waiting time: 591654.6049000041,  average waiting time per call: 591.6546049000041,  unCompleted calls,150,  certificate, -1643326099

    B4 , Calls D

    Code Owners,1,2,  Building_file,data/B4.json,  Calls,data/output.csv

    Total waiting time: 317559.2992340027,  average waiting time per call: 317.5592992340027,  unCompleted calls,99,  certificate, -1495971305

    B5 , Calls D

    Code Owners,1,2,  Building_file,data/B5.json,  Calls,data/output.csv

    Total waiting time: 202867.86829999991,  average waiting time per call: 202.8678682999999,  unCompleted calls,50,  certificate, -831842319


