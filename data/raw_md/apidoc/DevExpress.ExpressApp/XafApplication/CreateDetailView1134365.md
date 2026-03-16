---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object,System.Boolean)
name: CreateDetailView(IObjectSpace, Object, Boolean)
type: Method
summary: Creates a [](xref:DevExpress.ExpressApp.DetailView) for the specified object and initializes its properties.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, object obj, bool isRoot)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the new Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: obj
    type: System.Object
    description: An object which is represented by the new Detail View. This object is assigned to the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created Detail View is independent and owns the Object Space passed using the _objectSpace_ parameter; **false**, if the created Detail View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [Detail View](xref:112611) that represents the object passed as the _obj_ parameter.
seealso:
- linkId: "118760"
- linkId: "112803"
---
Use this method to create a [Detail View](xref:112611#detail-view) for the object specified by the _obj_ parameter. The information on the created Detail View is taken from the [Application Model](xref:112580)' node specified by the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) property of the corresponding [](xref:DevExpress.ExpressApp.Model.IModelClass) node.

[!include[CreateDetailView_obj](~/templates/createdetailview_obj111356.md)]

[!include[View_isRoot](~/templates/view_isroot111355.md)]

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
            e.View = Application.CreateDetailView(objectSpace, currentObject, true);
        }
        else {
            objectSpace.Dispose();
        }
    }
}
```
***
