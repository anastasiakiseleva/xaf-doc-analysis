---
uid: DevExpress.ExpressApp.PropertyCollectionSource.IsObjectFitForCollection(System.Object)
name: IsObjectFitForCollection(Object)
type: Method
summary: Tries to determine whether the specified object satisfies the criteria contained in the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) dictionary.
syntax:
  content: public override bool? IsObjectFitForCollection(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object that must be checked against the criteria contained in the `Criteria` dictionary.
  return:
    type: System.Nullable{System.Boolean}
    description: '`true` if the specified object satisfies the criteria contained in the `Criteria` dictionary; `false` if the object does not satisfies the criteria; `null` if it cannot be determined.'
seealso: []
---
This method returns a `Nullable\<Boolean>`-type value. It can return `null` if the specified object cannot be checked against the criteria contained in the `Criteria` dictionary.

This method is intended for internal use.