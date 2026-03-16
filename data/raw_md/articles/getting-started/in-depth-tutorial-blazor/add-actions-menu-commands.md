---
uid: "402128"
title: Add Actions (Menu Commands)
owner: Alexey Kazakov
seealso: []
---
# Add Actions (Menu Commands)

Before you proceed with this section of the tutorial, you should familiarize yourself with the following basic concepts of the **Cross-Platform .NET App UI**.

**Action**
	
:   Visually, Action is a toolbar item or another control that performs the associated code when an end user manipulates it. XAF has several predefined Action types. You can choose the appropriate type depending on how you want your Action to be displayed within the UI. All Actions expose the **Execute** event whose handler is executed when end users manipulate the corresponding element. For more details, refer to the [Actions](xref:112622) topic.

**Controller**
	
:   Controllers are classes inherited from the [](xref:DevExpress.ExpressApp.Controller) class. This class has the following descendants that can also serve as base classes for controllers:
	
    * [](xref:DevExpress.ExpressApp.ViewController) and its generic versions: [](xref:DevExpress.ExpressApp.ViewController`1) and [](xref:DevExpress.ExpressApp.ObjectViewController`2)
    * [](xref:DevExpress.ExpressApp.WindowController)
	
    Controllers [implement business logic](xref:113711) in your application. The application either executes this logic automatically (for example, on activation of a View) or triggers it when a user executes an Action declared within the Controller. XAF uses [reflection](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/reflection) to automatically collect controllers implemented within modules. Controller classes should be _public_. The Controller properties and base class determine the View or the Window where this controller is active. For more details, refer to the [Controllers](xref:112621) topic.

Controllers and Actions are instruments that implement custom features in an XAF application. In this tutorial section, you will learn how to complete the following tasks:

- Add Actions of different types
- Implement Controllers without Actions
- Modify the behavior of existing Controllers and Actions

We recommend that you complete the lessons in the following order:

* [](xref:402157)
* [](xref:402155)
* [](xref:402158)
* [](xref:402159)
* [](xref:402156)
