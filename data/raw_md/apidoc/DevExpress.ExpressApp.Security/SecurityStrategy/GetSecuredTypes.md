---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.GetSecuredTypes(DevExpress.ExpressApp.DC.ITypesInfo)
name: GetSecuredTypes(ITypesInfo)
type: Method
summary: Returns a list of business classes that can be secured.
syntax:
  content: public static IEnumerable<Type> GetSecuredTypes(ITypesInfo typesInfo = null)
  parameters:
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    defaultValue: "null"
    description: An @DevExpress.ExpressApp.DC.ITypesInfo object that provides access to XAF-related information on business classes.
  return:
    type: System.Collections.Generic.IEnumerable{System.Type}
    description: An **IEnumerable\<Type>** list of secured types.
seealso: []
---
By default, returns all persistent types (entries from the **XafTypesInfo.Instance.PersistentTypes** collection which have the [ITypeInfo.IsPersistent](xref:DevExpress.ExpressApp.DC.ITypeInfo.IsPersistent) property set to **true**) except for the **XPObjectType** and **ModuleInfo** types. You can add extra types (e.g., [non-persistent types](xref:116516) via the [SecurityStrategy.AdditionalSecuredTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AdditionalSecuredTypes) list). To determine whether a particular type is secured, use the [SecurityStrategy.IsSecuredType](xref:DevExpress.ExpressApp.Security.SecurityStrategy.IsSecuredType(System.Type,DevExpress.ExpressApp.DC.ITypesInfo)) method.