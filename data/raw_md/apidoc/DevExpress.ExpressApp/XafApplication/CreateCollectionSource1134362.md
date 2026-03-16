---
uid: DevExpress.ExpressApp.XafApplication.CreateCollectionSource(DevExpress.ExpressApp.IObjectSpace,System.Type,System.String)
name: CreateCollectionSource(IObjectSpace, Type, String)
type: Method
summary: Creates a collection source for a specified [List View](xref:112611).
syntax:
  content: public CollectionSourceBase CreateCollectionSource(IObjectSpace objectSpace, Type objectType, string listViewId)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that represents an Object Space for the objects retrieved to the created collection source.
  - id: objectType
    type: System.Type
    description: The Type object that represents the type of the objects that will be retrieved to the created collection source.
  - id: listViewId
    type: System.String
    description: A string value representing the target List View's identifier.
  return:
    type: DevExpress.ExpressApp.CollectionSourceBase
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceBase) object that represents the collection source of objects whose type is specified by the _objectType_ parameter.
seealso: []
---
This method creates a collection source for the View specified by the _listViewID_ parameter. Generally, you can create it directly via the constructor of the required collection source type.

This method can be currently used only in Windows Forms applications which utilize the **XtraGrid** control for displaying List Views.

By default, this method is used to retrieve objects for the following List Views:

* Lookup Property Editor's List View;
* List View in the pop-up Window invoked by the Link or Unlink Action.

The [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property of the created CollectionSource is set to [XafApplication.DefaultCollectionSourceMode](xref:DevExpress.ExpressApp.XafApplication.DefaultCollectionSourceMode) property value.