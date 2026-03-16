---
uid: DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Visibility
name: Visibility
type: Property
summary: Specifies the visibility of UI elements affected by a conditional appearance rule.
syntax:
  content: ViewItemVisibility? Visibility { get; set; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.ExpressApp.Editors.ViewItemVisibility}
    description: A **Nullable\<**[](xref:DevExpress.ExpressApp.Editors.ViewItemVisibility)**>** enumeration value specifying the visibility of UI elements affected by a conditional appearance rule.
seealso:
- linkId: "113286"
- linkId: "114008"
- linkId: "113221"
---
For details on how the **Visibility** property affects the UI, see the [AppearanceAttribute.Visibility](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility) member description.

To change the **Visibility** value in code, [access the required Property Editor instance](xref:402153) and then cast it to the [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance) type. Most of built-in Property Editors support this interface.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Editors;
// ...
((IAppearanceVisibility)thePropertyEditor).Visibility = ViewItemVisibility.Hide;
```
***