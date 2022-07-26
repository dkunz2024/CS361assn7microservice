# CS361 Assignment #7 Microservice Communication Contract


## Requesting & Retrieving data

1) Download assn7send.py & assn7receive.py from the repo
2) SEND: Start by running the assn7send.py first, do this by:
#### python assn7send.py
3) It will ask you to input a zipcode or address. When you've successfully inputted one of these, it will craft a message to send.
4) RECEIVE: Receive the data by running the assn7receive.py, using:
#### python assn7receive.py
5) The terminal will first print the message that was receieved. Then, you will be given a sample list of 5 locations near you.

Please let me know if you have any questions! You can reach me over discord & text like we have been communicating with so far.

## UML sequence diagram
The assn7send.py file gathers and sends over a user's zipcode/address using main(). After assn7receive.py receives it, nothing else happens.
![UMLsequence](https://user-images.githubusercontent.com/56979982/180923662-a8453aa4-c2f6-43c3-9fbb-e859161e1703.png)
