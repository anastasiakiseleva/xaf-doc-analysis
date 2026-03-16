---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Win.NotificationsOptions})
name: AddNotifications(IModuleBuilder<IWinApplicationBuilder>, Action<NotificationsOptions>)
type: Method
summary: '[!include[<\[Notifications Module\](xref:113688)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddNotifications(this IModuleBuilder<IWinApplicationBuilder> builder, Action<NotificationsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Notifications.Win.NotificationsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Notifications Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.ShowRefreshAction = true;>](~/templates/AddNotifications_Win_example.md)]