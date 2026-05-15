---
uid: DevExpress.Persistent.Base.LookupEditorModeAttribute
name: LookupEditorModeAttribute
type: Class
summary: Specifies the mode of the target business class property's Lookup Property Editor.
syntax:
  content: 'public class LookupEditorModeAttribute : ModelExportedValuesAttribute'
seealso:
- linkId: DevExpress.Persistent.Base.LookupEditorModeAttribute._members
  altText: LookupEditorModeAttribute Members
- linkId: 112925
---
XAF uses Lookup Property Editors to display business class properties based on the `BaseObject` type. The drop-down frame of this Property Editor contains a List View that displays all existing objects of the specified type. To enable the **Search** function for a specific property, apply the `LookupEditorMode` attribute to this property's declaration.

[!include[lookupeditormodeattribute-example](~/templates/lookupeditormodeattribute-example.md)]

To review all available attribute parameter values, refer to the following topic: [LookupEditorModeAttribute.Mode](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute.Mode).

You can also specify the editor mode in the [Model Editor](xref:112582). First, locate the required node: **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_**. Second, modify the following property: [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode).

# [C#](#tab/tabid-csharp)

```csharp
// ...
public class Contact : Person, IMapsMarker {
    // ...
    [LookupEditorMode(LookupEditorMode.AllItemsWithSearch)]
    public Department Department {
       // ...
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Persistent.Base

Public Class Contact
    Inherits Person
    Implements IMapsMarker
    ' ...
    <LookupEditorMode(LookupEditorMode.AllItemsWithSearch)>
    Public Property Department() As Department
       ' ...
```

***

See the attribute's [LookupEditorModeAttribute.Mode](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute.Mode) property description to learn about the available values you can pass as the _mode_ parameter.

The value of the **LookupEditorMode** attribute's _mode_ parameter is set for the [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. You can set the required value for this property directly in the Application Model via the [Model Editor](xref:112582).
