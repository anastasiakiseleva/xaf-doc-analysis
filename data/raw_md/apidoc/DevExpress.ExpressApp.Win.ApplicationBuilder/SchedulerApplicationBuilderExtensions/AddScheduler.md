---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Scheduler.Win.SchedulerOptions})
name: AddScheduler(IModuleBuilder<IWinApplicationBuilder>, Action<SchedulerOptions>)
type: Method
summary: '[!include[<\[Scheduler Module\](xref:112811)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddScheduler(this IModuleBuilder<IWinApplicationBuilder> builder, Action<SchedulerOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Scheduler.Win.SchedulerOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Scheduler Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[AddScheduler_Win_example](~/templates/AddScheduler_Win_example.md)]