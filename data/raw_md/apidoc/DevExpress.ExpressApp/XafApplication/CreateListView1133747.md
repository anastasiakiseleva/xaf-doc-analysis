---
uid: DevExpress.ExpressApp.XafApplication.CreateListView(DevExpress.ExpressApp.Model.IModelListView,DevExpress.ExpressApp.CollectionSourceBase,System.Boolean)
name: CreateListView(IModelListView, CollectionSourceBase, Boolean)
type: Method
summary: Creates a [List View](xref:112611) based on the information from the [Application Model](xref:112580)'s node specified by the _modelListView_ parameter.
syntax:
  content: public ListView CreateListView(IModelListView modelListView, CollectionSourceBase collectionSource, bool isRoot)
  parameters:
  - id: modelListView
    type: DevExpress.ExpressApp.Model.IModelListView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelListView) object that represents the Application Model node that serves as an information source for creating a new List View.
  - id: collectionSource
    type: DevExpress.ExpressApp.CollectionSourceBase
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceBase) object that represents the storage for the object to be displayed by the new List View. This object is assigned to the [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource) property.
  - id: isRoot
    type: System.Boolean
    description: '**true**, if the created List View is independent and owns the Object Space assigned to the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property; **false**, if the created List View is nested to another root View that owns the Object Space. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  return:
    type: DevExpress.ExpressApp.ListView
    description: A [](xref:DevExpress.ExpressApp.ListView) object used to display the collection of objects specified by the _collectionSource_ parameter.
seealso: []
---
Use this method to create and initialize a [List View](xref:112611#list-view) according to values passed as parameters.

[!include[CreateListView_collectionSource](~/templates/createlistview_collectionsource111365_1130207.md)]

[!include[View_isRoot](~/templates/view_isroot111355.md)]

[!include[CreateObjectSpace_Note](~/templates/createobjectspace_note111363.md)]

The following example creates a [Lookup List View](xref:112611#list-view) and displays it via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Model;
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
        string listViewId = Application.FindLookupListViewId(objectType);
        IModelListView modelListView = (IModelListView)Application.FindModelView(listViewId);
        CollectionSourceBase collectionSource = Application.CreateCollectionSource(
            newObjectSpace, objectType, listViewId);
        e.View = Application.CreateListView(modelListView, collectionSource, true);
    }
}
```
***
