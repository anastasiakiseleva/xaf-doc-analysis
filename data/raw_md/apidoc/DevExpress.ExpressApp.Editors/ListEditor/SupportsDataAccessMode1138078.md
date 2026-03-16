---
uid: DevExpress.ExpressApp.Editors.ListEditor.SupportsDataAccessMode(DevExpress.ExpressApp.CollectionSourceDataAccessMode)
name: SupportsDataAccessMode(CollectionSourceDataAccessMode)
type: Method
summary: Determines whether or not the given [data access mode](xref:113683) is supported by the [](xref:DevExpress.ExpressApp.Editors.ListEditor).
syntax:
  content: public virtual bool SupportsDataAccessMode(CollectionSourceDataAccessMode dataAccessMode)
  parameters:
  - id: dataAccessMode
    type: DevExpress.ExpressApp.CollectionSourceDataAccessMode
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceDataAccessMode) enumeration value that specifies the data access mode.
  return:
    type: System.Boolean
    description: '**true**, if the specified mode is supported, otherwise - **false**.'
seealso: []
---
In custom [List Editors](xref:113189), this method returns **true** for all data access modes. Override **SupportsDataAccessMode** in your custom List Editor to specify the supported modes.

# [C#](#tab/tabid-csharp)

```csharp
public override Boolean SupportsDataAccessMode(CollectionSourceDataAccessMode dataAccessMode) {
    return (dataAccessMode == CollectionSourceDataAccessMode.Client);
}
```
***