COMMAND PATTERN

It's a behavioral pattern.

Intends to encapsulate in an object all the data required for performing a given action (command),
including what method to call, the method's arguments, and the object to which the method belongs.

Allows us to decouple objects that produce the commands from their consumers, so that's why the pattern is commonly
known as the producer-consumer pattern.

It has four components:

1) Command classes:
A command is an object whose role is storing all the information required for executing an action, including
the method to call, the method arguments, and the object (known as the receiver) that implements the method.

It's composed of the command interface which contains its execute() method and all concrete classes that implement
the command interface.

2) Receiver class:
A receiver is an object that performs a set of cohesive actions. It's the component that performs the actual action
when the command's execute() method is called. In other words, it's the component inside the concrete command class
that actually performs the action and know exactly what must be done. Every class can work as a receiver.

3) Invoker class:
An invoker is an object that knows how to execute a given command but doesn't know how the command has been
implemented. It only knows the command's interface.

4) Client class
It's an object that controls the command execution process by specifying what commands to execute and at what stages
of the process to execute them. It creates the concrete command objects and define its receptor.