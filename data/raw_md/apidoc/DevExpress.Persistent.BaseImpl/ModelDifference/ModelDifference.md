---
uid: DevExpress.Persistent.BaseImpl.ModelDifference
name: ModelDifference
type: Class
summary: The XPO persistent class used to [store model differences](xref:403527) in the database.
syntax:
  content: |-
    [ImageName("ModelEditor_ModelMerge")]
    [RuleCombinationOfPropertiesIsUnique(null, DefaultContexts.Save, "UserId, ContextId")]
    public class ModelDifference : BaseObject, IModelDifference
seealso:
- linkId: DevExpress.Persistent.BaseImpl.ModelDifference._members
  altText: ModelDifference Members
---
For details, refer to the [](xref:DevExpress.ExpressApp.IModelDifference) interface description.