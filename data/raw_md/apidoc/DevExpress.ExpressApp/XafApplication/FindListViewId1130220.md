---
uid: DevExpress.ExpressApp.XafApplication.FindListViewId(System.Type)
name: FindListViewId(Type)
type: Method
summary: Returns the ID of the List View which is used for objects of a specified type by default.
syntax:
  content: public string FindListViewId(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object representing a business object type.
  return:
    type: System.String
    description: A string value that represents the ID of the View used to display objects whose type is specified by the _objectType_ parameter.
seealso: []
---
Use this method when you need to specify the ID of the View which must be created for the current object type. For example, when using the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) method to create a List View, you need to pass the ID of the View to be created. The **FindListViewId** method returns the value of the **DefaultListViewId** property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node. This node defines the type passed as the _viewId_ parameter.

You can use the analogous [XafApplication.GetListViewId](xref:DevExpress.ExpressApp.XafApplication.GetListViewId(System.Type)) method to raise an exception if the appropriate View ID is not found.