---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.IsSecuredType(System.Type,DevExpress.ExpressApp.DC.ITypesInfo)
name: IsSecuredType(Type, ITypesInfo)
type: Method
summary: Checks if the specified type can be secured.
syntax:
  content: public static bool IsSecuredType(Type type, ITypesInfo typesInfo = null)
  parameters:
  - id: type
    type: System.Type
    description: A **System.Type** object.
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    defaultValue: "null"
    description: An @DevExpress.ExpressApp.DC.ITypesInfo object that provides access to XAF-related information on business classes.
  return:
    type: System.Boolean
    description: '**true**, if the specified type can be secured; otherwise - **false**.'
seealso: []
---
By default, secured types are all persistent types (entries from the **XafTypesInfo.Instance.PersistentTypes** collection which have the [ITypeInfo.IsPersistent](xref:DevExpress.ExpressApp.DC.ITypeInfo.IsPersistent) property set to **true**) except for the **XPObjectType** and **ModuleInfo** types. You can add extra types (e.g., non-persistent types via the [SecurityStrategy.AdditionalSecuredTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AdditionalSecuredTypes) list). To get all secured types, use the [SecurityStrategy.GetSecuredTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.GetSecuredTypes(DevExpress.ExpressApp.DC.ITypesInfo)) method.