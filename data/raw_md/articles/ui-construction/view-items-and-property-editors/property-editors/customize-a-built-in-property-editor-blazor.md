---
uid: "402188"
title: 'Customize a Built-in Property Editor (Blazor)'
owner: Yekaterina Kiseleva
seealso:
  - linkId: "113104"
  - linkId: "113097"
---
# Customize a Built-in Property Editor (Blazor)

This topic describes two options you can use to customize a built-in XAF Property Editor for ASP.NET Core Blazor applications (refer to the following topic to see a similar example for WinForms: [How to: Customize a Built-in Property Editor (WinForms)](xref:113104)). This example displays the calendar and clock in **DateTimePropertyEditor**:

![BlazorCalendarPropertyEditor](~/images/BlazorCalendarPropertyEditor.png)

## Customize a Built-in Property Editor in a Controller 

Create a new [Controller](xref:112621) in the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_). To customize the Property Editor's control, override the `OnActivated` method and use the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl* method.

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
// ...
public class CustomizeDateEditorController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<DateTimePropertyEditor>(this, editor => {
            editor.ComponentModel.TimeSectionVisible = true;
        });
    }
}
```

***

## Create a Built-in Property Editor Descendant

Use this solution if you want to replace the default Property Editor with a custom editor for specific business object properties in the Model Editor. 

1. Inherit from the `DateTimePropertyEditor` class in the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_). [!include[PublicEditor](~/templates/publiceditor111797.md)] Override the `OnControlCreated` method to customize the Property Editor's control. To specify that the Property Editor can be used for the `DateTime` type properties, apply the [](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute) attribute.

    # [C#](#tab/tabid-csharp1)

    ```csharp
    using DevExpress.ExpressApp.Blazor.Editors;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Model;
    // ...
    [PropertyEditor(typeof(DateTime), false)]
    public class CustomDateTimePropertyEditor : DateTimePropertyEditor {
        public CustomDateTimePropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
        protected override void OnControlCreated() {
            base.OnControlCreated();
            ComponentModel.TimeSectionVisible = true;
        }
    }
    ```
    ***

2. To use this Property Editor for a specific property, double-click the _MySolution\Blazor.Server\Model.xafml_ file and run the [Model Editor](xref:112582) in the ASP.NET Core Blazor project. Set [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) of the required **OwnMember** or **ViewItem** node to `CustomDateTimePropertyEditor`.

    > [!TIP]
    > [!include[DefaultEditor](~/templates/defaulteditor111198.md)]

[!include[AdjustFormatting](~/templates/adjustformatting111199.md)]

## Handle Control Events

[!include[blazor-handle-razor-component-events](~/templates/blazor-handle-razor-component-events.md)]

[`CustomizeViewItemControl`]: xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0})