---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerWindowsFormsModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the **LookupListViewDefaultEditorUpdater** Generator Updater.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso:
- linkId: "112810"
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **LookupListViewDefaultEditorUpdater** Generator Updater sets the editor type of the **IEvent** Lookup List Views to @DevExpress.ExpressApp.Win.Editors.GridListEditor.