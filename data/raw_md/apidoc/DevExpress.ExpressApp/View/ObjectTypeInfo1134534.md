---
uid: DevExpress.ExpressApp.View.ObjectTypeInfo
name: ObjectTypeInfo
type: Property
summary: Gets the @DevExpress.ExpressApp.ObjectView.ObjectTypeInfo property value if the current @DevExpress.ExpressApp.View is @DevExpress.ExpressApp.ObjectView. Otherwise, returns *null*.
syntax:
  content: public virtual ITypeInfo ObjectTypeInfo { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: A @DevExpress.ExpressApp.DC.ITypeInfo object providing metadata information on the current View's business class.
seealso: []
---
You can use the returned object's [ITypeInfo.Type](xref:DevExpress.ExpressApp.DC.ITypeInfo.Type) property to obtai the @System.Type of the current View's business class.