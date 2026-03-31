---
uid: "112796"
seealso:
- linkId: "112810"
- linkId: "113089"
title: "How to: Convert Application Model Differences Between Versions Due to Structural Node Changes"
---
# How to: Convert Application Model Differences Between Versions Due to Structural Node Changes

This topic describes what to do if you release an update for your application and the Application Model is incompatible with the previous version. 
## XML Converter or Node Updater: How to Choose 

### Basic Scenario

You plan to release a new version of your application. The update contains changes to the Application Model. For example, you renamed a node property or moved a node to another position within the tree. Your goal is to make sure that the application remains operational and users do not lose any changes they made to the Application Model while they used the previous version. 
### Possible Upgrade Issues

On startup, an XAF application attempts to load the Application Model. It scans for the changes users made to the model and tries to apply them. If the Application Model structure changed since the last version, XAF fails to process the differences and displays an error message.  
### Solution 

Whenever you plan to change the Application Model structure, make sure to implement a way to convert the differences. You can use the following two techniques. 

1. **XML Converter**. Implement the [](xref:DevExpress.ExpressApp.Updating.IModelXmlConverter) interface to process XAFML files (a custom XML format). This method processes nodes one by one. It may not suit your needs if you need to manage multiple nodes at a time.
2. **Node Updater**. Implement the [](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1) interface. Such updaters can perform much more versatile conversions.

Review the following sections for examples.  

## XML Converter Samples

This section lists common Application Model upgrade scenarios that you can resolve with an XML Converter.   

In all samples, you need to extend your module with the [](xref:DevExpress.ExpressApp.Updating.IModelXmlConverter) interface and implement the [ConvertXml()](xref:DevExpress.ExpressApp.Updating.IModelXmlConverter.ConvertXml(DevExpress.ExpressApp.Updating.ConvertXmlParameters)) method. XAF calls this method for each node in the Application Model so that you can adjust the settings as necessary.

### Sample: Property Type Change

This example shows how to process a change to a property type. 

Suppose that a module's previous version extended the Application Model with a **Mode** property. Users could use strings "Simple" or "Advanced" as property values. 

# [C#](#tab/tabid-csharp)

```csharp{4-5}
using DevExpress.ExpressApp.Model;

public interface IModelMyOptions{
    // accepts strings "Simple" or "Advanced"
    string Mode { get; set; }
}
public sealed partial class MyModule : ModuleBase {
    //...
    public override void ExtendModelInterfaces(ModelInterfaceExtenders extenders) {
        base.ExtendModelInterfaces(extenders);
        extenders.Add<IModelOptions, IModelMyOptions>();
    }
}
```
***

The new version changes the property's type to an enumeration. (Note that the code also renames one of the modes from "Simple" to "Basic".)

# [C#](#tab/tabid-csharp)

```csharp{1,4-5}
public enum OperatingMode { Basic, Advanced }

public interface IModelMyOptions {
    // now accepts enumeration values
    OperatingMode Mode { get; set; }
}
```
***

You can implement the following XML Converter to ensure correct transition to the new version. 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Updating;

public sealed partial class MyModule : ModuleBase, IModelXmlConverter {
    //...
    public void ConvertXml(ConvertXmlParameters parameters) {
        // Check if this is the Options node.
        if(typeof(IModelOptions).IsAssignableFrom(parameters.NodeType)) {
            // Check if the user assigned a value to Mode.
            string property = "Mode";
            if(parameters.ContainsKey(property)) {
                // Retrieve the value.
                string value = parameters.Values[property];
                // If it's a legacy value, convert.
                if(!Enum.IsDefined(typeof(OperatingMode), value)) {
                    switch(value.ToLower()) {
                        case "advanced":
                            parameters.Values[property] = OperatingMode.Advanced.ToString();
                            break;
                        default:
                            parameters.Values[property] = OperatingMode.Basic.ToString();
                            break;                            
                    }                                  
                }                    
            }
        }
    }
}
```
***

### Sample: Property Name Change

Suppose the module's previous version extended the Application Model with the **Mode** property. The new version renames this property to **OperatingMode**. 

You can use the following XML Converter to handle this transition:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Updating;

public sealed partial class MyModule : ModuleBase, IModelXmlConverter {
    //...
    public void ConvertXml(ConvertXmlParameters parameters) {
        if(typeof(IModelOptions).IsAssignableFrom(parameters.NodeType)) {
            string oldProperty = "Mode";
            string newProperty = "OperatingMode";
            if(parameters.ContainsKey(oldProperty)) {
                parameters.Values[newProperty] = parameters.Values[oldProperty];
                parameters.Values.Remove(oldProperty);
            }
        }
    }
}
```
***

## Node Updater Samples

This section lists common Application Model upgrade scenarios that you can resolve with a Node Updater.   

To create a Node Updater, follow the steps below: 

* Extend any class with the [](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1) interface. The generic type parameter indicates the Application Model node type. 
* Implement the interface's [UpdateNode](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1.UpdateNode(`0,DevExpress.ExpressApp.Model.IModelApplication)) method. This method's parameters allow you to access the node and the entire Application Model. This means you can access any node in your code and thus implement conversions of any complexity.
* Override the [ModuleBase.AddModelNodeUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddModelNodeUpdaters(DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator)) method to register the Node Updater class. 

### Sample: Property Location Change

Suppose a module's previous version extended the Application Model's **Options** node with an **OperatingMode** string property. 

# [C#](#tab/tabid-csharp)

```csharp
public interface IModelMyOptions {
    OperatingMode OperatingMode { get; set; }
}
public enum OperatingMode { Basic, Advanced }
```
***

The new version moves the property to a newly introduced child node:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;

public interface IModelMyOptions {
    IModelChildOptions ChildOptions { get; }
}
public interface IModelChildOptions : IModelNode {
    OperatingMode OperatingMode { get; set; }
}
public enum OperatingMode { Basic, Advanced }
```
***

Create a Node Updater to ensure correct transition to the new version. You can implement the interface in your module class as shown below. 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Model.Core;

// Node Updater interface will process the Options node.
public sealed partial class MyModule : ModuleBase, IModelNodeUpdater<IModelOptions> {
    //...
    public void UpdateNode(IModelOptions node, IModelApplication application) {
        string myProperty = "OperatingMode";
        // Try and find the property at its previous location.
        if(node.HasValue(myProperty)) {
            // Retrieve the value.
            string value = node.GetValue<string>(myProperty);
            // Clear the legacy property.
            node.ClearValue(myProperty);
            // Assign the value to the new property.
            ((IModelMyOptions)node).ChildOptions.OperatingMode = 
                (OperatingMode)Enum.Parse(typeof(OperatingMode), value);
        }
    }        
}
```
***

Override the [ModuleBase.AddModelNodeUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddModelNodeUpdaters(DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator)) method and register the Node Updater.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Model.Core;

public sealed partial class MyModule : ModuleBase, IModelNodeUpdater<IModelOptions> {
    //...
    public override void AddModelNodeUpdaters(IModelNodeUpdaterRegistrator updaterRegistrator) {
        base.AddModelNodeUpdaters(updaterRegistrator);
        updaterRegistrator.AddUpdater<IModelOptions>(this);
    }    
}
```
***