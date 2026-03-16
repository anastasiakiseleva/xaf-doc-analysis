---
uid: DevExpress.ExpressApp.MultiTenancy.ITenantModelDifferenceStore.GetTenantModelDifferenceStore(DevExpress.ExpressApp.XafApplication,System.Guid)
name: GetTenantModelDifferenceStore(XafApplication, Guid)
type: Method
summary: Returns Application Model Differences for a tenant with the specified ID.
syntax:
  content: ModelStoreBase GetTenantModelDifferenceStore(XafApplication application, Guid tenantId)
  parameters:
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An object that allows you to manage the XAF application.
  - id: tenantId
    type: System.Guid
    description: The tenant identifier.
  return:
    type: DevExpress.ExpressApp.ModelStoreBase
    description: An object that provide a read-only storage for [Application Model](xref:112580) differences.
seealso:
- linkId: "404436"
---
