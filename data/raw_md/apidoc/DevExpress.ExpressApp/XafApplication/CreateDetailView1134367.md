---
uid: DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.ExpressApp.View)
name: CreateDetailView(IObjectSpace, Object, View)
type: Method
summary: Creates a [Detail View](xref:112611) for a specified object based on information on the source View.
syntax:
  content: public DetailView CreateDetailView(IObjectSpace objectSpace, object obj, View sourceView)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space which is used to work with the new Detail View [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject). This object is assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.
  - id: obj
    type: System.Object
    description: An object which is represented by the new Detail View. This object is assigned to the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property.
  - id: sourceView
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object that represents the [View](xref:112611) in which the command to show the new Detail View has been performed.
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [Detail View](xref:112611) that represents the object passed as the _obj_ parameter.
seealso:
- linkId: "118760"
- linkId: "112803"
---
If the new [Detail View](xref:112611#detail-view)'s [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) is different from the source View's Object Space, its [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property is set to **true**. Note that certain [Controllers](xref:112621) and [Actions](xref:112622) are deactivated if the **IsRoot** property is set to **false**. To avoid this, use the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) or [XafApplication.CreateNestedObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateNestedObjectSpace(DevExpress.ExpressApp.IObjectSpace)) method to create a new Object Space, and pass this Object Space as the _objectSpace_ parameter.

[!include[CreateDetailView_obj](~/templates/createdetailview_obj111356.md)]

Use this overload when you need information on the source View to determine what Detail View to create. Pass the source View as the _sourceView_ parameter. If the source View is a [](xref:DevExpress.ExpressApp.DetailView), the method uses information from the [Application Model](xref:112580)'s **Views** | _**&lt;View&gt;**_ node to create a new Detail View. If the source View is a List View, the method retrieves the Application Model's node information from the List View's [ListView.DetailViewId](xref:DevExpress.ExpressApp.ListView.DetailViewId) property.

The example below demonstrates how to open an object's [Detail View](xref:112611#detail-view) via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
//...
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
            e.View = Application.CreateDetailView(objectSpace, currentObject, View);
        }
        else {
            objectSpace.Dispose();
        }
    }
}
```
***