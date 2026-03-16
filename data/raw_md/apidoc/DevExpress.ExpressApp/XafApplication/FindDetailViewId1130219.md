---
uid: DevExpress.ExpressApp.XafApplication.FindDetailViewId(System.Type)
name: FindDetailViewId(Type)
type: Method
summary: Returns the ID of the Detail View which is used for objects of a specified type by default.
syntax:
  content: public string FindDetailViewId(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A string value that represents a business object type.
  return:
    type: System.String
    description: A string value that represents the ID of the View used to display objects whose type is specified by the _objectType_ parameter.
seealso: []
---
Use this method when you need to specify the ID of the View which must be created for the current object type. For instance, when using the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) method to create a Detail View, you need to pass the ID of the View to be created. The **FindDetailViewId** method returns the value of the **DefaultDetailViewId** property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node. This node defines the type passed as the _viewId_ parameter.

You can use the analogous [XafApplication.GetDetailViewId](xref:DevExpress.ExpressApp.XafApplication.GetDetailViewId(System.Type)) method to raise an exception if the appropriate View ID is not found.