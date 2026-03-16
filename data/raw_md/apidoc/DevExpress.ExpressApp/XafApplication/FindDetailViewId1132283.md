---
uid: DevExpress.ExpressApp.XafApplication.FindDetailViewId(System.Object,DevExpress.ExpressApp.View)
name: FindDetailViewId(Object, View)
type: Method
summary: Returns the ID of the [Detail View](xref:112611) which must be used for a specific object, when invoked from the source View.
syntax:
  content: public string FindDetailViewId(object obj, View sourceView)
  parameters:
  - id: obj
    type: System.Object
    description: An object for which the View ID must be determined.
  - id: sourceView
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object that represents the [View](xref:112611) from which the new Detail View will be invoked.
  return:
    type: System.String
    description: A string value that represents the ID of the View which must be used for the specified object.
seealso: []
---
Generally, you do not need to use this method. To create a Detail View for a specific object by the information on the source View, use the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) method overload that has the **sourceView** parameter.