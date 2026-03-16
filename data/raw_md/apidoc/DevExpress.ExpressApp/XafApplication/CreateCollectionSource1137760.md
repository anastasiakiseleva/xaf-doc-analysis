---
uid: DevExpress.ExpressApp.XafApplication.CreateCollectionSource(DevExpress.ExpressApp.IObjectSpace,System.Type,System.String,DevExpress.ExpressApp.CollectionSourceDataAccessMode,DevExpress.ExpressApp.CollectionSourceMode)
name: CreateCollectionSource(IObjectSpace, Type, String, CollectionSourceDataAccessMode, CollectionSourceMode)
type: Method
summary: Creates a Collection Source for a specific [List View](xref:112611).
syntax:
  content: public CollectionSourceBase CreateCollectionSource(IObjectSpace objectSpace, Type objectType, string listViewId, CollectionSourceDataAccessMode dataAccessMode, CollectionSourceMode mode)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that represents an Object Space for the objects retrieved to the created Collection Source.
  - id: objectType
    type: System.Type
    description: The Type object that represents the type of the objects that will be retrieved to the created Collection Source.
  - id: listViewId
    type: System.String
    description: A string value representing the target List View's identifier.
  - id: dataAccessMode
    type: DevExpress.ExpressApp.CollectionSourceDataAccessMode
    description: The [](xref:DevExpress.ExpressApp.CollectionSourceDataAccessMode) enumeration value that specifies the [data access mode](xref:113683)
  - id: mode
    type: DevExpress.ExpressApp.CollectionSourceMode
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceMode) enumeration value specifying the Collection Source's mode of operation. This value is set to the [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property.
  return:
    type: DevExpress.ExpressApp.CollectionSourceBase
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceBase) object that represents the Collection Source of objects whose type is specified by the _objectType_ parameter.
seealso: []
---
