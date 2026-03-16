---
uid: DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName
name: ControlTypeName
type: Property
summary: Specifies the type of the control that displays a Control Detail Item.
syntax:
  content: |-
    [Required]
    string ControlTypeName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the type of the control that displays a Control Detail Item.
seealso:
- linkId: DevExpress.ExpressApp.Layout.ControlViewItem
---
The @DevExpress.ExpressApp.Layout.ControlViewItem loads the specified control type dynamically by its name at runtime. Make sure your application loads the type assembly before it shows a `View` with this `ControlViewItem`. Otherwise, the following exception may occur:

```Console
TypeWasNotFoundException - "The '{ControlTypeName}' type was not found". 
```

To load the type assembly, create any lightweight object from the assembly type at startup:

# [C#](#tab/tabid-csharp)
```csharp
var pivotGridAssemblyInitializer = new PivotGridField();
```
***

Alternatively, add a control to a `UserControl`, as shown in the following topics:

- [](xref:404698)
- [](xref:114159)