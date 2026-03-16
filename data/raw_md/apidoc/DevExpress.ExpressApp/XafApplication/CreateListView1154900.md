---
uid: DevExpress.ExpressApp.XafApplication.CreateListView(DevExpress.ExpressApp.Model.IModelListView,DevExpress.ExpressApp.CollectionSourceBase,System.Boolean,DevExpress.ExpressApp.Editors.ListEditor)
name: CreateListView(IModelListView, CollectionSourceBase, Boolean, ListEditor)
type: Method
summary: For internal use.
syntax:
  content: public ListView CreateListView(IModelListView modelListView, CollectionSourceBase collectionSource, bool isRoot, ListEditor listEditor)
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
  - id: listEditor
    type: DevExpress.ExpressApp.Editors.ListEditor
    description: A [](xref:DevExpress.ExpressApp.Editors.ListEditor) to be used in the created List View.
  return:
    type: DevExpress.ExpressApp.ListView
    description: A [](xref:DevExpress.ExpressApp.ListView) object used to display the collection of objects specified by the _collectionSource_ parameter.
seealso: []
---
