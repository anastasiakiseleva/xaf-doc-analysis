---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object)
name: CreateDetailView(IObjectSpace, Object)
type: Method
summary: Creates a [Detail View](xref:112611) based on information specified in the [Application Model](xref:112580) for the type of the specified object.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, object obj)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the new Detail View [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: obj
    type: System.Object
    description: An object which is represented by the new Detail View. This object is assigned to the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [Detail View](xref:112611) that represents the object passed as the _obj_ parameter.
seealso:
- linkId: "118760"
- linkId: "112803"
---
Use this method to create a [Detail View](xref:112611#detail-view) for the object specified by the _obj_ parameter. The information on the created Detail View is taken from the [Application Model](xref:112580)' node specified by the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) property of the corresponding [](xref:DevExpress.ExpressApp.Model.IModelClass) node.

[!include[CreateDetailView_obj](~/templates/createdetailview_obj111356.md)]

The Object Space specified in the _objectSpace_ parameter should not belong to another View. To pass an Object Space used by another (parent) View to the created DetailView, either use the **CreateDetailView** method overload with the _isRoot_ parameter, or set the **IsRoot** property of the created DetailView to **false**.

The example below demonstrates how to open an object's [Detail View](xref:112611#detail-view) via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class ShowDetailViewController : ObjectViewController<ListView, Person> {
    public ShowDetailViewController() {
        PopupWindowShowAction showDetailViewAction = new PopupWindowShowAction(
            this, "ShowDetailView", PredefinedCategory.Edit);
        showDetailViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        showDetailViewAction.CustomizePopupWindowParams += ShowDetailViewAction_CustomizePopupWindowParams;
    }
    private void ShowDetailViewAction_CustomizePopupWindowParams(
        object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
        Object currentObject = objectSpace.GetObject(View.CurrentObject);
        if(currentObject != null) {
            e.View = Application.CreateDetailView(objectSpace, currentObject);
        }
        else {
            objectSpace.Dispose();
        }
    }
}
```
***