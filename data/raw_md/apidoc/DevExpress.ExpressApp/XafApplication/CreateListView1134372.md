---
uid: DevExpress.ExpressApp.XafApplication.CreateListView(DevExpress.ExpressApp.IObjectSpace,System.Type,System.Boolean)
name: CreateListView(IObjectSpace, Type, Boolean)
type: Method
summary: Creates a [List View](xref:112611) used for the objects of the specified type, by default.
syntax:
  content: public ListView CreateListView(IObjectSpace objectSpace, Type objectType, bool isRoot)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space used to retrieve objects from the database to the created List View's Collection Source.
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object specifying the business object type.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created List View is independent and owns the Object Space passed using the _objectSpace_ parameter; **false** if the created List View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.ListView
    description: A [](xref:DevExpress.ExpressApp.ListView) object used to display the collection of _objectType_ objects.
seealso: []
---
If you need to create a [List View](xref:112611#list-view) using the information specified in the [Application Model](xref:112580), use other **CreateListView** method overloads.

[!include[View_isRoot](~/templates/view_isroot111355.md)]

[!include[CreateObjectSpace_Note](~/templates/createobjectspace_note111363.md)]

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
        IObjectSpace newObjectSpace = Application.CreateObjectSpace(objectType);
        e.View = Application.CreateListView(newObjectSpace, objectType, true);
    }
}
```
***
