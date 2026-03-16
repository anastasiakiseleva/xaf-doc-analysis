---
uid: DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1
name: IModelNodeUpdater<T>
type: Interface
summary: Implemented by node updaters that [convert application model differences](xref:112796).
syntax:
  content: |-
    public interface IModelNodeUpdater<T>
        where T : IModelNode
  typeParameters:
  - id: T
    description: ''
seealso:
- linkId: DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1._members
  altText: IModelNodeUpdater<T> Members
---
Implement this interface in a class, to customize Application Model differences. To learn about node updaters, and see an example of using this method, refer to the [Convert Application Model Differences](xref:112796) topic.