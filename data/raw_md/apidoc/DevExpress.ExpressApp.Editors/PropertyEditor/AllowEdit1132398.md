---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit
name: AllowEdit
type: Property
summary: Provides access to a collection of reason/value pairs used to make a [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) read-only/editable.
syntax:
  content: public BoolList AllowEdit { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.BoolList
    description: A [](xref:DevExpress.ExpressApp.Utils.BoolList) object that represents a collection of key/value elements.
seealso: []
---
The example below demonstrates how to make a **Contact** object's **FirstName** field read-only.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
// ...
public class FirstNameController : ObjectViewController<DetailView, MainDemo.Module.BusinessObjects.Contact> {
    protected override void OnActivated() {
        PropertyEditor firstNamePropertyEditor = (PropertyEditor)View.FindItem("FirstName");
        firstNamePropertyEditor.AllowEdit["Read-Only"] = false;
    }
}

```
***

The **AllowEdit** is a collection whose elements represent a pair of string and Boolean values. The string value specifies a reason and the Boolean value specifies whether to make the Property Editor editable for this reason. A Property Editor is considered read-only if at least one of the **AllowEdit** collection elements contains a **false** value.

To determine whether a Property Editor is currently read-only, use the **AllowEdit** property in a conditional expression. Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object returned by **AllowEdit**.

# [C#](#tab/tabid-csharp)

```csharp
PropertyEditor myEditor;
//...
BoolList editableList = myEditor.AllowEdit;
if (editableList) {
    //...
}
```
***

To make an editable Property Editor read-only, use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method of the **BoolList** object returned by this property. Pass the reason for making the Property Editor read-only as the first parameter, and **false**, or a Boolean expression, as the second parameter. Alternatively, you can use the **[_key_]** operator of the **BoolList** object returned by the **AllowEdit** property, to get or set the specified key's value.

# [C#](#tab/tabid-csharp)

```csharp
PropertyEditor myEditor;
//...
BoolList editableList = myEditor.AllowEdit;
editableList["myKey"] = false;
```
***

To make a read-only Property Editor editable, use the [BoolList.RemoveItem](xref:DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)) method of the **BoolList** object returned by this property. Pass the key (reason) of the item with the **false** value. If this is a single item that has the false value, the Property Editor will become editable. Alternatively, you can use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method by passing the key, which has false as a value, and true as a new value for it.

# [C#](#tab/tabid-csharp)

```csharp
PropertyEditor myEditor;
//...
BoolList editableList = myEditor.AllowEdit;
editableList["disablingKey"] = true;
```
***

When a Property Editor's read-only state is changed, the [PropertyEditor.AllowEditChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEditChanged) event is raised.