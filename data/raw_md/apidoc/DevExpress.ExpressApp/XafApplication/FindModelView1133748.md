---
uid: DevExpress.ExpressApp.XafApplication.FindModelView(System.String)
name: FindModelView(String)
type: Method
summary: Provides access the [Application Model](xref:112580) node that defines a specified [View](xref:112611).
syntax:
  content: public virtual IModelView FindModelView(string viewId)
  parameters:
  - id: viewId
    type: System.String
    description: A string value that specifies the identifier of the View to be found in the Application Model.
  return:
    type: DevExpress.ExpressApp.Model.IModelView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelView) object that represents the Application Model node that defined the View specified by the _viewId_ parameter.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.FindModelView(System.String)
---
Use this property to customize a particular [Application Model](xref:112580) node. This property returns the node whose ID attribute is set to the value specified by the _viewId_ parameter.