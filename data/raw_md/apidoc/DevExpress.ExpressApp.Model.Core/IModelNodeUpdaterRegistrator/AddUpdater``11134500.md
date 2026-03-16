---
uid: DevExpress.ExpressApp.Model.Core.IModelNodeUpdaterRegistrator.AddUpdater``1(DevExpress.ExpressApp.Model.Core.IModelNodeUpdater{``0})
name: AddUpdater<T>(IModelNodeUpdater<T>)
type: Method
summary: Registers a node updater in the application.
syntax:
  content: |-
    void AddUpdater<T>(IModelNodeUpdater<T> updater)
        where T : IModelNode
  parameters:
  - id: updater
    type: DevExpress.ExpressApp.Model.Core.IModelNodeUpdater{{T}}
    description: An [](xref:DevExpress.ExpressApp.Model.Core.IModelNodeUpdater`1) object representing a node updater.
  typeParameters:
  - id: T
    description: ''
seealso: []
---
To learn about node updaters, and see an example of using this method, refer to the [Convert Application Model Differences](xref:112796) topic.