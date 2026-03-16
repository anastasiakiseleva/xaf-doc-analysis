---
uid: DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem
name: BlazorControlViewItem
type: Class
summary: A container for custom ASP.NET Core Blazor components displayed in a Detail View.
syntax:
  content: 'public class BlazorControlViewItem : ControlViewItem'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem._members
  altText: BlazorControlViewItem Members
- linkId: "113653"
- linkId: "404700"
- linkId: "404698"
---

The following code snippet uses `BlazorControlViewItem` to create a custom component:

**File:** _CS\MainDemo.Blazor.Server\Editors\ButtonComponent.razor_

```Razor{8}
@using DevExpress.Blazor
@using DevExpress.ExpressApp
@using DevExpress.ExpressApp.Blazor.Editors

<DxButton Text="Click me!" Click=@ClickFromUI />

@code {
    [CascadingParameter] public BlazorControlViewItem ViewItem { get; set; }

    void ClickFromUI() {
        ViewItem.Application.ShowViewStrategy.ShowMessage("Action is executed!");
    }
}
```

When you add the custom component to a Detail View, specify the component type as the **ControlTypeName** property value in the Model Editor:

![XAF Add A Control Detail Item in the Model Editor, DevExpress](~/images/xaf-model-editor-add-controldetailitem-devexpress.png)

For more information about custom ASP.NET Core Blazor View Items, refer to the following topics:
* [](xref:113653)
* [](xref:404698)