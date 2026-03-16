---
uid: DevExpress.ExpressApp.BaseObjectSpace.CanInstantiate(System.Type)
name: CanInstantiate(Type)
type: Method
summary: Indicates whether instances of a particular type can be created.
syntax:
  content: public virtual bool CanInstantiate(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: An object type for which it must be determined whether its instances can be created.
  return:
    type: System.Boolean
    description: '**true**, if instances of the specified type can be created; otherwise, **false**.'
seealso: []
---
To determine whether a particular type can be instantiated, use the IEntityStore (Type Info Source) object that must be passed as a parameter in the Object Space's constructor. To be instantiated, the requested type must be contained in the **IEntityStore.RegisteredEntities** collection.