---
uid: DevExpress.ExpressApp.XafApplication.GetDetailViewId(System.Type)
name: GetDetailViewId(Type)
type: Method
summary: Returns the ID of the Detail View which is used for objects of a specified type by default, and raises an exception if the appropriate View ID is not found.
syntax:
  content: public string GetDetailViewId(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A string value that represents a business object type.
  return:
    type: System.String
    description: A string value that represents the ID of the View used to display objects whose type is specified by the _objectType_ parameter.
seealso: []
---
This method calls the [XafApplication.FindDetailViewId](xref:DevExpress.ExpressApp.XafApplication.FindDetailViewId*) method and raises an exception if the appropriate View has not been found. Use this method instead of the [XafApplication.FindDetailViewId](xref:DevExpress.ExpressApp.XafApplication.FindDetailViewId*) method if you need an exception to be raised in an exclusive situation.