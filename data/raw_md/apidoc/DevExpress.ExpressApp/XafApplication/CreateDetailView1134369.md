---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.Model.IModelDetailView,System.Boolean,System.Object)
name: CreateDetailView(IObjectSpace, IModelDetailView, Boolean, Object)
type: Method
summary: Creates a [Detail View](xref:112611) for the specified object with settings from the [Application Model](xref:112580)'s Views | DetailView node specified by the _modelDetailView_ parameter.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, IModelDetailView modelDetailView, bool isRoot, object obj)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the new Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: modelDetailView
    type: DevExpress.ExpressApp.Model.IModelDetailView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelDetailView) object that represents the Application Model node that serves as an information source for creating a new Detail View.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created Detail View is independent and owns the Object Space passed using the _objectSpace_ parameter; **false**, if the created Detail View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
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
Use this method to create and initialize a [Detail View](xref:112611#detail-view) according to values passed as parameters.

[!include[CreateDetailView_modelDetailView](~/templates/createdetailview_modeldetailview111361.md)]

[!include[View_isRoot](~/templates/view_isroot111355.md)]

[!include[CreateDetailView_obj](~/templates/createdetailview_obj111356.md)]

[!include[CreateObjectSpace_Note](~/templates/createobjectspace_note111363.md)]

The example below demonstrates how to open an object's [Detail View](xref:112611#detail-view) via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Model;
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
            IModelClass modelClass = Application.FindModelClass(currentObject.GetType());
            IModelDetailView defaultDetailView = modelClass.DefaultDetailView;
            e.View = Application.CreateDetailView(objectSpace, defaultDetailView, true, currentObject);
        }
        else {
            objectSpace.Dispose();
        }
    }
}
```
***
