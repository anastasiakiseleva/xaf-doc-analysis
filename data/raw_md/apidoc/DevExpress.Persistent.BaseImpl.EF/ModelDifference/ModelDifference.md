---
uid: DevExpress.Persistent.BaseImpl.EF.ModelDifference
name: ModelDifference
type: Class
summary: The entity used to [store model differences](xref:403527) in the database.
syntax:
  content: |-
    [ImageName("ModelEditor_ModelMerge")]
    [OptimisticLockIgnore]
    [RuleCombinationOfPropertiesIsUnique(null, DefaultContexts.Save, "UserId, ContextId")]
    public class ModelDifference : BaseObject, IModelDifference
seealso:
- linkId: DevExpress.Persistent.BaseImpl.EF.ModelDifference._members
  altText: ModelDifference Members
---
For details, refer to the [](xref:DevExpress.ExpressApp.IModelDifference) interface description.