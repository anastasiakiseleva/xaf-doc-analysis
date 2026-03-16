---
uid: DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode
name: DataAccessMode
type: Property
summary: Gets the mode used to access the [](xref:DevExpress.ExpressApp.CollectionSourceBase)'s collection.
syntax:
  content: public CollectionSourceDataAccessMode DataAccessMode { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.CollectionSourceDataAccessMode
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceDataAccessMode) enumeration value that specifies the mode used to access the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection).
seealso:
- linkId: DevExpress.ExpressApp.View.IsRoot
- linkId: "8398"
- linkId: "3726"
---
When you create a Collection Source in code, you can initialize the **DataAccessMode** property using a constructor with the _dataAccessMode_ parameter. To set this property to the required value in the [Model Editor](xref:112582), use the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node corresponding to the List View for which the current Collection Source is created.

[!include[DataAccessModes_Links](~/templates/dataaccessmodes_links111899.md)]