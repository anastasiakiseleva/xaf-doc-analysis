---
uid: DevExpress.ExpressApp.XafApplication.CreateListEditor(DevExpress.ExpressApp.CollectionSourceBase,DevExpress.ExpressApp.Model.IModelListView)
name: CreateListEditor(CollectionSourceBase, IModelListView)
type: Method
summary: Creates the [List Editor](xref:113189) which is specified in the appropriate [Application Model](xref:112580) node.
syntax:
  content: public ListEditor CreateListEditor(CollectionSourceBase collectionSource, IModelListView modelListView)
  parameters:
  - id: collectionSource
    type: DevExpress.ExpressApp.CollectionSourceBase
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceBase) object representing the Collection Source of the [List View](xref:112611) which is displayed via the new ListEditor object.
  - id: modelListView
    type: DevExpress.ExpressApp.Model.IModelListView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelListView) object representing the Application Model node that defines the List View for which a List Editor is created.
  return:
    type: DevExpress.ExpressApp.Editors.ListEditor
    description: An appropriate List Editor.
seealso: []
---
This method creates the List Editor of the type specified by the [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) property of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node which is passed as the info parameter. If the List View cannot be created, an exception is raised.

A List Editor can implement the [](xref:DevExpress.ExpressApp.Editors.IComplexListEditor) and/or **IProtectedContentEditor** interface. If the **IComplexListEditor** interface is implemented, its Setup method is called. If the **IProtectedContentEditor** interface is implemented, its **ProtectedContentText** property is set to the Application node's [IModelApplication.ProtectedContentText](xref:DevExpress.ExpressApp.Model.IModelApplication.ProtectedContentText) property value.

You may need to use this method if a custom Property Editor displays its value via a List View. In this instance, use the List View's constructor with the _listEditor_ parameter (see [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*)).