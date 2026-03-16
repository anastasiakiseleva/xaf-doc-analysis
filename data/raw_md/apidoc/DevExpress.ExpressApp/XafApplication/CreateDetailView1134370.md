---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.String,System.Boolean)
name: CreateDetailView(IObjectSpace, String, Boolean)
type: Method
summary: Creates a [Detail View](xref:112611) based on information from the [Application Model](xref:112580)'s Views | DetailView node specified by the _detailViewID_ parameter.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, string detailViewID, bool isRoot)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the new Detail View [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: detailViewID
    type: System.String
    description: A string that represents an identifier of the [Application Model](xref:112580) node that serves as an information source for creating a new Detail View.
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
Use this method to create a [Detail View](xref:112611#detail-view) that is not bound to an object. You can set an object separately using the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.

[!include[CreateDetailView_detailViewID](~/templates/createdetailview_detailviewid111364.md)]

[!include[View_isRoot](~/templates/view_isroot111355.md)]

[!include[CreateObjectSpace_Note](~/templates/createobjectspace_note111363.md)]

The example below demonstrates how to open an object's [Detail View](xref:112611#detail-view) via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
//...
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
            Type objectType = currentObject.GetType();
            string detailViewId = Application.GetDetailViewId(objectType);
            DetailView createdView = Application.CreateDetailView(objectSpace, detailViewId, true);
            createdView.CurrentObject = currentObject;
            e.View = createdView;
        }
        else {
            objectSpace.Dispose();
        }
    }
}
```
***