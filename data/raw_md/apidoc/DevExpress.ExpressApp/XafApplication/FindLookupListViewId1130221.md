---
uid: DevExpress.ExpressApp.XafApplication.FindLookupListViewId(System.Type)
name: FindLookupListViewId(Type)
type: Method
summary: Returnes the ID of the Lookup List View which is used for objects of a specified type by default.
syntax:
  content: public string FindLookupListViewId(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A string value that represents a business object type.
  return:
    type: System.String
    description: A string value that represents the ID of the Lookup List View used to display objects whose type is specified by the _objectType_ parameter.
seealso: []
---
Use this method when you need to specify the ID of the Lookup List View which must be created for the current object type. For example, when using the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) method to create a Lookup List View, you need to pass the ID of the Lookup List View to be created. The **FindLookupListViewId** method returns the value of the **DefaultLookupListViewId** property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node. This node defines the type passed as the _viewId_ parameter.