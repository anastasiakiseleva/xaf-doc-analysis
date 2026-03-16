---
uid: DevExpress.ExpressApp.Security.SecurityModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Adds Generator Updaters that perform the Application Model customizations required by the Security System.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** collection.
seealso: []
---
The Application Model customizations include adding the My Details, User and Role navigation items, and object access types localization. Generally, you do not need to invoke this method from your code, as this is done automatically.