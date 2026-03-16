---
uid: DevExpress.ExpressApp.Dashboards.DashboardsModule.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the Generator Updater of the Dashboards Module.
syntax:
  content: public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso: []
---
This method is not intended to be called from your code.

A Generator Updater is a class used to customize the [Application Model](xref:112580)'s zero layer after it has been generated. The **Reports V2 Module**  creates the **Reports** | **Dashboads** navigation item if the [DashboardsModule.GenerateNavigationItem](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.GenerateNavigationItem) property is set to **true**.