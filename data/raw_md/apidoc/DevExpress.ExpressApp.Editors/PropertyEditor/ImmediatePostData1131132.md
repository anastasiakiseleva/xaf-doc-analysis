---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ImmediatePostData
name: ImmediatePostData
type: Property
summary: Specifies whether the property editor's control value should be passed to the property of a bound object as soon as possible when the value is changed by user. For instance, it allows you to enforce updating other displayed values that are calculated based on the current property.
syntax:
  content: public bool ImmediatePostData { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the property editor's control value should be passed as soon as possible; otherwise, **false**."
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImmediatePostData
---
This property derives its default value from [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] | **ImmediatePostData** and [!include[Node_Views_ListView_Columns_Column](~/templates/node_views_listview_columns_column111388.md)] | **ImmediatePostData**.

Refer to the [](xref:DevExpress.Persistent.Base.ImmediatePostDataAttribute) topic for details.

The example below demonstrates how to apply **ImmediatePostData** to **FirstName** and **LastName**. This causes the calculated **FullName** field to update automatically in WinForms applications.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class FullNameController : ObjectViewController<DetailView, MainDemo.Module.BusinessObjects.Contact> {
    protected override void OnActivated() {
        StringPropertyEditor firstNameEditor = (StringPropertyEditor)View.FindItem("FirstName");
        StringPropertyEditor lastNameEditor = (StringPropertyEditor)View.FindItem("LastName");
        firstNameEditor.ImmediatePostData = true;
        lastNameEditor.ImmediatePostData = true;
    }
}

```
***