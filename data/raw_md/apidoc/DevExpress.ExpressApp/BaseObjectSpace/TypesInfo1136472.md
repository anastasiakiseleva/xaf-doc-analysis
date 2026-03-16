---
uid: DevExpress.ExpressApp.BaseObjectSpace.TypesInfo
name: TypesInfo
type: Property
summary: Gets information on the business classes added to the Application Model (see [](xref:DevExpress.ExpressApp.Model.IModelBOModel)).
syntax:
  content: public ITypesInfo TypesInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An object that implements the [](xref:DevExpress.ExpressApp.DC.ITypeInfo) interface.
seealso: []
---
Use this property to get information on a particular business class. For this purpose, use the [ITypesInfo.FindTypeInfo](xref:DevExpress.ExpressApp.DC.ITypesInfo.FindTypeInfo*) or [ITypesInfo.CanInstantiate](xref:DevExpress.ExpressApp.DC.ITypesInfo.CanInstantiate(System.Type)) method of the object returned by this property.