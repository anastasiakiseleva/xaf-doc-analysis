---
uid: DevExpress.ExpressApp.XafApplication.GetListViewId(System.Type)
name: GetListViewId(Type)
type: Method
summary: Returns the ID of the List View which is used for objects of a specified type by default, and raises the 'CannotFindListViewWithId' exception if the appropriate View ID is not found.
syntax:
  content: public string GetListViewId(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A string value that represents a business object type.
  return:
    type: System.String
    description: A string value that represents the ID of the View used to display objects whose type is specified by the _objectType_ parameter.
seealso: []
---
This method calls the [XafApplication.FindListViewId](xref:DevExpress.ExpressApp.XafApplication.FindListViewId(System.Type)) method and raises the 'CannotFindListViewWithId' exception if the appropriate View has not been found. Use this method instead of the [XafApplication.FindListViewId](xref:DevExpress.ExpressApp.XafApplication.FindListViewId(System.Type)) method if you need an exception to be raised in an exclusive situation.