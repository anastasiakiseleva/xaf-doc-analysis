
---
uid: "402189"
title: Implement a Property Editor Based on a Custom Component (Blazor)
owner: Yekaterina Kiseleva
seealso:
- linkId: "113097"
- linkId: "113653"
- linkId: "403258"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-display-a-collection-property-as-a-checked-list-box
  altText: 'How to: Display a Collection Property as a Checked List Box'
---

# Implement a Property Editor Based on a Custom Component (Blazor)

This topic describes how to implement a Property Editor for ASP.NET Core Blazor applications. For this, implement the following entities in the [application project](xref:118045) (_MySolution.Blazor.Server_):  

[Component Model](#component-model)
:   An object representation of the component that is required to change the component's state.
[Property Editor](#property-editor) 
:   A class that integrates the component into your XAF application.

> [!NOTE]
> When you use Razor markup (*.razor) to create a custom component, ensure that the component's logic is separated from property editors. Use [Parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/#component-parameters) and the [@inject](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection#request-a-service-in-a-component) directive to supply necessary data to the component. Avoid mixing the component's logic with the component model or property editor.
>
>The process of component creation in XAF is similar to non-XAF applications. The Component Model contains information about component parameters and component type, and is responsible for linking the component with the property editor.
>
>
> For more information about the XAF Component Model, refer to the following topic: [](xref:404767).


The example below demonstrates a custom String Property Editor that displays the [InputText](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.forms.inputtext) component.

## Component Model 

1. Create a `ComponentModelBase` descendant and name it _InputTextModel_.
   In this class, declare properties that you will set in the underlying InputText component. The properties must have the same type and name as their counterparts in the component. In this example, use `Value`, `ValueChanged`, and `ValueExpression` properties.
2. Override the `ComponentType` method and return the component type.
   XAF automatically creates a [RenderFragment](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.renderfragment) to render `InputText` based on properties and component type specified in the Component Model.

**File**: _MySolution.Blazor.Server\Editors\InputTextModel.cs_

```csharp
using System.Linq.Expressions;
using DevExpress.ExpressApp.Blazor.Components.Models;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Forms;  

namespace YourSolutionName.Blazor.Server.Editors;

public class InputTextModel : ComponentModelBase {
    public string  Value {
        get => GetPropertyValue<string>();
        set => SetPropertyValue(value);
    }
    public EventCallback<string> ValueChanged {
        get => GetPropertyValue<EventCallback<string>>();
        set => SetPropertyValue(value);
    }
    public Expression<Func<string>> ValueExpression {
        get => GetPropertyValue<Expression<Func<string>>>();
        set => SetPropertyValue(value);
    }
    public override Type ComponentType => typeof(InputText);
}
```  

## Property Editor

1. Create a `BlazorPropertyEditorBase` descendant and name it _CustomStringPropertyEditor_. Apply 
a @DevExpress.ExpressApp.Editors.PropertyEditorAttribute to it and set its parameters to `string` and `false`. These values specify that you can choose this Property Editor in the [Model Editor](xref:112582) for any string property without making this the default editor for the property..
2. Override the `CreateComponentModel` method, create the `InputTextModel` instance, and set it up.
3. Override the `ReadValueCore` and `GetControlValueCore` methods to set and retrieve the value of the underlying component.
4. Override the `ApplyReadOnly` method to manage the read-only state.

**File**: _MySolution.Blazor.Server\Editors\CustomStringPropertyEditor.cs_

```csharp
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Model;
using Microsoft.AspNetCore.Components;  

namespace YourSolutionName.Blazor.Server.Editors;  

[PropertyEditor(typeof(string), false)]
public class CustomStringPropertyEditor : BlazorPropertyEditorBase {
    public CustomStringPropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
    public override InputTextModel ComponentModel => (InputTextModel)base.ComponentModel;
    protected override IComponentModel CreateComponentModel() {
        var model = new  InputTextModel();
        model.ValueExpression = () => model.Value;
        model.ValueChanged = EventCallback.Factory.Create<string>(this, value => {
            model.Value = value;
            OnControlValueChanged();
            WriteValue();
        });
        return model;
    }
    protected override void ReadValueCore() {
        base.ReadValueCore();
        ComponentModel.Value = (string)PropertyValue;
    }
    protected override object GetControlValueCore() => ComponentModel.Value;
    protected override void ApplyReadOnly() {
        base.ApplyReadOnly();
        ComponentModel?.SetAttribute("readonly", !AllowEdit);
    }
}
```

Rebuild your solution and invoke the Model Editor for the ASP.NET Core Blazor application project (_MySolution.Blazor.Server_). Navigate to the required **BOModel** | _**\<Class>**_ | **OwnMembers** | _**\<Member>**_ node and set the node's [PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property to `CustomStringPropertyEditor`.

You can also set this Property Editor for a specific View only. To do this, specify the [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node's `PropertyEditorType` property.

> [!NOTE]
> The built-in Component Model handles the Component's `ValueChanged` event (`TextChanged`, `DateChanged`, `TimeChanged`, and so on) and automatically reads and writes the Component's Value (Text, Date, Time, and so on). For example, an implementation of a property editor based on `DxTextBoxModel` may look like this:
>
> ```csharp
> using DevExpress.ExpressApp.Blazor.Components.Models;
> using DevExpress.ExpressApp.Blazor.Editors;
> using DevExpress.ExpressApp.Editors;
> using DevExpress.ExpressApp.Model;
> 
> [PropertyEditor(typeof(string), false)]
> public class CustomStringPropertyEditor : BlazorPropertyEditorBase {
>     public CustomStringPropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
>     public override DxTextBoxModel ComponentModel => (DxTextBoxModel)base.ComponentModel;
>     protected override IComponentModel CreateComponentModel() => new DxTextBoxModel();
> }
> ```

## Access XafApplication and ObjectSpace to Query and Manipulate Data (Perform CRUD Operations)

A custom Property Editor may require access to the application or the View ObjectSpace object. If so, implement the `IComplexViewItem` interface as shown in the following topic: @DevExpress.ExpressApp.Editors.IComplexViewItem.

Use the [IComplexViewItem.Setup](xref:DevExpress.ExpressApp.Editors.IComplexViewItem.Setup(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.XafApplication)) method to get the @DevExpress.ExpressApp.XafApplication and @DevExpress.ExpressApp.IObjectSpace objects. The @DevExpress.ExpressApp.IObjectSpace object contains methods to access the application database.

## Display a Custom Component in a List View

The InputText component from the above example will be rendered in Detail Views and in List Views during inline editing. To specify a component that your custom Property Editor should render in regular List View cells, override the `BlazorPropertyEditorBase.CreateViewComponentCore` method.

**File:**  _MySolution.Blazor.Server\CustomStringPropertyEditor.cs_

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Editors;
using Microsoft.AspNetCore.Components;

namespace YourSolutionName.Blazor.Server.Editors;

[PropertyEditor(typeof(string), false)]
public class CustomStringPropertyEditor : BlazorPropertyEditorBase {
    // ...
    protected override RenderFragment CreateViewComponentCore(object dataContext) {
        InputTextModel componentModel = new InputTextModel();
        componentModel.Value = (string)this.GetPropertyValue(dataContext);
        componentModel.ValueExpression = () => componentModel.Value;
        componentModel.SetAttribute("readonly", true);
        return  componentModel.GetComponentContent();
    }
}
```
***

The image below demonstrates the result.

![|XAF ASP.NET Core Blazor Custom Component-Based String Property Editor in a List View, DevExpress](~/images/xaf-blazor-custom-component-based-property-editor-devexpress.png)
