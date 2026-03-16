---
uid: DevExpress.ExpressApp.PropertyCollectionSource.CanApplyCriteria
name: CanApplyCriteria
type: Property
summary: Returns the value that indicates whether the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) can be filtered.
syntax:
  content: public override bool CanApplyCriteria { get; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the Collection Source's collection can be filtered; otherwise **false**."
seealso: []
---
This property is used internally in **XAF**. For instance, [](xref:DevExpress.ExpressApp.SystemModule.FilterController) will not activate for a View whose Collection Source's **CanApplyCriteria**property returns **false**.