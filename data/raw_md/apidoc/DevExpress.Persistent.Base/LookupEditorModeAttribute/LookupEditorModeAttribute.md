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
---
By default, an **Object** type business class property is displayed via a Lookup Property Editor. The drop-down frame of this Property Editor contains a List View that displays all existing objects of the specified type. In addition, this frame can contain a **Search** function, so that end-users can easily find a particular object in that List View. Apply the **LookupEditorMode** attribute to a property, to specify whether the Lookup Editor should contain the **Search** function. 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;

// ...
public class Contact : Person, IMapsMarker {
    // ...
    [LookupEditorMode(LookupEditorMode.AllItemsWithSearch)]
    public Department Department {
       // ...

```
***

See the attribute's [LookupEditorModeAttribute.Mode](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute.Mode) property description to learn about the available values you can pass as the _mode_ parameter.

The value of the **LookupEditorMode** atribute's _mode_ parameter is set for the [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. You can set the required value for this property directly in the Application Model via the [Model Editor](xref:112582).