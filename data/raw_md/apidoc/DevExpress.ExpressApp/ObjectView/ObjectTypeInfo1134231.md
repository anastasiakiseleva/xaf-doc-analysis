---
uid: DevExpress.ExpressApp.ObjectView.ObjectTypeInfo
name: ObjectTypeInfo
type: Property
summary: Specifies metadata information on the current View's [business class](xref:113664#business-classes).
syntax:
  content: public override ITypeInfo ObjectTypeInfo { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: A @DevExpress.ExpressApp.DC.ITypeInfo object providing metadata information on the current View's business class.
seealso: []
---
You can use the returned object's [ITypeInfo.Type](xref:DevExpress.ExpressApp.DC.ITypeInfo.Type) property to obtain the @System.Type of the current View's business class.