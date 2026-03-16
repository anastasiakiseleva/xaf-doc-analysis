---
uid: DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the **FilterCaptionsLocalizationModelNodesGeneratorUpdater** Generator Updater.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController
- linkId: "112810"
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **FilterCaptionsLocalizationModelNodesGeneratorUpdater** Generator Updater creates an **OpenSaveDialogFilters** localization group containing localization items corresponding to the supported exporting file formats.