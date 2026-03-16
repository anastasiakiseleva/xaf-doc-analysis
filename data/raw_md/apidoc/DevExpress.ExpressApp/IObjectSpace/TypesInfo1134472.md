---
uid: DevExpress.ExpressApp.IObjectSpace.TypesInfo
name: TypesInfo
type: Property
summary: Gets information on the business classes added to the Application Model (see [](xref:DevExpress.ExpressApp.Model.IModelBOModel)).
syntax:
  content: ITypesInfo TypesInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An object that implements the [](xref:DevExpress.ExpressApp.DC.ITypesInfo) interface.
seealso: []
---
Use this property to get information on a particular business class. For this purpose, use the [ITypesInfo.FindTypeInfo](xref:DevExpress.ExpressApp.DC.ITypesInfo.FindTypeInfo*) or [ITypesInfo.CanInstantiate](xref:DevExpress.ExpressApp.DC.ITypesInfo.CanInstantiate(System.Type)) method of the object returned by this property.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to implement the **TypesInfo** property. It's implemented in the **BaseObjectSpace** class.