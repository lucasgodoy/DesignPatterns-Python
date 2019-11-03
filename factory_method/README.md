#FACTORY METHOD

It's a creational pattern.

Defines an interface to create an object, but lets subclasses decide which class to instantiate. 
This pattern postpone class instantiation to subclasses in a way they can instantiate according
to its necessities, when they already know what type of class to instantiate. In other words, this pattern
delegates the responsibility of initializing a class from the client to a particular factory class by creating a 
type of virtual constructor. To achieve this, we rely on a factory which provides us with the objects, hiding the actual
implementation details. The created objects are accessed using a common interface.

It has four components:

1) Product:
Defines an interface of objects that the factory method creates.

2) Concrete product:
Implements the Product interface.

3) Creator:
Declares the factory method, returning a Product type object. 

4) Concrete creator:
Redefines the factory method to return a instance of a concrete product.