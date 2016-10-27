# IoC
#CS455 Software Engineering
#Inversion of Control

This sample is written in python 3.2 and depends on pip3
Inversion of Control (IoC) increases the modularity of program and introduce flexibility to add run time components and perform independent testing of individual components without worrying about the dependencies.
We'll view IoC as Dependency Injection (DI). We'll essentially decouple the dependencies between layers through some shared abstractions.
Use-Case Description
There are two essential classes Products and Operations, naturally the class Operations depends on Products and offers the possibility of different operations on a List of products (in this case all types of a particular product).
Class Products implements two basic functionality ”add” an item and “getList” returns all the items.
Class Operations implements “isProduct”, an object of this class needs an instance of Products (Hence the dependency).
Injecting Dependency


  


