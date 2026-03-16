---
uid: "404767"
title: Underlying Controls and Components Behind UI Elements (ASP.NET Core Blazor)
owner: Anastasiya Kisialeva
---
# Underlying Controls and Components Behind UI Elements (ASP.NET Core Blazor)

In XAF Blazor applications, the UI is built using Razor components. Component classes are usually Razor markup pages with a .razor file extension. The code snippet below demonstrates a custom Razor component:

```Razor
<DxSpinEdit @bind-Value="@Value" ShowSpinButtons="false" CssClass="my-custom-class"></DxSpinEdit>

@code {
    int Value { get; set; } = 10;
}
```

In this code snippet, you add a [DxSpinEdit\<T\>](xref:DevExpress.Blazor.DxSpinEdit`1) control to the markup, and specify the following parameters:
* [ShowSpinButtons](xref:DevExpress.Blazor.DxSpinEdit`1.ShowSpinButtons) - disables increment/decrement buttons.
* [CssClass](xref:DevExpress.Blazor.Base.DxDataEditor`1.CssClass) - adds a custom class to HTML elements rendered by the `DxSpinEdit` component.

`@bind-Value="@Value"` is responsible for the following functionality:
  - When XAF renders a `DxSpinEdit` component, its value is set to the `Value` property.
  - When you change the `DxSpinEdit` value in the UI, the `Value` property is updated.

See also:

* [Razor components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)
* [ASP.NET Core Blazor data binding](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)
* [ASP.NET Core Razor component lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)

You will rarely need to create custom components, but may need to customize built-in components. To do so, you do not need to modify markup code. Instead, use XAF component models - proxy objects that allow you to change the parameters of their respective components from anywhere in code.

For example, `DxSpinEditModel` is an object representation of the `DxSpinEdit` component. Each `DxSpinEditModel` property has a corresponding [DxSpinEdit](xref:DevExpress.Blazor.DxSpinEdit`1._members) property:

```csharp
public class DxSpinEditModel : ComponentModelBase {
    //
    public bool ShowSpinButtons {
        get => GetPropertyValue<bool>(true);
        set => SetPropertyValue(value);
    }
    public string CssClass {
        get => GetPropertyValue<string>();
        set => SetPropertyValue(value);
    }
}
```

To customize a property editor's component in an auto-generated XAF View, you need to work with the Component Model at runtime or in code:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public class AddCustomCssClassController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<NumericPropertyEditor>(this, editor => {
            editor.ComponentModel.ShowSpinButtons = false;
            editor.ComponentModel.CssClass += " my-custom-class";
        });
    }
}
```

You can use Component Models to customize visual appearance and behavior of Property Editors (such as DxTextBox, DxDateEdit, DxSpinEdit), List Editors (such as DxGrid, DxScheduler), navigation (such as DxAccordion, DxTreeView), DxToolbar, and other components in XAF ASP.NET Core Blazor applications.

A Component Model replicates all [parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components#component-parameters) of the related component. You can use these parameters to configure the underlying component before creation. However, the model does not allow you to access the current component state or call its methods directly.

Use the `ComponentInstance` property or handle the `ComponentInstanceCaptured` event to access the underlying component instance and its full API.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public partial class GridListEditorController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxGridListEditor editor) {
            editor.GridModel.ComponentInstanceCaptured += (s, e) => {
                e.ComponentInstance.CollapseAllGroupRows();
            };
        }
    }
}
```

See also:

* <xref:402188>
* <xref:402154>
* <xref:120092>
* <xref:112617>
* [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl#aspnet-core-blazor-specific-scenarios)

## A Base Class for Underlying XAF Blazor Components

`DevExpress.ExpressApp.Blazor.Components.Models.ComponentModelBase` is an abstract base class for all Component Models. Built-in Component Models replicate all [parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/) of the corresponding component (**default**). However, when you create a custom Component Model, you can include only necessary parameters.

In most cases, you can use the `SetPropertyValue` and `GetPropertyValue` methods to add the required component parameters to your Component Model class:

```csharp
using System.Linq.Expressions;
using DevExpress.ExpressApp.Blazor.Components.Models;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Forms;

namespace YourSolutionName.Blazor.Server.Editors;

public class InputTextModel : ComponentModelBase {
    public string Value {
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

The `ComponentType` property is described in the next section.

The following methods and properties can also be useful:

`ComponentModelBase.SetAttribute`
:   This method sets additional attributes for the component (an equivalent of the [ParameterAttribute.CaptureUnmatchedValues](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.parameterattribute.captureunmatchedvalues) property). For more information, refer to the following topic: [Arbitrary attributes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/splat-attributes-and-arbitrary-parameters).
    ```csharp
    public void SetAttribute(string name, object value)
    ```

    Example of usage:
    
    ```csharp
    InputModel model = new InputModel();
    model.SetAttribute("title", "A tooltip text");
    ```

    ![|XAF ASP.NET Core Blazor ComponentModel SetAttribute Method, DevExpress](~/images/xaf-blazor-componentmodel-setattribute-devexpress.png)


`ComponentModelBase.Attributes`
:   This property contains a list of additional attributes specified by the `ComponentModelBase.SetAttribute` method.

    ```csharp
    public IReadOnlyDictionary<string, object> Attributes { get; }
    ```

    Example of usage:

    ```Razor
    <InputText Value=@ComponentModel.Value
            @* --- *@
            @attributes=ComponentModel.Attributes />

    @code {
        [Parameter] public InputModel ComponentModel { get; set; }
    }
    ```

See also:

* [Manually Build a Render Tree (RenderTreeBuilder)](https://learn.microsoft.com/en-us/aspnet/core/blazor/advanced-scenarios)
* [](xref:402189)
* [](xref:403258)

## Component State Changes and Content Render

`ComponentModelBase` implements the `IComponentModel` and `IComponentModelRenderable` interfaces.

```csharp
namespace DevExpress.ExpressApp.Blazor.Components.Models;

public interface IComponentModel {
    event EventHandler Changed;
}
public interface IComponentModelRenderable : IComponentModel {
    Type ComponentType { get; }
}
```

The `IComponentModel.Changed` event is triggered every time a property of the Component Model changes. For example, when you call the `SetPropertyValue` method with a new value.

The `ComponentType` property is required to create a [RenderFragment](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.renderfragment) and render the underlying component.

Use the following extension method to create a `RenderFragment` of a component defined by the corresponding Component Model:

```csharp
namespace DevExpress.ExpressApp.Blazor.Components.Models;

public static class ComponentModelRenderer {
    public static RenderFragment GetComponentContent(this IComponentModelRenderable renderable, Action<object> addComponentReferenceCapture = default);
}
```

The following conditions must be met:

1. Component Model properties must have the same type and name as the related component's parameters.
2. The `ComponentType` property must return the component type that will be rendered.

A usage example of an extension method:

```csharp
using DevExpress.ExpressApp.Blazor.Components.Models;
// ...
var model = new InputTextModel();
// ...
RenderFragment inputTextContent = model.GetComponentContent();
```

`DevExpress.ExpressApp.Blazor.Components.ComponentModelObserver` is a component that wraps the main component and subscribes to the `ComponentModel.Changed` event. When the event is triggered, `ComponentModelObserver` calls the [StateHasChanged](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.componentbase.statehaschanged) method and re-renders itself and the child component.

In XAF:

```csharp
public class CustomViewItem : ViewItem, IComponentContentHolder {
    private RenderFragment componentContent;
    public InputTextModel ComponentModel { get; private set; }
    protected override object CreateControlCore() {
        ComponentModel = new InputTextModel();
        // ...
        return ComponentModel;
    }
    
    public RenderFragment ComponentContent {
        get {
            componentContent ??= ComponentModelObserver.Create(ComponentModel, ComponentModel.GetComponentContent());
            return componentContent;
        }
    }
    // ...
}
```

The following example shows a possible `ComponentContent` representation in Razor markup:
```Razor
<ComponentModelObserver ComponentModel="@ComponentModel">
    @ComponentModel.GetComponentContent()
</ComponentModelObserver>

@code {
    public InputModel ComponentModel { get; set; }
}
```

## Handle Component Events

[!include[BlazorHandleComponentEvents](~/templates/blazor-handle-razor-component-events.md)]
