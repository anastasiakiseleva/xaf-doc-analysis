---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.Model.IModelDetailView,System.Boolean)
name: CreateDetailView(IObjectSpace, IModelDetailView, Boolean)
type: Method
summary: Creates a [Detail View](xref:112611) based on information from the [Application Model](xref:112580)'s Views | DetailView node specified by the _modelDetailView_ parameter.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, IModelDetailView modelDetailView, bool isRoot)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which is used to work with the new Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: modelDetailView
    type: DevExpress.ExpressApp.Model.IModelDetailView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelDetailView) object that represents the Application Model node that serves as an information source for creating a new Detail View.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created Detail View is independent and owns the Object Space passed using the _objectSpace_ parameter; **false**, if the created Detail View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [Detail View](xref:112611) that does not represent any object.
seealso:
- linkId: "118760"
- linkId: "112803"
---
Use this method to create a [Detail View](xref:112611#detail-view) which is not bound to an object. You can set an object separately using the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.

> [!NOTE]
> Do not use another View's [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) for the creation of a new root View in it. Instead, create a new Object Space using the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method for the new root View.

[!include[CreateDetailView_modelDetailView](~/templates/createdetailview_modeldetailview111361.md)]

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
        if(View.CurrentObject != null) {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
            IModelClass modelClass = Application.FindModelClass(View.CurrentObject.GetType());
            IModelDetailView defaultDetailView = modelClass.DefaultDetailView;
            e.View = Application.CreateDetailView(objectSpace, defaultDetailView, true);
        }
    }
}
```
***