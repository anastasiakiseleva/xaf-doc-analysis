---
uid: "112579"
title: Application Model (UI Settings Storage)
owner: Andrey Kozhevnikov
---
# Application Model (UI Settings Storage)

XAF uses the same application business logic to construct UI for different target platforms. The framework identifies business model classes, analyzes them, and builds metadata - an XML file that describes an application. That metadata is the **Application Model**. XAF uses it to build the application's UI for the required platform.

For example, you can declare the following simple class:

![simpleclass](~/images/simpleclass.png)

XAF identifies this class as part of the business model and generates a corresponding node in the **Application Model**. This is what the node looks like in [Model Editor](xref:112582)

![simpleClassModelEditor](~/images/simpleClassModelEditor.png)

Based on this **Application Model**, XAF generates UI for Blazor and WinForms platforms. The following image shows a Blazor example.

![simpleclassBlazor](~/images/simpleclassBlazor.png)
 
Refer to the document below to learn how you can use the **Application Model** to customize your application's UI:

## [How the Application Model Works](xref:112580)
* Application Model basics
* Which classes take part in Model construction
* Application Model structure, layers, and storage media
* How XAF uses Application Model values to configure a UI element
### [Change the Application Model](xref:403527)
* Model Editor
* Access model values in code
### [Extend the Application Model](xref:112810)
* How to add new nodes and their properties
* How to customize existing nodes
### [Enable Administrative UI to Manage Model Differences](xref:113704)
### [Merge End-User Customizations into the XAF Solution](xref:113335)

## Advanced tasks
* [](xref:112796)
* [](xref:403533)
* [](xref:118592)
* [](xref:403535)
* [](xref:113316)
* [](xref:113698)

