---
uid: DevExpress.ExpressApp.XafApplication.CreatePropertyCollectionSource(DevExpress.ExpressApp.IObjectSpace,System.Type,System.Object,DevExpress.ExpressApp.DC.IMemberInfo,System.String,System.Boolean,DevExpress.ExpressApp.CollectionSourceMode)
name: CreatePropertyCollectionSource(IObjectSpace, Type, Object, IMemberInfo, String, Boolean, CollectionSourceMode)
type: Method
summary: Creates a Collection Source for a nested List View that displays a collection property.
syntax:
  content: public PropertyCollectionSource CreatePropertyCollectionSource(IObjectSpace objectSpace, Type masterObjectType, object masterObject, IMemberInfo memberInfo, string listViewId, bool isServerMode, CollectionSourceMode mode)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space used to retrieve the object for the created Collection Source.
  - id: masterObjectType
    type: System.Type
    description: The type of the object whose collection property is about to be displayed.
  - id: masterObject
    type: System.Object
    description: An object whose collection property is about to be displayed.
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object that defines the collection property to be displayed.
  - id: listViewId
    type: System.String
    description: A string representing an identifier of the List View for which a Collection Source is created.
  - id: isServerMode
    type: System.Boolean
    description: '**true**, if all the data processing takes place on the database server side; **false**, if all the data processing takes place on the client side. This value is used to initialize the [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property of the created Collection Source.'
  - id: mode
    type: DevExpress.ExpressApp.CollectionSourceMode
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceMode) enumeration value specifying the Collection Source's mode of operation. This value is used to initialize the [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property of the created Collection Source.
  return:
    type: DevExpress.ExpressApp.PropertyCollectionSource
    description: A [](xref:DevExpress.ExpressApp.PropertyCollectionSource) object representing a Collection Source for a nested List View.
seealso: []
---
