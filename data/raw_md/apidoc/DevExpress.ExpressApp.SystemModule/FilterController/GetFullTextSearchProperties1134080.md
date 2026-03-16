---
uid: DevExpress.ExpressApp.SystemModule.FilterController.GetFullTextSearchProperties
name: GetFullTextSearchProperties()
type: Method
summary: Returns properties scanned by the **FullTextSearch** Action (property selection is based on the [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) property value).
syntax:
  content: public ICollection<string> GetFullTextSearchProperties()
  return:
    type: System.Collections.Generic.ICollection{System.String}
    description: An `ICollection\<String>` object that specifies properties scanned by the **FullTextSearch** [Action](xref:112622).
seealso:
- linkId: "112923"
---
Use this method when you handle the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event. The method helps you determine properties used in search operations.