---
uid: DevExpress.ExpressApp.XafApplication.CreateListView(System.Type,System.Boolean)
name: CreateListView(Type, Boolean)
type: Method
summary: Creates a [List View](xref:112611) used for the objects of the specified type, by default.
syntax:
  content: public ListView CreateListView(Type objectType, bool isRoot)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object specifying the business object type.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created List View is independent and owns the Object Space assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property; **false**, if the created List View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.ListView
    description: A [](xref:DevExpress.ExpressApp.ListView) object used to display the collection of _objectType_ objects.
seealso: []
---
With this **CreateListView** overload, the [Object Space](xref:113707) passed to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property is created automatically.

If you need to create a [List View](xref:112611#list-view) using the information specified in the [Application Model](xref:112580), use other **CreateListView** method overloads.

Use this method to create and initialize a [List View](xref:112611#list-view) according to values passed as parameters.

[!include[View_isRoot](~/templates/view_isroot111355.md)]

The following example creates a [List View](xref:112611#list-view) and displays it via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class ShowListViewController : WindowController {
    public ShowListViewController() {
        PopupWindowShowAction showListViewAction = new PopupWindowShowAction(
            this, "ShowListView", PredefinedCategory.Edit);
        showListViewAction.CustomizePopupWindowParams += ShowListViewAction_CustomizePopupWindowParams;
    }
    private void ShowListViewAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        Type objectType = typeof(Person);
        e.View = Application.CreateListView(objectType, true);
    }
}
```
***