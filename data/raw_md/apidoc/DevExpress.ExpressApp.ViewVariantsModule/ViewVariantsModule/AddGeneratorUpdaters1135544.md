---
uid: DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the **UpdateNavigationItemNodeGenerator** and **UpdateModelListViewNodesGenerator** Generator Updaters.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso:
- linkId: "113198"
- linkId: "112810"
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **UpdateNavigationItemNodeGenerator** initializes the [IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings.GenerateRelatedViewVariantsGroup) property with a default value. The **UpdateModelListViewNodesGenerator** creates default View Variant nodes.