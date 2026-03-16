---
uid: "404125"
title: Add Custom Nodes and Properties to the Application Model in Code
owner: Elena Khamlyuk
seealso:
  - linkId: "112580"
  - linkId: "112810"
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/XAF-how-to-add-an-unbound-column-to-gridlisteditor-to-execute-a-custom-action-for-a-record
    altText: XAF - Add an Unbound Column to GridListEditor to Execute a Custom Action for a Record
---
# Add Custom Nodes and Properties to the Application Model in Code
 
This topic describes how to extend the auto-generated [Application Model](xref:112579) with custom nodes and properties in code. Use the [Model Editor](xref:112582) to edit the Application Model visually.

 ![An Application Model node and node property](~/images/app-model-node-and-property.png)

> [!Tip]
> If you need to change the existing Node properties, see the following topic: [](xref:112810).


## Add a Custom Property to an Existing Node

This example shows how to add the _MyCustomProperty_ to the root Model node.

1. Declare an [](xref:DevExpress.ExpressApp.Model.IModelNode) descendant interface with a custom property.

    **File:** _MySolution.Module\Module.cs_

    ```csharp
    using DevExpress.ExpressApp.Model;
    // ...
    namespace MySolution.Module {
        // ... 
        public interface IModelMyModelExtension : IModelNode {
            string MyCustomProperty { get; set; }
        }
    }    
    ```

2. Override the [ModuleBase.ExtendModelInterfaces](xref:DevExpress.ExpressApp.ModuleBase.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)) method to add the custom property to the node:

    **File:** _MySolution.Module\Module.cs_

    ```csharp
    using DevExpress.ExpressApp.Model;
    // ...
    namespace MySolution.Module {
        public sealed partial class MySolutionModule : ModuleBase {
            // ...
            public override void ExtendModelInterfaces(ModelInterfaceExtenders extenders) {
                base.ExtendModelInterfaces(extenders);
                extenders.Add<IModelApplication, IModelMyModelExtension>();
            }
            // ...
        }
    }
    ```

    Alternatively, implement the [](xref:DevExpress.ExpressApp.IModelExtender) interface in a [Controller](xref:112621) and implement the [ModuleBase.ExtendModelInterfaces](xref:DevExpress.ExpressApp.ModuleBase.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)) method in the Controller code:
 
    ```csharp
    using DevExpress.ExpressApp.Model;
    using System.ComponentModel;
    // ...
    namespace MySolution.Module {

        public class MyController : ViewController<ListView>, IModelExtender {
            public void ExtendModelInterfaces(ModelInterfaceExtenders extenders) {
                extenders.Add<IModelApplication, IModelMyModelExtension>();
            }
        }
    }
    ```
 
3. Rebuild the solution and open the [Model Editor](xref:112582) to check the result. The root [](xref:DevExpress.ExpressApp.Model.IModelApplication) node contains **MyCustomProperty**.

    ![CustomizeApplicationModelInCode_1](~/images/customizeapplicationmodelincode_1116643.png)

To add **MyCustomProperty** to another node, pass the interface corresponding to this node instead of **IModelApplication** to the **extenders.Add** method. The following topic lists available interfaces: [Application Model Interfaces Shipped with XAF](xref:403535).

In XAF, a custom property's name cannot be _Application_. The @DevExpress.ExpressApp.Model.IModelNode interface already includes the @DevExpress.ExpressApp.Model.IModelNode.Application property that returns the Application Model's root node. If you implement a custom property that is named _Application_, the following exception occurs: _Cannot compile the generated code_.


You can decorate node properties with the following attributes:

[Browsable](xref:System.ComponentModel.BrowsableAttribute)
:   Specifies whether a property is displayed in the [Model Editor](xref:112582). If you use the technique described above to add a property, Model Editor shows the property. To hide this property, decorate it with the **Browsable** attribute and pass **false** as a parameter.

[Category](xref:System.ComponentModel.CategoryAttribute)
:   Specifies a category. The Model Editor groups properties of each node by their categories in the property grid. The default category is _Misc_. To assign a category to a property, decorate the property with the **Category** attribute and pass a category name as a parameter. If the specified category does not exist, XAF adds this category.

[DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute)
:   Specifies a name of a property that contains a list of predefined values for the current property. XAF generates a drop-down list in the Model Editor property grid to shows these values. If the current node exposes a list of child nodes (implements the **IModelList\<**_ChildNodeType_**>** interface), you can pass _this_ as the **DataSourceProperty** attribute parameter to show the child nodes as predefined values in the property grid.

[DefaultValue](xref:System.ComponentModel.DefaultValueAttribute)
:   Specifies a property's default value.

[Editor](xref:System.ComponentModel.EditorAttribute)
:   Binds a custom editor to the property.

[Description](xref:System.ComponentModel.DescriptionAttribute)
:   Specifies a property's description displayed at the bottom of the Model Editor.

[Localizable](xref:System.ComponentModel.LocalizableAttribute)
:   Specifies whether a property can be [localized](xref:112595). To define a localizable property, decorate it with the **Localizable** attribute and pass **true** as a parameter.

[ReadOnly](xref:System.ComponentModel.ReadOnlyAttribute)
:   Specifies whether a user can change the property value in the Model Editor. Decorate a property with the **ReadOnly** attribute and pass **true** as a parameter to prohibit value modification in the Model Editor. Alternatively, omit the set accessor.

[Required](xref:System.ComponentModel.DataAnnotations.RequiredAttribute)
:   Specifies whether a property is required. When you decorate a property with the **Required** attribute, the Model Editor does not allow you to save changes if the property value is not set.


The following code adds the **Localizable** attribute to **MyCustomProperty** and makes **MyCustomRequiredProperty** required:

**File:** _MySolution.Module\Module.cs_

```csharp
using DevExpress.ExpressApp.Model;
using System.ComponentModel;
// ...
namespace MySolution.Module {
    // ...
    public interface IModelMyModelExtension : IModelNode {
        [Localizable(true)]
        string MyCustomProperty { get; set; }
        [Required]
        string MyCustomRequiredProperty { get; set; }
    }
}   
```

## Add a New Node to the Application Model

To create a custom node, declare an [](xref:DevExpress.ExpressApp.Model.IModelNode) descendant interface with custom properties.

If an interface property inherited from **IModelNode** omits the set accessor, the [Model Editor](xref:112582) displays it as a node (**MyChildNode** in the example below). If an interface property has the set accessor, the Model Editor displays it as a property in the property grid (**MyProperty** in the example below).

```csharp
[KeyProperty(nameof(Name))]
public interface IModelMyChildNode : IModelNode {
    string Name { get; set; }
    // ...
}

public interface IModelMyNodeWithChildNode : IModelNode {
    IModelMyChildNode MyChildNode { get; }
    IModelMyChildNode MyProperty { get; set; }
}

```

![A child node and node property](~/images/app-model-node-property.png)

The example below defines the **IModelMyChildNode** and **IModelMyNodeWithChildNode** interfaces derived from [](xref:DevExpress.ExpressApp.Model.IModelNode).

**File:** _MySolution.Module\Module.cs_

```csharp
using System.ComponentModel;
// ...
namespace MySolution.Module {
    // ...
    [KeyProperty(nameof(Name))]
    public interface IModelMyChildNode : IModelNode {
        string Name { get; set; }
        [Localizable(true)]
        string MyStringProperty { get; set; }
        int MyIntegerProperty { get; set; }
    }
    public interface IModelMyNodeWithChildNode : IModelNode {
        IModelMyChildNode MyChildNode { get; }
    }
    public interface IModelMyNodeWithChildNodes : IModelNode, IModelList<IModelMyChildNode> {
    }
}
```

**IModelMyNodeWithChildNodes** implements the **IModelList\<IModelMyChildNode>** interface to expose the list of **IModelMyChildNode** nodes.

You can decorate node interfaces with the following attributes:

Description
:   Specifies a node description displayed at the bottom of the Model Editor.
DisplayName
:   Specifies a node caption in the Model Editor.
DisplayProperty
:   Specifies the node's property name, whose value is used as the node's caption in the Model Editor.
[ImageName](xref:DevExpress.Persistent.Base.ImageNameAttribute)
:   Specifies a node image that the Model Editor displays for the node.
KeyProperty
:   Specifies a node key property. XAF uses key properties to identify nodes. A key property must be of the string type. If you do not use the **KeyProperty** attribute, XAF generates the **Id** property. In the example above, _Name_ is the key property for the _IModelMyChildNode_.

To add the **ModelMyNodeWithChildNodes** and **IModelMyNodeWithChildNode** nodes to the Application Model, extend the corresponding parent node interface as described in the section above: [Add a Custom Property to the Existing Node](#add-a-custom-property-to-an-existing-node).

**File:** _MySolution.Module\Module.cs_

```csharp
using System.ComponentModel;

namespace MySolution.Module {
    public sealed partial class MySolutionModule : ModuleBase {    
        // ...
        public override void ExtendModelInterfaces(ModelInterfaceExtenders extenders) {
            base.ExtendModelInterfaces(extenders);
            extenders.Add<IModelApplication, IModelMyModelExtension>();
        }
    }

    public interface IModelMyModelExtension : IModelNode {
        // ...
        IModelMyNodeWithChildNode MyNodeWithOneChildNode { get; }
        IModelMyNodeWithChildNodes MyNodeWithSeveralChildNodes { get; }
    }
}
```

Rebuild the solution and open the [Model Editor](xref:112582) to check the result.

![Add nodes to the Application Model](~/images/add-nodes-to-application-model.png)

You can use the context menu to add child nodes to the **MyNodeWithSeveralChildNodes** node.

![Add child custom nodes to the Application Model](~/images/add-child-nodes-to-custom-node.png)

## Use a Node Generator to Add Multiple Child Nodes

If you need to add a batch of similar child nodes to a parent node, use a Node Generator. Create a @DevExpress.ExpressApp.Model.ModelNodesGeneratorBase descendant and override the **GenerateNodesCore** virtual method. Use the _node_ parameter to access the parent node. The Node Generator below creates ten **IModelMyChildNode** nodes and assigns indices to them:

**File:** _MySolution.Module\Module.cs_

```csharp
using DevExpress.ExpressApp.Model.Core;
// ...
namespace MySolution.Module {
    // ...
    public class MyChildNodeGenerator : ModelNodesGeneratorBase {
        protected override void GenerateNodesCore(ModelNode node) {
            for (int i = 0; i < 10; i++) {
                string childNodeName = "MyChildNode " + i.ToString();
                node.AddNode<IModelMyChildNode>(childNodeName);
                node.GetNode(childNodeName).Index = i;
            }
        }
    }
}
```

> [!Tip]
> You can use the `node.Application` property to access the root Application Model node in the **GenerateNodesCore** method's code.

Use @DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute to associate a node implementation with a Node Generator:

**File:** _MySolution.Module\Module.cs_

```csharp
namespace MySolution.Module {
    // ...
    [ModelNodesGenerator(typeof(MyChildNodeGenerator))]
    public interface IModelMyNodeWithChildNodes : IModelNode, IModelList<IModelMyChildNode> {
    }
    // ...
}
```

Rebuild your solution and open the [Model Editor](xref:112582) to see the changes.

![Use Node Generator](~/images/use-node-generator.png)

Node Generators make changes at [the Application Model zero layer](xref:112580). XAF executes the **GenerateNodesCore** method when the **MyNodeWithSeveralChildNodes** data is requested for the first time and stores this data in the Application Model.


You can implement a single Node Generator for each node. Use [Generator Updaters](#use-generator-updaters-to-customize-nodes) for additional node customization.

## Implement a Property with a List of Predefined Values

Use the **DataSourceProperty** attribute to add a list of predefined values to a node property. Pass the name of a node property that contains a list of values as the **DataSourceProperty** parameter. You can also use _this_ to display the child nodes of the current node in the drop-down list with available values.

### Display Child Nodes in the Drop-Down List

The example below extends the **IModelMyNodeWithChildNodes** node with the **SelectedChildNode** property. This property allows users to select child nodes as available values.

**File:** _MySolution.Module\Module.cs_

```csharp
using DevExpress.Persistent.Base;
// ...
namespace MySolution.Module {
    // ...
    public interface IModelMyNodeWithChildNodes : IModelNode, IModelList<IModelMyChildNode> {
        [DataSourceProperty("this")]
        IModelMyChildNode SelectedChildNode { get; set; }
    }
}
```

Rebuild your solution to update the Application Model. The image below shows the result.

![Property with a List of Predefined Values](~/images/property-with-predefined-values.png)

If you add or remove child nodes, the drop-down list reflects changes immediately.

### Display Custom Values in the Drop-Down List

The example below implements the custom **ListProperty** and displays a list of predefined values for this property in the property grid. To define a list of values, follow the steps below:

1. Implement a collection property without the set accessor (**SourceListProperty** in the example below). Apply the **Browsable(false)** attribute to this property to hide it from the Application Model structure. 
 
2. Decorate **ListProperty** with the **DataSourceProperty** attribute and use the collection property name as the attribute parameter.

3. Create a static class and decorate it with the **DomainLogic** attribute. Use the node interface, which contains the **ListProperty** property, as the attribute parameter.

4. Add the **Get_SourceListProperty** method to this class. The **Get_SourceListProperty** method returns the **SourceListProperty** value. This value contains a list of predefined values for **ListProperty**. In the example, it returns the following values: `"Value1", "value2", "Value3" `.

**File:** _MySolution.Module\Module.cs_    
    
```csharp
public interface IModelMyNodeWithChildNodes : IModelNode, IModelList<IModelMyChildNode> {
    [DataSourceProperty("SourceListProperty")]
    String ListProperty { get; set; }

    [Browsable(false)]
    IEnumerable<String> SourceListProperty {
        get;
    }
}
[DomainLogic(typeof(IModelMyNodeWithChildNodes))]
public static class ModelMyNodeWithChildNodesLogic {
    public static IEnumerable<string> Get_SourceListProperty(IModelMyNodeWithChildNodes myNodeWithChildNodes) {
        return new List<string>() { "Value1", "value2", "Value3" };
    }
}
```

![A property with a list of custom values in the Application Model](~/images/app-model-list-values.png)


## Use Generator Updaters to Customize Nodes

Use Generator Updaters to mass update child nodes. Create a Generator Updater class as a @DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1 descendant. The **ModelNodesGeneratorUpdater\<T>** class exposes the @DevExpress.ExpressApp.Model.IModelNodesGeneratorUpdater.UpdateNode(DevExpress.ExpressApp.Model.Core.ModelNode) virtual method. Override this method to update child nodes. Use the _node_ parameter to access the parent node. 

You can add several Generator Updaters to a Node Generator. The example below implements two Generator Updaters. The first Updater sets the **IModelMyChildNode.MyIntegerProperty** value for each node, the second one sets the **IModelMyNodeWithChildNodes.SelectedChildNode** property. 

```csharp
namespace MySolution.Module {
    // ...
    public class MyChildNodesUpdater1 : ModelNodesGeneratorUpdater<MyChildNodeGenerator> {
        public override void UpdateNode(ModelNode node) {
            foreach (IModelMyChildNode childNode in ((IModelMyNodeWithChildNodes)node)) {
                if (childNode.Index.HasValue) {
                        childNode.MyIntegerProperty = (int)childNode.Index + 1;
                }
            }
        }
    }
    public class MyChildNodesUpdater2 : ModelNodesGeneratorUpdater<MyChildNodeGenerator> {
        public override void UpdateNode(ModelNode node) {
            ((IModelMyNodeWithChildNodes)node).SelectedChildNode =
                ((IModelMyNodeWithChildNodes)node)["MyChildNode 9"];
        }
    }
}
```

> [!Tip]
> You can use the `node.Application` property to access the root Application Model node in the **UpdateNode** method's code.

 Use the [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method to register Generator Updaters.

**File:** _MySolution.Module\Module.cs_

```csharp
using DevExpress.ExpressApp.Model.Core;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    // ...       
    public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters) {
        base.AddGeneratorUpdaters(updaters);
        updaters.Add(new MyChildNodesUpdater1());
        updaters.Add(new MyChildNodesUpdater2());
    }
    // ...
}
```

Rebuild your solution and open the [Model Editor](xref:112582) to see the result.

![Mass update child nodes](~/images/application-model-mass-update.png)

You may not see the changes as displayed in the image above. This happens if you modify these property values in the Model Editor before the code is executed. Generator Updaters operate at the Application Model zero [layer](xref:112580) and changes made at design time override Updater settings. Reset differences for the **MyNodeWithSeveralChildNodes** node to see the changes: right-click the node and select **Reset Differences**. 

> [!Note]
> Node Generators and Node Updaters work at the Application Model zero layer. The [User Model Differences](xref:403527) storage does not contain these changes. To customize nodes at the User Model Differences layer, use the techniques from the following topic: [How to change the default Application Model value globally or for multiple nodes](https://supportcenter.devexpress.com/Ticket/Details/T271022/how-to-change-the-default-application-model-value-globally-or-for-multiple-nodes).

You can use the technique described above to attach Generator Updaters to [built-in Node Generators](xref:113316). The following topics contain examples for built-in Generators:

* [EnumDescriptor.GenerateDefaultCaptions](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GenerateDefaultCaptions*)
* [](xref:112992)
* [](xref:405483)
* [](xref:113315)
